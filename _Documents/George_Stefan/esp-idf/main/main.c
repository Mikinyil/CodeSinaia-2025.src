#include "main.h"

static const char* TAG = "lcd_example";

static void wifi_event_handler(void* arg, esp_event_base_t event_base,
                               int32_t event_id, void* event_data) {
    if (event_id == WIFI_EVENT_AP_STACONNECTED) {
        wifi_event_ap_staconnected_t* event = (wifi_event_ap_staconnected_t*)event_data;
        ESP_LOGI(TAG, "station " MACSTR " join, AID=%d",
                 MAC2STR(event->mac), event->aid);
    } else if (event_id == WIFI_EVENT_AP_STADISCONNECTED) {
        wifi_event_ap_stadisconnected_t* event = (wifi_event_ap_stadisconnected_t*)event_data;
        ESP_LOGI(TAG, "station " MACSTR " leave, AID=%d, reason=%d",
                 MAC2STR(event->mac), event->aid, event->reason);
    }
}

void wifi_init_softap(void) {
    ESP_ERROR_CHECK(nvs_flash_init());

    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    esp_netif_t* h_wifi_ap = esp_netif_create_default_wifi_ap();
    // esp_netif_dhcps_stop(h_wifi_ap);
    esp_netif_ip_info_t ipAddrInfo = {
        .ip = {
            .addr = (192 << 24) | (168 << 16) | (1 << 8) | (1),
        },
        .gw = {
            .addr = (192 << 24) | (168 << 16) | (1 << 8) | (1),
        },
        .netmask = {
            .addr = (255 << 24) | (255 << 16) | (255 << 8) | (0),
        },
    };
    esp_netif_set_ip_info(h_wifi_ap, &ipAddrInfo);

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_AP));

    ESP_ERROR_CHECK(esp_event_handler_instance_register(WIFI_EVENT,
                                                        ESP_EVENT_ANY_ID,
                                                        &wifi_event_handler,
                                                        NULL,
                                                        NULL));

    wifi_config_t wifi_config = {
        .ap = {
            .ssid = "ESP32",
            .ssid_len = 0,
            .password = "12345678",
            .max_connection = 4,
            .authmode = WIFI_AUTH_WPA2_PSK,
        },
    };

    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_AP, &wifi_config));
    ESP_ERROR_CHECK(esp_wifi_set_storage(WIFI_STORAGE_RAM));
    ESP_ERROR_CHECK(esp_wifi_start());

    ESP_LOGI(TAG, "wifi_init_softap finished.");

    webserver_init();
}

esp_err_t get_root(httpd_req_t* req) {
    httpd_resp_set_type(req, "text/html");
    httpd_resp_set_status(req, HTTPD_200);
    return httpd_resp_send(req, HTML_ROOT, HTTPD_RESP_USE_STRLEN);
}
char sz_buf[256], sz_text[64] = "Waiting...", sz_temp[17];
bool lcd_update = false;
int h2dec(char c) {
    if(c >= '0' && c <= '9')
        return c - '0';
    if(c >= 'A' && c <= 'F')
        return c - 'A' + 10;
    if(c >= 'a' && c <= 'f')
        return c - 'a' + 10;
    return 0;
}
void url_decode(char *src, char *dst)
{
    char *w = dst;
    for(char *p = src; *p; ++p, ++w) {
        if(*p == '+')
            *w = ' ';
        else if(*p == '%') {
            ++p;
            int c0 = h2dec(*p);
            ++p;
            int c1 = h2dec(*p);
            *w = (char)(c0 * 16 + c1);
        } else {
            *w = *p;
        }
    }
    *w = 0;
}
esp_err_t post_update(httpd_req_t* req) {
    memset(sz_buf, 0, sizeof sz_buf);
    httpd_req_recv(req, sz_buf, sizeof sz_buf);
    // printf("POST: %s\n", sz_buf);
    // strcpy(sz_text, sz_buf + 4);
    memset(sz_text, 0, sizeof sz_text);
    url_decode(sz_buf + 4, sz_text);

    lcd_update = true;

    httpd_resp_set_type(req, "text/html");
    httpd_resp_set_status(req, HTTPD_200);
    return httpd_resp_send(req, HTML_ROOT, HTTPD_RESP_USE_STRLEN);
}
esp_err_t httpd_not_found(httpd_req_t* req, httpd_err_code_t error) {
    httpd_resp_set_type(req, "text/plain");
    httpd_resp_set_status(req, HTTPD_404);
    return httpd_resp_send(req, "Not Found", HTTPD_RESP_USE_STRLEN);
}

void webserver_init(void) {
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();
    httpd_handle_t server = NULL;
    httpd_start(&server, &config);

    httpd_uri_t uri_root = {
        .uri = "/",
        .method = HTTP_GET,
        .handler = get_root,
    };
    httpd_register_uri_handler(server, &uri_root);
    httpd_uri_t uri_update = {
        .uri = "/update",
        .method = HTTP_POST,
        .handler = post_update,
    };
    httpd_register_uri_handler(server, &uri_update);
    httpd_register_err_handler(server, HTTPD_404_NOT_FOUND, httpd_not_found);
}

// i2c_master_bus_handle_t h_i2c_bus;
// i2c_master_dev_handle_t h_pcf8574;

void init_i2c(void) {
    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = 21,
        .sda_pullup_en = true,
        .scl_io_num = 22,
        .scl_pullup_en = true,
        .master.clk_speed = 100000,
    };
    i2c_param_config(I2C_NUM_0, &conf);
    i2c_driver_install(I2C_NUM_0, conf.mode, 0, 0, 0);
}

i2c_lcd_pcf8574_handle_t h_lcd;

void init_lcd(void) {
    lcd_init(&h_lcd, 0x27, I2C_NUM_0);
    lcd_begin(&h_lcd, 16, 2);
    lcd_set_backlight(&h_lcd, 1);

    update_lcd();
}

void update_lcd(void) {
    lcd_clear(&h_lcd);
    lcd_set_cursor(&h_lcd, 0, 0);

    // print first line
    memset(sz_temp, 0, sizeof sz_temp);
    strncpy(sz_temp, sz_text, 16);
    lcd_print(&h_lcd, sz_temp);
    if (strlen(sz_text) > 16) {
        memset(sz_temp, 0, sizeof sz_temp);
        strncpy(sz_temp, sz_text + 16, 16);
        lcd_set_cursor(&h_lcd, 0, 1);
        lcd_print(&h_lcd, sz_temp);
    }
    if (strlen(sz_text) > 32) {
        lcd_clear(&h_lcd);
        lcd_set_cursor(&h_lcd, 0, 0);
        lcd_print(&h_lcd, "mesage too long");
    }
    printf("sz_text: '%s'\n", sz_text);
    if (!strcmp(sz_text, "clear")) {
        lcd_clear(&h_lcd);
    }
}

void app_main(void) {
    wifi_init_softap();

    init_i2c();
    init_lcd();

    while(true) {
        if(lcd_update)
            update_lcd();
        lcd_update = false;
        vTaskDelay(10);
    }
}