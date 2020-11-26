from machine import  const
from Utils.buttons import Buttons, UP, DOWN, RIGHT, LEFT

__MOVE_PLAYER_SPEED = const(250)


class Player(object):
    def __init__(self, buttons: Buttons ) -> None:
        self.__buttons = buttons

    def checkMove(self, playerPosition) -> None:

        if self.__buttons.checkMove() == LEFT:
            self.__movePlayerPos(LEFT, playerPosition)
        elif self.__buttons.checkMove() == RIGHT:
            self.__movePlayerPos(RIGHT, playerPosition)
        elif self.__buttons.checkMove() == DOWN:
            self.__movePlayerPos(DOWN, playerPosition)
        elif self.__buttons.checkMove() == UP:
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
