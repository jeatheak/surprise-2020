
from Utils.buttons import Buttons, UP, DOWN, RIGHT, LEFT
from Scenes.Street.utils import Utils
from Scenes.Street.renderStreet import RenderStreet
from Scenes.Street.player import Player as PlayerMove
from Utils.stateMachine import StateMachine
from Utils.timer import Timer
from Speech.player import Player


class streetScene(object):
    def __init__(self, neopixel, mp3: Player, buttons: Buttons) -> None:
        self.__renderStreet = RenderStreet(neopixel)
        self.__neo = neopixel
        self.__mp3 = mp3
        self.__done = False
        self.__state = StateMachine(True)
        self.__speechTimer = Timer(4000)
        self.__buttons = buttons
        self.playerPosition = [
            [1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0],
        ]

        for led in range(34):
            neopixel[led] = (0, 0, 0)
        neopixel.write()

        self.__setStates()

    def run(self):
        self.__state.checkState()
        if self.__done:
            return True

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__GiveSpeech())
        stateMachine.add(lambda: self.__startStreetScene())
        stateMachine.add(lambda: self.__play())
        stateMachine.add(lambda: self.__finish())

    def __play(self) -> None:
        # Move traffic
        self.__renderStreet.moveTraffic()

        # Perform Player check
        self.checkMove()

        # render Led strips
        self.__renderStreet.renderStreetLeds(self.playerPosition)

        if self.playerPosition[5][0] == 1:
            print('Player has Finished!')
            self.__state.nextState()

    def __finish(self) -> None:
        self.__renderStreet.renderFinish()
        self.__mp3.Stop()
        self.__done = True
        self.__state.nextState()

    def __GiveSpeech(self) -> None:
        if self.__speechTimer.check():
            self.__state.nextState()

    def __startStreetScene(self) -> None:
        print('Starting StreetScene')
        self.__mp3.PlaySpecificInFolder(2, 1)
        self.__mp3.EnableLoop()
        self.__state.nextState()

    def checkMove(self) -> None:
        btn = self.__buttons.checkMove()

        if btn != 0:
            print(btn)

        if btn == LEFT:
            self.__movePlayerPos(LEFT)
        elif btn == RIGHT:
            self.__movePlayerPos(RIGHT)
        elif btn == DOWN:
            self.__movePlayerPos(DOWN)
        elif btn == UP:
            self.__movePlayerPos(UP)

    def __movePlayerPos(self, direction) -> None:
        playerStreetPos = self.playerPosition

        for row in range(len(playerStreetPos)):
            for cell in range(len(playerStreetPos[row])):

                if (playerStreetPos[row][cell] == 1):

                    if (direction == RIGHT and cell > 0):
                        playerStreetPos[row][cell - 1] = 1
                        playerStreetPos[row][cell] = 0

                        return

                    elif (direction == LEFT and cell <= len(playerStreetPos)):
                        playerStreetPos[row][cell + 1] = 1
                        playerStreetPos[row][cell] = 0

                        return

                    elif (direction == UP):
                        if row == 0:
                            playerStreetPos[1][4] = 1
                            playerStreetPos[row][cell] = 0

                        elif (row > 0 and row < 4):
                            playerStreetPos[row + 1][cell] = 1
                            playerStreetPos[row][cell] = 0

                        elif (row == 4):
                            playerStreetPos[row + 1][0] = 1
                            playerStreetPos[row][cell] = 0

                        return

                    elif (direction == DOWN):
                        if row == 5:
                            playerStreetPos[row - 1][4] = 1
                            playerStreetPos[row][cell] = 0

                        elif (row > 1 and row < 6):
                            playerStreetPos[row - 1][cell] = 1
                            playerStreetPos[row][cell] = 0

                        elif (row == 1):
                            playerStreetPos[0][0] = 1
                            playerStreetPos[row][cell] = 0

                        return
