
from Speech.player import Player
from Utils.buttons import Buttons
from Utils.stateMachine import StateMachine
from Scenes.Sewer import sewerScene
from Scenes.Shoe import shoeScene
from Scenes.Startup import startup

from machine import Pin
from neopixel import NeoPixel

pinStreet = Pin(16, Pin.OUT)
neoStreet = NeoPixel(pinStreet, 34)
pinShoe = Pin(18, Pin.OUT)
neoShoe = NeoPixel(pinShoe, 5)

mp3 = Player(1, 21, 22)

state = 1

print('init Main done')
print('Starting main loop...')

buttons = Buttons(17, 18, 19, 26)
sewer = sewerScene(5, 23, buttons, mp3)
shoe = shoeScene(neoShoe, state, 5, 23, buttons, mp3)
start = startup()

stateMachine = StateMachine()
stateMachine.add(start.run())
stateMachine.add(shoe.run())
stateMachine.add(sewer.run())

while 1:

    stateMachine.nextState()
