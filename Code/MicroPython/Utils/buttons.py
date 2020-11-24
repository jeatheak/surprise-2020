from micropython import const
from machine import Pin
from Utils.timer import Timer

LEFT = const(1)
RIGHT = const(2)
DOWN = const(3)
UP = const(4)
_movePlayerSpeed = const(250)

class Buttons(object):
    def __init__(self, up: int, down: int, left: int, right: int) -> None:
        self._down = Pin(down, Pin.IN, Pin.PULL_UP)
        self._up = Pin(up, Pin.IN, Pin.PULL_UP)
        self._left = Pin(left, Pin.IN, Pin.PULL_UP)
        self._right = Pin(right, Pin.IN, Pin.PULL_UP)
        self.move = 0
        self._tm = Timer(_movePlayerSpeed)

    def _setMove(self, pin: Pin, dir: LEFT|RIGHT|DOWN|UP, str: str) -> int:
        if pin.value():
            if self._tm.check():
                print("Move ", str)
                self.move = dir
            else:
                self.move = 0
            return 1

        return 0


    def checkMove(self) -> int:
        if self._setMove(self._left,LEFT,'Left'):
            return self.move
        elif self._setMove(self._right,RIGHT,'Right'):
            return self.move
        elif self._setMove(self._up,UP,'Up'):
            return self.move
        elif self._setMove(self._down,DOWN,'Down'):
            return self.move
        else: 
            self.move = 0

        return self.move
