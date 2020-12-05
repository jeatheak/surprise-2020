from Utils.stepper import Stepper
from Utils.stateMachine import StateMachine
import os
stepperLocation = open('stepperLoc', 'w')
stepperLocationR = open('stepperLoc', 'r')


class startup(object):
    def __init__(self, neopixel, stepper: Stepper) -> None:
        self.__state = StateMachine(True)
        self.__neo = neopixel
        self.__done = False

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

    def run(self) -> None:
        self.__state.checkState()
        if self.__done:
            return True

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__lightStart())

    def __lightStart(self) -> None:
        for led in range(5):
            self.__neo[led] = (0, 25, 0)

        self.__neo.write()
        self.__state.nextState()
        self.__done = True
