from Speech.player import Player
from Utils.timer import Timer
from Utils.stepper import Stepper
from Utils.stateMachine import StateMachine
import os
stepperLocation = open('stepperLoc', 'w')
stepperLocationR = open('stepperLoc', 'r')


class startup(object):
    def __init__(self, neopixel, stepper: Stepper, mp3: Player) -> None:
        self.__state = StateMachine(True)
        self.__neo = neopixel
        self.__done = False
        self.__speechTimer = Timer(4000)
        self.__mp3 = mp3

        for led in range(5):
            neopixel[led] = (0, 0, 0)

        neopixel.write()

        f = open("stepperLoc.txt", "r")
        stepperLoc = f.readline()
        f.close()

        if stepperLoc == 'Open':
            outFile = open('stepperLoc.txt', 'w')
            outFile.write('Closed')
            outFile.close()
            stepper.step(1000, 1)  # Close

        self.__setStates()
        print('Init Startup Scene')

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__start())
        stateMachine.add(lambda: self.__StartTalk())
        stateMachine.add(lambda: self.__wait(20000))
        stateMachine.add(lambda: self.__lightStart())

    def __wait(self, delay: int) -> None:
        if self.__speechTimer.check(delay):
            print('Timer Ended.')
            self.__state.nextState()

    def __start(self) -> None:
        self.__speechTimer.reset()
        self.__state.nextState()

    def run(self) -> None:
        self.__state.checkState()
        if self.__done:
            return True

    def __StartTalk(self) -> None:
        print('Start Speech Start')
        self.__mp3.SetVolume(50)
        self.__mp3.PlaySpecificInFolder(4, 1)
        self.__state.nextState()

    def __lightStart(self) -> None:
        for led in range(5):
            self.__neo[led] = (0, 25, 0)

        self.__neo.write()
        self.__state.nextState()
        self.__done = True
