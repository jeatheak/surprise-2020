
from Speech.player import Player
from Utils.buttons import Buttons
from Utils.stateMachine import StateMachine
from Scenes.Sewer.sewerScene import sewerScene
from Scenes.Shoe.shoeScene import shoeScene
from Scenes.Street.streetScene import streetScene
from Scenes.Startup.startup import startup

from machine import Pin
from neopixel import NeoPixel

import Scenes.pindefinitions as p

pinStreet = Pin(p.STREET_DIN, Pin.OUT)
neoStreet = NeoPixel(pinStreet, 34)
pinShoe = Pin(p.SHOE_DIN, Pin.OUT)
neoShoe = NeoPixel(pinShoe, 16)
pinStart = Pin(p.START_DIN, Pin.OUT)
neoStart = NeoPixel(pinStart, 5)
pinSewer = Pin(p.SEWER_DIN, Pin.OUT)
neoSewer = NeoPixel(pinSewer, 10)
pinFinish = Pin(p.FINAL_DIN, Pin.OUT)
neoFinish = NeoPixel(pinFinish, 10)

mp3 = Player(1, p.DF_TX_PIN, p.DF_RX_PIN)

print('init Main done')
print('Starting main loop...')

buttons = Buttons(p.UP_ARROW, p.DOWN_ARROW, p.LEFT_ARROW, p.RIGHT_ARROW)
sewer = sewerScene(p.SEWER_SEGMENT_CLK, p.SEWER_SEGMENT_DIO,
                   buttons, mp3, neoSewer, neoFinish)
shoe = shoeScene(neoShoe, p.LEFT_SIDE_BTN,
                 p.RIGHT_SIDE_BTN, mp3)
street = streetScene(neoStreet, mp3, buttons)
start = startup(neoStart)

stateMachine = StateMachine()
stateMachine.add(lambda: start.run())
# stateMachine.add(lambda: shoe.run())
# TODO: add road Lightning
stateMachine.add(lambda: sewer.run())

while 1:

    stateMachine.checkState()
