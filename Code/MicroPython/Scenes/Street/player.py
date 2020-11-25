from machine import Pin, const
from Utils.timer import Timer

LEFT = const(1)
RIGHT = const(2)
DOWN = const(3)
UP = const(4)

btnLeft = Pin(17, Pin.IN, Pin.PULL_UP)
btnRight = Pin(19, Pin.IN, Pin.PULL_UP)
btnDown = Pin(18, Pin.IN, Pin.PULL_UP)
btnUp = Pin(23, Pin.IN, Pin.PULL_UP)

__MOVE_PLAYER_SPEED = const(250)


class Player(object):
    def __init__(self) -> None:
        self.__buttonTimer = Timer(__MOVE_PLAYER_SPEED)

    def checkMove(self, playerPosition) -> None:
        btnTimer = self.__buttonTimer

        if btnLeft.value() and btnTimer.check():
            self.__movePlayerPos(LEFT, playerPosition)
        elif btnRight.value() and btnTimer.check():
            self.__movePlayerPos(RIGHT, playerPosition)
        elif btnDown.value() and btnTimer.check():
            self.__movePlayerPos(DOWN, playerPosition)
        elif btnUp.value() and btnTimer.check():
            self.__movePlayerPos(UP, playerPosition)

    def __movePlayerPos(self, direction, playerStreetPos) -> None:
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
