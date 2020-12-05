from machine import Pin
from neopixel import NeoPixel
from .utils import Utils
from Utils.timer import Timer

streetScene = [
    [0],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0]
]

brightness = 35
streetBrightness = 0


class RenderStreet(object):
    def __init__(self, neoPixel) -> None:
        self.__slowTrafficTimer = Timer(1500)
        self.__fastTrafficTimer = Timer(700)
        self.__neo = neoPixel

    def moveTraffic(self):
        if(self.__slowTrafficTimer.check()):
            streetScene[1] = Utils.rightRotation(streetScene[1])
            streetScene[4] = Utils.leftRotation(streetScene[4])

        if(self.__fastTrafficTimer.check()):
            streetScene[2] = Utils.rightRotation(streetScene[2])
            streetScene[3] = Utils.leftRotation(streetScene[3])

    def renderFinish(self):
        currentLed = 0
        for row in range(len(streetScene)):
            for cell in range(len(streetScene[row])):
                self.__neo[currentLed] = (0, 25, 0)
                currentLed = currentLed + 1
        self.__neo.write()

    def renderStreetLeds(self, playerposition):
        np = self.__neo
        currentLed = 0
        for row in range(0, len(streetScene)):
            if(row % 2) == 0:
                for y in range(0, len(streetScene[row])):
                    if playerposition[row][y] == 1:
                        if (streetScene[row][y] == 1):
                            print('hit')
                            playerposition[row][y] = 0
                            playerposition[0][0] = 1
                        else:
                            np[currentLed] = (
                                brightness, brightness, brightness)
                    elif streetScene[row][y] == 1:
                        np[currentLed] = (0, brightness, 0)
                    else:
                        np[currentLed] = (
                            streetBrightness, 0, 0)
                    currentLed = currentLed + 1
            else:
                for y in range(len(streetScene[row]) - 1, -1, -1):
                    if playerposition[row][y] == 1:
                        if (streetScene[row][y] == 1):
                            print('hit')
                            playerposition[row][y] = 0
                            playerposition[0][0] = 1
                        else:
                            np[currentLed] = (
                                brightness, brightness, brightness)
                    elif streetScene[row][y] == 1:
                        np[currentLed] = (0, brightness, 0)
                    else:
                        np[currentLed] = (
                            streetBrightness, 0, 0)
                    currentLed = currentLed + 1

        np.write()
