#include "Freenove_WS2812_Lib_for_ESP32.h"

#define LEDS_COUNT  2
#define LEDS_PIN  16
#define CHANNEL   0

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 26;    // the number of the pushbutton pin
const int ledPin = 2;      // the number of the LED pin
const int brightness = 25; // in %

Freenove_ESP32_WS2812 strip = Freenove_ESP32_WS2812(LEDS_COUNT, LEDS_PIN, CHANNEL, TYPE_GRB);

// Variables will change:
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin

// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() {
  pinMode(buttonPin, INPUT);
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

void loop() {
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        ledState = !ledState;
      }
    }
  }

  digitalWrite(ledPin, ledState);
  
  if(ledState){
    Serial.println("HIGH");
    strip.setLedColorData(0, convert(brightness),0,0);
    strip.setLedColorData(1, 0,0,convert(brightness));
  }else{
    Serial.println("LOW");
    strip.setLedColorData(0, 0,convert(brightness),0);
    strip.setLedColorData(1, 0,convert(brightness),0);
  }
  
  lastButtonState = reading;
  strip.show();
}
