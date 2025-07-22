#include <LiquidCrystal_I2C.h>

//define lcd
LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup() {
  //serial and lcd init
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  
  //write on lcd
  lcd.setCursor(0, 0);
  lcd.print("ready");

  lcd.setCursor(0,1);
  lcd.print("waiting...");
}

void loop() {
  //if we have a message
  if ( Serial.available()) {
    //display the message 
    lcd.clear();
    lcd.setCursor(0,0);

    String txt = Serial.readStringUntil('\n');
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
}