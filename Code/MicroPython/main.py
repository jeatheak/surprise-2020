import time
from Scenes.streetScene import streetScene
from Scenes.shoeScene import shoeScene
from machine import Pin
from neopixel import NeoPixel

pinStreet = Pin(16, Pin.OUT)
neoStreet = NeoPixel(pinStreet, 34)
pinShoe = Pin(18, Pin.OUT)
neoShoe = NeoPixel(pinShoe, 5)

state = 1

print('init Main done')
print('Starting main loop...')


while True:

    if state == 1:
        print('Startup blablablabla...')
        state = 2
    elif state == 2:
        state = shoeScene(neoShoe, state)
    elif state > 4 and state <= 5:
        state = streetScene(neoStreet, state)
