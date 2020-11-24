from machine import Pin
import time

btnSLeft = Pin(23, Pin.IN, Pin.PULL_UP)
btnSRight = Pin(19, Pin.IN, Pin.PULL_UP)


def shoeScene(neopixel, state):

    if state == 2:
        state = runningMan(neopixel, state)
    elif state == 3:
        neopixel[0] = (25, 0, 25)
        neopixel[1] = (25, 0, 25)
        neopixel[2] = (25, 0, 25)
        neopixel.write()
        state = 4

    return state


buttonPressRate = 0
movePlayerSpeed = 100
currentLed = 0
prevLed = -1
leftButtonPressed = 0
notPressedDelta = 0
notPressedRate = 0


def runningMan(neopixel, state):
    global buttonPressRate
    global currentLed
    global leftButtonPressed
    global notPressedRate

    buttonDelta = time.ticks_diff(time.ticks_ms(), buttonPressRate)
    notPressedDelta = time.ticks_diff(time.ticks_ms(), notPressedRate)

    if notPressedDelta > 250:
        if(currentLed >= 0):
            currentLed -= 1
        notPressedRate = time.ticks_ms()

    if btnSLeft.value() and not leftButtonPressed and not btnSRight.value():
        if buttonDelta > movePlayerSpeed:
            currentLed += 1
            leftButtonPressed = 1
            buttonPressRate = time.ticks_ms()
    elif btnSRight.value() and leftButtonPressed:
        if buttonDelta > movePlayerSpeed:
            currentLed += 1
            leftButtonPressed = 0
            buttonPressRate = time.ticks_ms()

    if prevLed < currentLed:
        for led in range(5):
            if led < currentLed:
                neopixel[led] = (25, 25, 25)
            else:
                neopixel[led] = (0, 0, 0)

        neopixel.write()

        if currentLed >= 5:
            return state + 1

    return state
