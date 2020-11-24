import Utils.tm1637
from micropython import const
from machine import Pin
import time
from Utils.buttons import Buttons, UP, DOWN, LEFT, RIGHT
from random import randint
from Speech.player import Player
from Utils.timer import Timer, DoubleTimer

__RANDOM_FLASH_RATE = const(100)
__ACTIVE_TIME = const(1000)
__FINISH_FLASH_RATE = const(150)
__SPEECH_DELAY = const(3000)
__FINISH_CODE = [1, 2, 0, 4]
__nums = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]

class sewerScene(object):
    def __init__(self, clk: int, dio: int, buttons: Buttons, mp3: Player) -> None:
        self.__state = 0
        self.__tm = Utils.tm1637.TM1637(clk=Pin(clk), dio=Pin(dio))
        self.__position = 0
        self.__btns = buttons
        self.__mp3 = mp3
        self.__numberFlashTimer = DoubleTimer(__FINISH_FLASH_RATE, __FINISH_FLASH_RATE * 1.5)
        self.__resetTimer = Timer(__ACTIVE_TIME)
        self.currentCode = [0, 0, 0, 0]

        print('SewerScene: done init')

    def run(self):
        if self.__state == 0:
            print('Starting the SewerScene')
            self.__mp3.PlaySpecificInFolder(3, 1)
            self.__mp3.EnableLoop()
            self.__state = 1
        elif self.__state == 1:
            self._showRandomNumbers()
            if self.__btns.checkMove() > 0:
                self.__tm.number(0000)
                self._writeCode([0, 0, 0, 0])
                self.__resetTimer.reset()
                self.__state = 2
        elif self.__state == 2:
            btnState = self.__btns.checkMove()

            if btnState == UP:
                if(self.currentCode[self.__position] < 9):
                    self.__resetTimer.reset()
                    self.currentCode[self.__position] += 1
                    self._writeCode(self.currentCode)
                    print('New Code: ', self.currentCode)
            elif btnState == DOWN:
                if(self.currentCode[self.__position] > 0):
                    self.__resetTimer.reset()
                    self.currentCode[self.__position] -= 1
                    self._writeCode(self.currentCode)
                    print('New Code: ', self.currentCode)
            elif btnState == RIGHT:
                if(self.__position < 3):
                    self.__resetTimer.reset()
                    self.__position += 1
                    print('New Position: ', self.__position)
            elif btnState == LEFT:
                if(self.__position > 0):
                    self.__resetTimer.reset()
                    self.__position -= 1
                    print('New Position: ', self.__position)
            else:
                self._resetIfInactive()
                self._showActiveNumber()

            if self.currentCode == __FINISH_CODE:
                print('You Won!')
                self.__state = 3

        elif self.__state == 3:
            if self.__resetTimer.check(__SPEECH_DELAY) == 1:
                self.__mp3.PlaySpecificInFolder(3, 2)
                self.__state = 4
        elif self.__state == 4:
            self._showFinish()
        else:
            self.__tm.write([0, 0, 0, 0])
       

    def _showFinish(self):
        if self.__numberFlashTimer.check(__FINISH_FLASH_RATE, __FINISH_FLASH_RATE * 2) == 1:
            self.__tm.write([0, 0, 0, 0])
        elif self.__numberFlashTimer.check(__FINISH_FLASH_RATE, __FINISH_FLASH_RATE * 2) == 2:
            self._writeCode(self.currentCode)

    def _resetIfInactive(self):
        if self.__resetTimer.check():
            self.__state = 1
            self.__position = 0

    def _showActiveNumber(self):
        if self.__numberFlashTimer.check() == 1:
            self.__tm.write([0], self.__position)
        elif self.__numberFlashTimer.check() == 2:
            self._writeCode(self.currentCode)

    def _writeCode(self, arr):
        self.currentCode = arr

        self.__tm.write([__nums[arr[0]], __nums[arr[1]],
                        __nums[arr[2]], __nums[arr[3]]])

    def _showRandomNumbers(self):
        if self.__resetTimer.check(__RANDOM_FLASH_RATE):
            code = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
            self._writeCode(code)
