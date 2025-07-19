#include <WiFi.h>
#include <WebServer.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Changed to 16x2 LCD (common size)

// Access Point credentials
const char* ssid = "ESP32";         
const char* password = "12345678";  

// IP Address details 
IPAddress local_ip(192, 168, 1, 1);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

//webpage
const String str = R"html(
<!DOCTYPE html>
<html>
  <head>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>esp32 WebServer to LCD</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 0;
        padding: 20px;
      }
      h1 {
        color: #444;
      }
      form {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        background: #f5f5f5;
        border-radius: 10px;
      }
      input,
      button {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
      }
      button {
        background: #4caf50;
        color: white;
        border: none;
        cursor: pointer;
      }
      button:hover {
        background: #45a049;
      }
    </style>
  </head>
  <body>
    <h1>esp32 WebServer to LCD</h1>
    <form action="/update" method="POST">
      <label for="txt">Text</label>
      <input
        type="text"
        id="txt"
        name="txt"
        maxlength="32"
      />
      <button type="submit">Update LCD</button>
    </form>
  </body>
</html>

)html";
 
//server
WebServer server(80);

String txt = "Waiting...";

void setup() {
  Serial.begin(115200);
  
  // Access Point init
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);
  
  //handles pentru diferite envenimente
  server.on("/", handle_OnConnect);
  server.on("/update", HTTP_POST, handle_Update); 
  server.onNotFound(handle_NotFound);
  
  server.begin();
  Serial.println("HTTP server started");
  
  // LCD init
  lcd.init();
  lcd.backlight();
  updateLCD();
}

void loop() {
  server.handleClient();
}

void updateLCD() {
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(txt.substring(0, 16));
  if (txt.length() > 16) {
      lcd.setCursor(0,1);
      lcd.print(txt.substring(16, 32));
    }
    if ( txt.length() > 32){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("message too long");
    }
    if ( txt == "clear" ) {
      lcd.clear();  
    }
}

void handle_OnConnect() {
  server.send(200, "text/html", str);
}

void handle_Update() {
  //value for the lcd in the webpage
  if (server.hasArg("txt")) {
    txt = server.arg("txt");
  } 
  updateLCD();
  server.send(200, "text/html", str);
}

void handle_NotFound() {
  server.send(404, "text/plain", "Not found");
}

