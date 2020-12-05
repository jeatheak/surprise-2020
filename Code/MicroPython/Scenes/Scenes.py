
from Scenes.PathLighting.pathlight import PathLightning
from Utils.stepper import create as stepperCreate
from Scenes.Finish.finish import finishScene
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

stepper = stepperCreate(Pin(p.STEPPER_PIN1, Pin.OUT), Pin(
    p.STEPPER_PIN2, Pin.OUT), Pin(p.STEPPER_PIN3, Pin.OUT), Pin(p.STEPPER_PIN4, Pin.OUT))

print('init Main done')
print('Starting main loop...')

buttons = Buttons(p.UP_ARROW, p.DOWN_ARROW, p.LEFT_ARROW, p.RIGHT_ARROW)
sewer = sewerScene(p.SEWER_SEGMENT_CLK, p.SEWER_SEGMENT_DIO,
                   buttons, mp3, neoSewer, neoFinish)
shoe = shoeScene(neoShoe, p.LEFT_SIDE_BTN,
                 p.RIGHT_SIDE_BTN, mp3)
street = streetScene(neoStreet, mp3, buttons)
start = startup(neoStart, stepper)
finish = finishScene(neoFinish, mp3, stepper)
pathLight = PathLightning(neoSewer, neoFinish)

stateMachine = StateMachine()
stateMachine.add(lambda: start.run())
# stateMachine.add(lambda: shoe.run())
# stateMachine.add(lambda: pathLight.lightPath1())
# stateMachine.add(lambda: street.run())
stateMachine.add(lambda: pathLight.lightPath2())
stateMachine.add(lambda: sewer.run())
stateMachine.add(lambda: pathLight.lightPath3())
# stateMachine.add(lambda: finish.run())

while 1:

    stateMachine.checkState()
