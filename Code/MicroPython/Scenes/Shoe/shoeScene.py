from machine import Pin
from micropython import const
from Speech.player import Player
from Utils.stateMachine import StateMachine
from Utils.buttons import Button
from Utils.timer import Timer

__MOVE_PLAYER = const(100)
__NOT_PRESSED = const(250)


class shoeScene:

    def __init__(self, neopixel, btnLeft: int, btnRight: int, mp3: Player) -> None:
        print('Init shoeScene..')
        self.__mp3 = mp3
        self.__state = StateMachine(True)
        self.__neo = neopixel

        self.__leftButtonPressed = False
        self.__done = False
        self.__currentLed = 0
        self.__prevLed = -1
        self.__btnLeft = Button(
            btnLeft, __MOVE_PLAYER)
        self.__btnRight = Button(
            btnRight, __MOVE_PLAYER)

        self.__notPressedTimer = Timer(__NOT_PRESSED)

        for led in range(16):
            neopixel[led] = (0, 0, 0)

        neopixel.write()

        self.__setStates()
        print('Done Init shoeScene')

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__start())
        stateMachine.add(lambda: self.__runningMan(self.__neo))
        stateMachine.add(lambda: self.__finish(self.__neo))

    def run(self) -> None:
        self.__state.checkState()
        if self.__done:
            return True

    def __start(self) -> None:
        print('Starting ShoeScene...')
        self.__mp3.PlaySpecificInFolder(1, 1)
        self.__mp3.EnableLoop()
        self.__state.nextState()

    def __runningMan(self, neopixel) -> None:
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
            for led in range(13):
                if led < self.__currentLed:
                    neopixel[led] = (25, 25, 25)
                else:
                    neopixel[led] = (0, 0, 0)

            neopixel.write()

            if self.__currentLed >= 13:
                print('goto Finish')
                self.__state.nextState()

    def __finish(self, neopixel) -> None:
        for led in range(13):
            neopixel[led] = (0, 15, 0)
        for led in range(13, 16):
            neopixel[led] = (25, 25, 25)

        neopixel.write()
        self.__done = True

        self.__mp3.Stop()
        self.__state.nextState()
