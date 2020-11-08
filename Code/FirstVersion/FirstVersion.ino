#include "Freenove_WS2812_Lib_for_ESP32.h"

#define LEDS_COUNT  28
#define LEDS_PIN  16
#define CHANNEL   0

// constants won't change. They're used here to set pin numbers:
const int LBTN = 17, DBTN = 18, RBTN = 19, UBTN = 23;    // the number of the pushbutton pin
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
  pinMode(LBTN, INPUT);
  pinMode(DBTN, INPUT);
  pinMode(RBTN, INPUT);
  pinMode(UBTN, INPUT);
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
void playerPosF(int state, int sleep, int left) {
  if(state && (millis() - lastPosTime) > sleep){
    lastPosTime = millis();
    if(left && playerPos < LEDS_COUNT) playerPos++;
    if(!left && playerPos >= LEDS_COUNT) playerPos--;
    Serial.print("PlayerPos = ");
    Serial.println(playerPos);
  }
  
}

double pulsState = 0.1;
int pulseWay = 1;
void pulseLight(int r,int g,int b, int ledStart, int ledEnd){
  for (int i = ledStart; i < ledEnd; i++) {
    strip.setLedColorData(i,convert(r*pulsState),convert(g*pulsState),convert(b*pulsState));
  }

  if(pulsState >= 1) pulseWay = 0;
  else if(pulsState <= 0.1) pulseWay = 1;
  
  if(pulseWay) pulsState += 0.005;
  else pulsState -= 0.005;

}

void streetScene(int plPos, int ledStart, int ledEnd){
    for (int i = ledStart; i < ledEnd; i++) {
      if(plPos == i - ledStart){
        Serial.print("PlayerPos: ");
        Serial.println(plPos);
        strip.setLedColorData(i,convert(50),convert(50),convert(50));
      }
      else strip.setLedColorData(i,convert(50),0,0);
  }

}

unsigned long playerMoveSleep = 0;
void readButtons(){
  
  if(digitalRead(RBTN)){
    if((millis() - playerMoveSleep) > 500){
      playerPos++;
      playerMoveSleep = millis();
    }
  }else if(digitalRead(LBTN)){
    if((millis() - playerMoveSleep) > 500){
      playerPos--;
      playerMoveSleep = millis();
    }
  }else if(digitalRead(UBTN)){
    if((millis() - playerMoveSleep) > 500){
      playerPos += 2;
      playerMoveSleep = millis();
    }
  }else if(digitalRead(DBTN)){
    if((millis() - playerMoveSleep) > 500){
      playerPos -= 2;
      playerMoveSleep = millis();
    }
  }
}

unsigned long mainLoopSleep = 0;
void loop() {

  readButtons();
  
  if ((millis() - mainLoopSleep) > 10){
    //pulseLight(0,100,0,0,28);
    streetScene(playerPos, 0, 8);
    strip.show();
    mainLoopSleep = millis();
  }
}
