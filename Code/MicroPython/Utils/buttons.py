
from micropython import const
from machine import Pin
import time

_buttonPressRate = 0

LEFT = const(1)
RIGHT = const(2)
DOWN = const(3)
UP = const(4)
_movePlayerSpeed = const(250)


class buttons(object):
    def __init__(self, up: int, down: int, left: int, right: int) -> None:
        self._down = Pin(down, Pin.IN, Pin.PULL_UP)
        self._up = Pin(up, Pin.IN, Pin.PULL_UP)
        self._left = Pin(left, Pin.IN, Pin.PULL_UP)
        self._right = Pin(right, Pin.IN, Pin.PULL_UP)
        self.move = 0

    def checkMove(self) -> int:
        global _buttonPressRate

        buttonDelta = time.ticks_diff(time.ticks_ms(), _buttonPressRate)

        if self._left.value():
            if buttonDelta > _movePlayerSpeed:
                print("Move left")
                self.move = LEFT
                _buttonPressRate = time.ticks_ms()
            else:
                self.move = 0
        elif self._right.value():
            if buttonDelta > _movePlayerSpeed:
                print("Move right")
                self.move = RIGHT
                _buttonPressRate = time.ticks_ms()
            else:
                self.move = 0
        elif self._down.value():
            if buttonDelta > _movePlayerSpeed:
                print("Move down")
                self.move = DOWN
                _buttonPressRate = time.ticks_ms()
            else:
                self.move = 0
        elif self._up.value():
            if buttonDelta > _movePlayerSpeed:
                print("Move up")
                self.move = UP
                _buttonPressRate = time.ticks_ms()
            else:
                self.move = 0
        else:
            self.move = 0

        return self.move
