import tm1637
from micropython import const
from machine import Pin
import time
from random import randint

FINISH_CODE = const(1204)
REFRESH_RATE = const(200)


class sewerScene(object):
    def __init__(self, clk: int, dio: int, btn: Pin) -> None:
        self.state = 0
        self.tm = tm1637.TM1637(clk=Pin(clk), dio=Pin(dio))
        self._randomNumberRate = 0
        self.btn: Pin = btn
        self.currentCode = 0
        print('done init')

    def write(self):
        if self.state == 1:
            """Loop show random numbers"""
            self._showRandomNumbers()
        elif self.state == 2:
            """Check if number equals the Finish_Code"""

        else:
            """All leds off"""
            self.tm.write([0, 0, 0, 0])

    def start(self):
        """Starts the scene"""
        print('Starting the SewerScene')
        self.state = 1

    def _checkInput(self):
        """Perfoms input handling"""

    def _showRandomNumbers(self):
        _delta = time.ticks_diff(time.ticks_ms(), self._randomNumberRate)

        if _delta > REFRESH_RATE:
            code = randint(0, 9999)
            self.tm.number(code)
            self.currentCode = code
            self._randomNumberRate = time.ticks_ms()
