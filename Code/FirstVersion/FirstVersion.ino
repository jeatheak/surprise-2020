#include "Freenove_WS2812_Lib_for_ESP32.h"

#define LEDS_COUNT 35
#define LEDS_PIN 16
#define CHANNEL 0

#define LEFT 0
#define DOWN 1
#define RIGHT 2
#define UP 3

const int LBTN = 17, DBTN = 18, RBTN = 19, UBTN = 23;
Freenove_ESP32_WS2812 strip = Freenove_ESP32_WS2812(LEDS_COUNT, LEDS_PIN, CHANNEL, TYPE_GRB);

void setup()
{
  pinMode(LBTN, INPUT);
  pinMode(DBTN, INPUT);
  pinMode(RBTN, INPUT);
  pinMode(UBTN, INPUT);

  Serial.begin(115200);
  strip.begin();
}
int convert(int bit)
{
  if (bit > 100)
    bit = 100;
  else if (bit < 0)
    bit = 0;

  return ((255 / 100) * bit);
}

double pulsState = 0.1;
int pulseWay = 1;
void pulseLight(int r, int g, int b, int ledStart, int ledEnd)
{
  for (int i = ledStart; i < ledEnd; i++)
  {
    strip.setLedColorData(i, convert(r * pulsState), convert(g * pulsState), convert(b * pulsState));
  }

  if (pulsState >= 1)
    pulseWay = 0;
  else if (pulsState <= 0.1)
    pulseWay = 1;

  if (pulseWay)
    pulsState += 0.005;
  else
    pulsState -= 0.005;
}

//===== Street Scene =====//
int playerStreetPos[6][8] =
    {
        {1},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0}};

void movePlayerPos(int direction)
{
  for (int row = 0; row < sizeof(playerStreetPos)/4; row++)
  {
    for (int cell = 0; cell < sizeof(playerStreetPos[row])/4; cell++)
    {
      if (playerStreetPos[row][cell] == 1)
      {
        switch (direction)
        {
        case LEFT:
          if (cell > 0)
          {
            playerStreetPos[row][cell - 1] = 1;
            playerStreetPos[row][cell] = 0;
          }
          return;
        case RIGHT:
          if (cell < sizeof(playerStreetPos[row]))
          {
            playerStreetPos[row][cell + 1] = 1;
            playerStreetPos[row][cell] = 0;
          }
          return;
        case UP:
          if (row == 0)
          {
            playerStreetPos[1][4] = 1;
            playerStreetPos[row][cell] = 0;
          }
          else if (row > 0 && row < 4)
          {
            playerStreetPos[row + 1][cell] = 1;
            playerStreetPos[row][cell] = 0;
          }
          else if (row == 4)
          {
            playerStreetPos[row + 1][0] = 1;
            playerStreetPos[row][cell] = 0;
          }
          return;
        case DOWN:
          if (row == 5)
          {
            playerStreetPos[row - 1][4] = 1;
            playerStreetPos[row][cell] = 0;
          }
          else if (row > 1 && row < 5)
          {
            playerStreetPos[row - 1][cell] = 1;
            playerStreetPos[row][cell] = 0;
          }
          else if (row == 1)
          {
            playerStreetPos[row - 1][0] = 1;
            playerStreetPos[row][cell] = 0;
          }

          return;
        }
      }
    }
  }
}

int streetTrafficPos[6][8] =
    {
        {0},
        {1, 1, 0, 1, 0, 0, 1, 0},
        {0, 1, 0, 0, 1, 0, 0, 0},
        {0, 0, 1, 0, 0, 0, 1, 0},
        {0, 1, 0, 1, 0, 0, 1, 1},
        {0}};

unsigned long trafficDelay = 0;
void streetScene(int plPos, int ledStart)
{
  int finishRow = 5;
  int ledCount = (4 * 8) + 2;

  // Wait 500ms before changing traffic
  // Set Traffic possitions
  if ((millis() - trafficDelay) > 1000)
  {
      int sizeOfRow = 8;
      // set first traffic lane
      for (int currentRowPos = sizeOfRow; currentRowPos >= 0; currentRowPos--)
      {
        if (streetTrafficPos[1][currentRowPos])
        {
          
          // set new pos
          if (currentRowPos <= sizeOfRow)
            streetTrafficPos[1][currentRowPos + 1] = 1;
          else
            streetTrafficPos[1][0] = 1;

          // set current pos
          if (currentRowPos > 0 && (streetTrafficPos[1][currentRowPos] - 1) == 1)
            streetTrafficPos[1][currentRowPos] = 1;
          else
            streetTrafficPos[1][currentRowPos] = 0;
        }
      }
      for (int currentRowPos = 0; currentRowPos < sizeOfRow; currentRowPos++)
      {
        if (streetTrafficPos[2][currentRowPos])
        {
          
          // set new pos
          if (currentRowPos > (sizeOfRow - 1))
            streetTrafficPos[2][currentRowPos - 1] = 1;
          else
            streetTrafficPos[2][0] = 1;

          // set current pos
          if (currentRowPos > (sizeOfRow - 1) && (streetTrafficPos[1][currentRowPos] + 1) == 1)
            streetTrafficPos[2][currentRowPos] = 1;
          else
            streetTrafficPos[2][currentRowPos] = 0;
        }
      }
    
    /*for (int currentRow = 3; currentRow < 5; currentRow++)
    {
      int sizeOfRow = sizeof(streetTrafficPos[currentRow])/4;
      // set second traffic lane
      for (int currentRowPos = (sizeOfRow / 2); currentRowPos < sizeOfRow; currentRowPos++)
      {
        if (streetTrafficPos[currentRow][currentRowPos])
        {
          // set new pos
          if (currentRowPos > (sizeOfRow - 1))
            streetTrafficPos[currentRow][currentRowPos - 1] = 1;
          else
            streetTrafficPos[currentRow][0] = 1;

          // set current pos
          if (currentRowPos > (sizeOfRow - 1) && (streetTrafficPos[currentRow][currentRowPos] + 1) == 1)
            streetTrafficPos[currentRow][currentRowPos] = 1;
          else
            streetTrafficPos[currentRow][currentRowPos] = 0;
        }
      }
    }*/

    trafficDelay = millis();
  }

  // Render traffic
  int currentLed = 0;
  for (int currentRow = 0; currentRow < finishRow; currentRow++)
  {
    if(currentRow == 0 || currentRow == 5)
    {
      if (streetTrafficPos[currentRow][0])
          strip.setLedColorData(currentLed, 0, convert(50), 0);
        else
          strip.setLedColorData(currentLed, convert(50), 0, 0);
      currentLed++;
    }
    else
    {
      for (int currentRowPos = 0; currentRowPos < sizeof(streetTrafficPos[currentRow])/4; currentRowPos++)
      {
        if (streetTrafficPos[currentRow][currentRowPos])
          strip.setLedColorData(currentLed, 0, convert(50), 0);
        else
          strip.setLedColorData(currentLed, convert(50), 0, 0);
      currentLed++;
    }
    }
  }

  // Render Player Position
  currentLed = 0;
  for (int currentRow = 0; currentRow < 6; currentRow++)
  {
    if(currentRow == 0 || currentRow == 5)
    {
      if (playerStreetPos[currentRow][0])
          strip.setLedColorData(currentLed, convert(50), convert(50), convert(50));
      currentLed++;
    }
    else
    {
      for (int currentRowPos = 0; currentRowPos < sizeof(playerStreetPos[currentRow])/4; currentRowPos++)
      {
        if (playerStreetPos[currentRow][currentRowPos])
          strip.setLedColorData(currentLed, convert(50), convert(50), convert(50));
        currentLed++;
      }
    }

  }
}

//==== Buttons ====//
unsigned long playerMoveSleep = 0;
int playerPos = 0;
void readButtons()
{
  if (digitalRead(RBTN))
  {
    if ((millis() - playerMoveSleep) > 500)
    {
      movePlayerPos(RIGHT);
      playerMoveSleep = millis();
    }
  }
  else if (digitalRead(LBTN))
  {
    if ((millis() - playerMoveSleep) > 500)
    {
      movePlayerPos(LEFT);
      playerMoveSleep = millis();
    }
  }
  else if (digitalRead(UBTN))
  {
    if ((millis() - playerMoveSleep) > 500)
    {
      movePlayerPos(UP);
      playerMoveSleep = millis();
    }
  }
  else if (digitalRead(DBTN))
  {
    if ((millis() - playerMoveSleep) > 500)
    {
      movePlayerPos(DOWN);
      playerMoveSleep = millis();
    }
  }
}

unsigned long mainLoopSleep = 0;
void loop()
{

  readButtons();

  if ((millis() - mainLoopSleep) > 10)
  {
    //pulseLight(0,100,0,0,28);
    streetScene(playerPos, 0);
    strip.show();
    mainLoopSleep = millis();
  }
}
