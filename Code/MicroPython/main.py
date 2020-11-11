import time
from Scenes.streetScene import streetScene
from machine import Pin
from neopixel import NeoPixel

pin = Pin(16, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
neopixel = NeoPixel(pin, 34)  # create NeoPixel driver on GPIO0 for 8 pixels

state = 3

print('init Main done')
print('Starting main loop...')


while True:

    streetScene(neopixel, state)
