import Utils.tm1637
from micropython import const
from machine import Pin
import time
from Utils.buttons import Buttons, UP, DOWN, LEFT, RIGHT
import array as arr
from random import randint
from Speech.player import Player

_REFRESH_RATE = const(100)
_ACTIVE_TIME = const(1000)
_ACTIVE_RATE = const(150)

_FINISH_CODE = [1, 2, 0, 4]
_nums = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]


class sewerScene(object):
    def __init__(self, clk: int, dio: int, buttons: Buttons, mp3: Player) -> None:
        self._state = 0
        self._tm = Utils.tm1637.TM1637(clk=Pin(clk), dio=Pin(dio))
        self._numberRate = 0
        self._activeTimeRate = 0
        self._position = 0
        self._btns = buttons
        self._mp3 = mp3

        self.currentCode = [0, 0, 0, 0]

        print('SewerScene: done init')

    def write(self):
        if self._state == 1:
            self._showRandomNumbers()
            if self._btns.checkMove() > 0:
                self._tm.number(0000)
                self._writeCode([0, 0, 0, 0])
                self._activeTimeRate = time.ticks_ms()
                self._state = 2
        elif self._state == 2:
            btnState = self._btns.checkMove()

            if btnState == UP:
                if(self.currentCode[self._position] < 9):
                    self._activeTimeRate = time.ticks_ms()
                    self.currentCode[self._position] += 1
                    self._writeCode(self.currentCode)
                    print('New Code: ', self.currentCode)
            elif btnState == DOWN:
                if(self.currentCode[self._position] > 0):
                    self._activeTimeRate = time.ticks_ms()
                    self.currentCode[self._position] -= 1
                    self._writeCode(self.currentCode)
                    print('New Code: ', self.currentCode)
            elif btnState == RIGHT:
                if(self._position < 3):
                    self._activeTimeRate = time.ticks_ms()
                    self._position += 1
                    print('New Position: ', self._position)
            elif btnState == LEFT:
                if(self._position > 0):
                    self._activeTimeRate = time.ticks_ms()
                    self._position -= 1
                    print('New Position: ', self._position)
            else:
                self._resetIfInactive()
                self._showActiveNumber()

            if self.currentCode == _FINISH_CODE:
                print('You Won!')
                self._mp3.PlaySpecificInFolder(3, 2)
                self._state = 3

        elif self._state == 3:
            self._showFinish()
        else:
            self._tm.write([0, 0, 0, 0])

    def start(self):
        print('Starting the SewerScene')
        self._mp3.PlaySpecificInFolder(3, 1)
        self._mp3.EnableLoop()
        self._state = 1

    def _showFinish(self):
        _delta = time.ticks_diff(time.ticks_ms(), self._numberRate)

        if _delta > _ACTIVE_RATE and _delta <= _ACTIVE_RATE * 2:
            self._tm.write([0, 0, 0, 0])
        elif _delta > _ACTIVE_RATE * 2:
            self._writeCode(self.currentCode)
            self._numberRate = time.ticks_ms()

    def _resetIfInactive(self):
        _delta = time.ticks_diff(time.ticks_ms(), self._activeTimeRate)

        if _delta > _ACTIVE_TIME:
            self._state = 1
            self._position = 0
            self._activeTimeRate = time.ticks_ms()

    def _showActiveNumber(self):
        _delta = time.ticks_diff(time.ticks_ms(), self._numberRate)

        if _delta > _ACTIVE_RATE and _delta <= _ACTIVE_RATE * 1.5:
            self._tm.write([0], self._position)
        elif _delta > _ACTIVE_RATE * 1.5:
            self._writeCode(self.currentCode)
            self._numberRate = time.ticks_ms()

    def _writeCode(self, arr):
        self.currentCode = arr

        self._tm.write([_nums[arr[0]], _nums[arr[1]],
                        _nums[arr[2]], _nums[arr[3]]])

    def _showRandomNumbers(self):
        _delta = time.ticks_diff(time.ticks_ms(), self._numberRate)

        if _delta > _REFRESH_RATE:
            code = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
            self._writeCode(code)
            self._numberRate = time.ticks_ms()
