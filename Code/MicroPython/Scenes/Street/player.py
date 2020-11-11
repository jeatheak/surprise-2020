from machine import Pin
import time

LEFT = 1
RIGHT = 2
DOWN = 3
UP = 4

btnLeft = Pin(17, Pin.IN, Pin.PULL_UP)
btnRight = Pin(19, Pin.IN, Pin.PULL_UP)
btnDown = Pin(18, Pin.IN, Pin.PULL_UP)
btnUp = Pin(23, Pin.IN, Pin.PULL_UP)

buttonPressRate = 0

movePlayerSpeed = 250


def checkMove(playerPosition):

    global buttonPressRate
    buttonDelta = time.ticks_diff(time.ticks_ms(), buttonPressRate)

    if btnLeft.value():
        if buttonDelta > movePlayerSpeed:
            movePlayerPos(LEFT, playerPosition)
            buttonPressRate = time.ticks_ms()
    elif btnRight.value():
        if buttonDelta > movePlayerSpeed:
            movePlayerPos(RIGHT, playerPosition)
            buttonPressRate = time.ticks_ms()
    elif btnDown.value():
        if buttonDelta > movePlayerSpeed:
            movePlayerPos(DOWN, playerPosition)
            buttonPressRate = time.ticks_ms()
    elif btnUp.value():
        if buttonDelta > movePlayerSpeed:
            movePlayerPos(UP, playerPosition)
            buttonPressRate = time.ticks_ms()


def movePlayerPos(direction, playerStreetPos):
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
