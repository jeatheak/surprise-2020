#import Scenes.Scenes


from Utils.stepper import create as StepperCreate
from machine import Pin
from neopixel import NeoPixel

# print('init Pixel')
# pinNeo = Pin(16, Pin.OUT)
# neo = NeoPixel(pinNeo, 34)


# for led in range(34):
#     neo[led] = (25, 25, 25)


# neo.write()
# print('Done writing leds')

print('start stepper')


s1 = StepperCreate(Pin(27, Pin.OUT), Pin(25, Pin.OUT),
                   Pin(32, Pin.OUT), Pin(12, Pin.OUT), delay=1)
s1.step(500, -1)  # Open
s1.step(500)  # close
