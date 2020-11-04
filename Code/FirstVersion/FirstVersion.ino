#include "Freenove_WS2812_Lib_for_ESP32.h"

#define LEDS_COUNT  2
#define LEDS_PIN  16
#define CHANNEL   0

// constants won't change. They're used here to set pin numbers:
const int leftBtnPin = 26;    // the number of the pushbutton pin
const int rightBtnPin = 18;    // the number of the pushbutton pin
const int ledPin = 2;      // the number of the LED pin
const int brightness = 10; // in %

Freenove_ESP32_WS2812 strip = Freenove_ESP32_WS2812(LEDS_COUNT, LEDS_PIN, CHANNEL, TYPE_GRB);

// Variables will change:
int ledState = HIGH;         

int buttonStateLeft, buttonStateRight;             
int lastButtonStateLeft = LOW, lastButtonStateRight = LOW;   
unsigned long lastDebounceTimeLeft = 0, lastDebounceTimeRight = 0;  

unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() {
  pinMode(leftBtnPin, INPUT);
  pinMode(rightBtnPin, INPUT);
  pinMode(ledPin, OUTPUT);

  digitalWrite(ledPin, ledState);
  Serial.begin(115200);
  
  strip.begin();
}

int convert(int bit) {
  if(bit > 100) bit = 100; 
  else if(bit < 0) bit = 0; 
  
  return ((255/100)*bit);
}

int checkBtn(int buttonPin) {
  int state = LOW;
  int reading = digitalRead(buttonPin);
  
  if (reading != lastButtonStateLeft) {
    lastDebounceTimeLeft = millis();
  }

  if ((millis() - lastDebounceTimeLeft) > debounceDelay) {
    
    if (reading != buttonStateLeft) {
      buttonStateLeft = reading;      
      /*if (buttonStateLeft == HIGH) {
        ledState = !ledState;
      }*/
    }
  }
  
  lastButtonStateLeft = reading;
  
  return buttonStateLeft;
}

unsigned long lastPosTime = 0;
int playerPos = 0;
void increasePlayerPos(int state, int sleep) {
  if(state && (millis() - lastPosTime) > sleep){
    lastPosTime = millis();
    if(playerPos < LEDS_COUNT) playerPos++;
    Serial.print("PlayerPos = ");
    Serial.println(playerPos);
  }
  
}

int mainLoopSleep = 0;
void loop() {
  int state = checkBtn(leftBtnPin);
  
  increasePlayerPos(state, 500);

  for (int i = 0; i < LEDS_COUNT; i++) {
     if(i == playerPos) strip.setLedColorData(i, 0,convert(brightness),convert(brightness));
     else strip.setLedColorData(i, 0,0,0);
  }
  
  if ((millis() - mainLoopSleep) > 10){
    strip.show();
    mainLoopSleep = millis();
  }
}
