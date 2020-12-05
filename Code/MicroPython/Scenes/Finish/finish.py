from Speech.player import Player
from Utils.stateMachine import StateMachine
from Utils.stepper import Stepper
stepperLocation = open('stepperLoc', 'w')


class finishScene(object):
    def __init__(self, neopixel, mp3: Player, stepper: Stepper) -> None:
        self.__state = StateMachine(True)
        self.__done = False
        self.__mp3 = mp3
        self.__neo = neopixel
        self.__stepper = stepper
        self.currentCode = [0, 0, 0, 0]

        neopixel[7] = (0, 0, 0)
        neopixel[8] = (0, 0, 0)
        neopixel.write()

        self.__setStates()
        print('finishScene: done init')

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__start())
        stateMachine.add(lambda: self.__setPresents(self.__neo))
        stateMachine.add(lambda: self.__openSideDoor(self.__stepper))

    def run(self) -> bool:
        self.__state.checkState()
        if self.__done:
            return True

    def __start(self) -> None:
        self.__mp3.PlaySpecificInFolder(4, 1)
        self.__mp3.EnableLoop()
        self.__state.nextState()

    def __setPresents(self, neopixel) -> None:
        neopixel[7] = (0, 150, 0)
        neopixel[8] = (100, 0, 100)
        neopixel.write()
        self.__state.nextState()

    def __openSideDoor(self, stepper: Stepper) -> None:
        f = open("stepperLoc.txt", "r")
        stepperLoc = f.readline()
        f.close()

        if stepperLoc == 'Closed':
            outFile = open('stepperLoc.txt', 'w')
            outFile.write('Open')
            outFile.close()
            stepper.step(1000, -1)  # Open

        self.__state.nextState()
