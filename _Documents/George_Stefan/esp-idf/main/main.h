#include <stdio.h>
#include <string.h>

#include "driver/gpio.h"
#include "driver/i2c_master.h"
#include "esp_event.h"
#include "esp_http_server.h"
#include "esp_log.h"
#include "esp_mac.h"
#include "esp_netif.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "i2c_lcd_pcf8574.h"
#include "lwip/err.h"
#include "lwip/sys.h"
#include "nvs_flash.h"

const char *HTML_ROOT = "<html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>esp32 WebServer to LCD</title><style> body { font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 20px; } h1 { color: #444; } form { max-width: 400px; margin: 0 auto; padding: 20px; background: #f5f5f5; border-radius: 10px; } input, button { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; } button { background: #4caf50; color: white; border: none; cursor: pointer; } button:hover { background: #45a049; } </style></head><body><h1>esp32 WebServer to LCD</h1><form action=\"/update\" method=\"POST\"><label for=\"txt\">Text</label><input type=\"text\" id=\"txt\" name=\"txt\" maxlength=\"32\" /><button type=\"submit\">Update LCD</button></form></body></html>";

void webserver_init(void);
void update_lcd(void);