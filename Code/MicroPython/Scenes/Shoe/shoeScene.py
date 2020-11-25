from machine import Pin, const
from Speech.player import Player
from Utils.stateMachine import StateMachine
from Utils.buttons import Button
from Utils.timer import Timer

__MOVE_PLAYER = const(100)
__NOT_PRESSED = const(250)


class shoeScene(object):

    def __init__(self, neopixel, state, btnLeft: int, btnRight: int, mp3: Player) -> None:
        print('Init shoeScene..')
        self.mainState = state
        self.__mp3 = mp3
        self.__state = StateMachine(True)
        self.__neo = neopixel

        self.__leftButtonPressed = False
        self.__currentLed = 0
        self.__prevLed = -1
        self.__btnLeft = Button(
            Pin(btnLeft, Pin.IN, Pin.PULL_UP), __MOVE_PLAYER)
        self.__btnRight = Button(
            Pin(btnRight, Pin.IN, Pin.PULL_UP), __MOVE_PLAYER)

        self.__notPressedTimer = Timer(__NOT_PRESSED)

        self.__setStates()
        print('Done Init shoeScene')

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__start())
        stateMachine.add(lambda: self.__runningMan(self.__neo))
        stateMachine.add(lambda: self.__lightShoe())
        # stateMachine.add(1)

    def run(self) -> None:
        self.__state.checkState()

    def __start(self) -> bool:
        print('Starting ShoeScene...')
        self.__mp3.PlaySpecificInFolder(1, 1)
        self.__mp3.EnableLoop()
        return True

    def __lightShoe(self) -> bool:
        self.__neo[0] = (25, 0, 25)
        self.__neo[1] = (25, 0, 25)
        self.__neo[2] = (25, 0, 25)
        self.__neo.write()
        return True

    def __runningMan(self, neopixel) -> bool:
        btnLeft = self.__btnLeft
        btnRight = self.__btnRight

        if self.__notPressedTimer.check():
            if(self.__currentLed >= 0):
                self.__currentLed -= 1

        if btnLeft.checkMove() and not self.__leftButtonPressed and not btnRight.checkMove():
            self.__currentLed += 1
            self.__leftButtonPressed = True
        if btnRight.checkMove() and self.__leftButtonPressed and not btnLeft.checkMove():
            self.__currentLed += 1
            self.__leftButtonPressed = False

        if self.__prevLed < self.__currentLed:
            for led in range(5):
                if led < self.__currentLed:
                    neopixel[led] = (25, 25, 25)
                else:
                    neopixel[led] = (0, 0, 0)

            neopixel.write()

            if self.__currentLed >= 5:
                return True

        return False
