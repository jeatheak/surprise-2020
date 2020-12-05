from micropython import const
from Utils.buttons import Buttons, UP, DOWN, RIGHT, LEFT

__MOVE_PLAYER_SPEED = const(250)


class Player(object):
    def __init__(self, buttons: Buttons) -> None:
        self.__buttons = buttons
