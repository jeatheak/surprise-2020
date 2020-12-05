import Utils.tm1637
from micropython import const
from machine import Pin
from Utils.buttons import Buttons, UP, DOWN, LEFT, RIGHT
from random import randint
from Speech.player import Player
from Utils.timer import Timer, DoubleTimer
from Utils.stateMachine import StateMachine


class PathLightning(object):
    def __init__(self, neopixel1, neopixel2) -> None:
        self.__pathcounter = 0
        self.__pathcounter2 = 4
        self.__neo1 = neopixel1
        self.__neo2 = neopixel2
        self.__ledTimer = Timer(500)

        for led in range(10):
            neopixel1[led] = (0, 0, 0)
        neopixel1.write()

        for led in range(10):
            neopixel2[led] = (0, 0, 0)
        neopixel2.write()

        print('SewerScene: done init')

    def lightPath1(self) -> bool:
        if self.__ledTimer.check():
            if self.__pathcounter >= 3:
                return True

            self.__neo1[self.__pathcounter] = (0, 25, 0)
            self.__neo1.write()
            self.__pathcounter += 1

            return False

    def lightPath2(self) -> bool:
        if self.__ledTimer.check():
            if self.__pathcounter >= 6:
                return True

            self.__neo1[self.__pathcounter] = (0, 25, 0)
            self.__neo1.write()
            self.__pathcounter += 1

            return False

    def lightPath3(self) -> bool:
        if self.__ledTimer.check():
            if self.__pathcounter2 >= 7:
                return True

            self.__neo2[self.__pathcounter2] = (0, 25, 0)
            self.__neo2.write()
            self.__pathcounter2 += 1

            return False
