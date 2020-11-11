from machine import Pin
from neopixel import NeoPixel
from . import utils
import time

streetScene = [
    [0],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0]
]

slowTrafficRate = 0
fastTrafficRate = 0


def moveTraffic():
    global fastTrafficRate
    global slowTrafficRate

    slowTrafficDelta = time.ticks_diff(time.ticks_ms(), slowTrafficRate)
    fastTrafficDelta = time.ticks_diff(time.ticks_ms(), fastTrafficRate)

    if(slowTrafficDelta > 1500):
        streetScene[1] = utils.rightRotation(streetScene[1])
        streetScene[4] = utils.leftRotation(streetScene[4])
        slowTrafficRate = time.ticks_ms()

    if(fastTrafficDelta > 700):
        streetScene[2] = utils.rightRotation(streetScene[2])
        streetScene[3] = utils.leftRotation(streetScene[3])
        fastTrafficRate = time.ticks_ms()


brightness = 18
streetBrightness = 10


def renderStreetLeds(playerposition, np, state):
    currentLed = 0
    if(state == 3):
        for row in range(0, len(streetScene)):
            if(row % 2) == 0:
                for y in range(0, len(streetScene[row])):
                    if playerposition[row][y] == 1:
                        if (streetScene[row][y] == 1):
                            playerposition[row][y] = 0
                            playerposition[0][0] = 1
                        else:
                            np[currentLed] = (brightness, 0, 0)
                    elif streetScene[row][y] == 1:
                        np[currentLed] = (0, brightness, 0)
                    else:
                        np[currentLed] = (
                            0, streetBrightness, streetBrightness)
                    currentLed = currentLed + 1
            else:
                for y in range(len(streetScene[row]) - 1, -1, -1):
                    if playerposition[row][y] == 1:
                        if (streetScene[row][y] == 1):
                            playerposition[row][y] = 0
                            playerposition[0][0] = 1
                        else:
                            np[currentLed] = (brightness, 0, 0)
                    elif streetScene[row][y] == 1:
                        np[currentLed] = (0, brightness, 0)
                    else:
                        np[currentLed] = (
                            0, streetBrightness, streetBrightness)
                    currentLed = currentLed + 1
    elif state > 3:
        for row in range(len(streetScene)):
            for cell in range(len(streetScene[row])):
                np[currentLed] = (5, 5, 5)
                currentLed = currentLed + 1

    if state >= 3:
        np.write()
