from machine import Pin
from neopixel import NeoPixel
from . import utils

pin = Pin(16, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 17)  # create NeoPixel driver on GPIO0 for 8 pixels

streetScene = [
    [0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0],
]


def moveTraffic():
    streetScene[1] = utils.rightRotation(streetScene[1])
    streetScene[2] = utils.rightRotation(streetScene[2])


def renderStreetLeds(playerposition):
    currentLed = 0
    for row in range(0, len(streetScene)):
        if(row % 2) == 0:
            for y in range(0, len(streetScene[row])):
                if playerposition[row][y] == 1:
                    if (streetScene[row][y] == 1):
                        playerposition[row][y] = 0
                        playerposition[0][0] = 1
                    else:
                        np[currentLed] = (30, 0, 0)
                elif streetScene[row][y] == 1:
                    np[currentLed] = (0, 30, 0)
                else:
                    np[currentLed] = (0, 20, 20)
                currentLed = currentLed + 1
        else:
            for y in range(len(streetScene[row]) - 1, -1, -1):
                if playerposition[row][y] == 1:
                    if (streetScene[row][y] == 1):
                        playerposition[row][y] = 0
                        playerposition[0][0] = 1
                    else:
                        np[currentLed] = (30, 0, 0)
                elif streetScene[row][y] == 1:
                    np[currentLed] = (0, 30, 0)
                else:
                    np[currentLed] = (0, 20, 20)
                currentLed = currentLed + 1

    np.write()
