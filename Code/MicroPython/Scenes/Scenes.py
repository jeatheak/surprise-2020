import time
from Scenes.streetScene import streetScene
from Scenes.shoeScene import shoeScene
import Scenes.sewerScene
from machine import Pin, SOFT_RESET
from neopixel import NeoPixel
import Utils.buttons

pinStreet = Pin(16, Pin.OUT)
neoStreet = NeoPixel(pinStreet, 34)
pinShoe = Pin(18, Pin.OUT)
neoShoe = NeoPixel(pinShoe, 5)

state = 1

print('init Main done')
print('Starting main loop...')

buttons = Utils.buttons.buttons(17, 18, 19, 26)
sewerScene = Scenes.sewerScene.sewerScene(5, 23, buttons)

while 1:

    if state == 1:
        print('Startup blablablabla...')
        sewerScene.start()
        state = 6
    elif state == 2:
        state = shoeScene(neoShoe, state)
    elif state > 4 and state <= 5:
        state = streetScene(neoStreet, state)
    elif state >= 6 and state <= 7:
        sewerScene.write()
