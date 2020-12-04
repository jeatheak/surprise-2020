# from Utils.buttons import Button
# from Utils.timer import DoubleTimer, Timer
import Scenes.Scenes
# from machine import Pin


# from Speech.player import Player
# import Scenes.pindefinitions as p
# from Utils.stepper import create as StepperCreate
# from machine import Pin
# from neopixel import NeoPixel

# print('init Pixel')
# pinNeo = Pin(p.SHOE_DIN, Pin.OUT)
# neo = NeoPixel(pinNeo, 34)


# for led in range(34):
#     neo[led] = (25, 25, 25)


# neo.write()
# print('Done writing leds')

# print('start stepper')
# mp3 = Player(1, p.DF_TX_PIN, p.DF_RX_PIN)

# mp3.PlaySpecificInFolder(3, 1)
# mp3.EnableLoop()

# s1 = StepperCreate(Pin(27, Pin.OUT), Pin(25, Pin.OUT),
#                    Pin(32, Pin.OUT), Pin(12, Pin.OUT), delay=1)
# s1.step(500, -1)  # Open
# s1.step(500)  # close

# btn = Button(5, 200)
# # btnPin = Pin(5, Pin.IN, Pin.PULL_UP)

# while True:
#     btn.checkMove()
#     # print(btnPin.value())


# tim = DoubleTimer(1000, 5000)

# while True:
#     t = tim.check()
#     if t != 0:
#         print(t)
