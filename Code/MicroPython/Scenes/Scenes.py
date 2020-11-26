
from Speech.player import Player
from Utils.buttons import Buttons
from Utils.stateMachine import StateMachine
from Scenes.Sewer import sewerScene
from Scenes.Shoe import shoeScene
from Scenes.Street import streetScene
from Scenes.Startup import startup

from machine import Pin
from neopixel import NeoPixel

import Scenes.pindefinitions as p

pinStreet = Pin(p.STREET_DIN, Pin.OUT)
neoStreet = NeoPixel(pinStreet, 34)
pinShoe = Pin(p.SHOE_DIN, Pin.OUT)
neoShoe = NeoPixel(pinShoe, 5)

mp3 = Player(1, p.DF_TX_PIN, p.DF_RX_PIN)

print('init Main done')
print('Starting main loop...')

buttons = Buttons(p.UP_ARROW, p.DOWN_ARROW, p.LEFT_ARROW, p.RIGHT_ARROW)
sewer = sewerScene(p.SEWER_SEGMENT_CLK, p.SEWER_SEGMENT_DIO, buttons, mp3)
shoe = shoeScene(neoShoe, p.LEFT_SIDE_BTN, p.RIGHT_SIDE_BTN, buttons, mp3)
street = streetScene(neoStreet, mp3)
start = startup()

stateMachine = StateMachine()
stateMachine.add(lambda: start.run())
stateMachine.add(lambda: shoe.run())
stateMachine.add(lambda: sewer.run())

while 1:

    stateMachine.checkState()
