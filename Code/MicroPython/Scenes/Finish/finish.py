import Utils.tm1637
from micropython import const
from machine import Pin
from Utils.buttons import Buttons, UP, DOWN, LEFT, RIGHT
from random import randint
from Speech.player import Player
from Utils.timer import Timer, DoubleTimer
from Utils.stateMachine import StateMachine

__RANDOM_FLASH_RATE = const(100)
__ACTIVE_TIME = const(1000)
__FINISH_FLASH_RATE = const(150)
__SPEECH_DELAY = const(3000)
__FINISH_CODE = [1, 2, 0, 4]
__nums = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]


class sewerScene(object):
    def __init__(self) -> None:
