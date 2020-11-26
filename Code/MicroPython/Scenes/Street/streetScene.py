from Utils.buttons import Buttons
from Scenes.Street.utils import Utils
from Scenes.Street.renderStreet import RenderStreet
from Scenes.Street.player import Player
from Utils.stateMachine import StateMachine
from Utils.timer import Timer
from Speech.player import Player


class streetScene(object):
    def __init__(self, neopixel, mp3: Player, buttons: Buttons) -> None:
        self.__renderStreet = RenderStreet()
        self.__neo = neopixel
        self.__mp3 = mp3
        self.__done = False
        self.__state = StateMachine(True)
        self.__speechTimer = Timer(4000)
        self.__buttons = buttons
        self.playerPosition = [
            [1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0],
        ]

        self.__setStates()


    def run(self):
        self.__state.checkState()
        if self.__done: return True

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__GiveSpeech())
        stateMachine.add(lambda: self.__startStreetScene())
        stateMachine.add(lambda: self.__play())
        stateMachine.add(lambda: self.__finish())

    def __play(self) -> None:
        # Move traffic
        self.__renderStreet.moveTraffic()

        # Perform Player check
        Player.checkMove(self.playerPosition, self.__buttons)

        # render Led strips
        self.__renderStreet.renderStreetLeds(self.playerPosition, self.__neo)

        if self.playerPosition[5][0] == 1:
            print('Player has Finished!')
            self.__state.nextState()

    def __finish(self) -> None:
        self.__renderStreet.renderFinish()
        self.__done = True
        self.__state.nextState()

    def __GiveSpeech(self) -> None:
        if self.__speechTimer.check():
            self.__state.nextState()

    def __startStreetScene(self) -> None:
        print('Starting StreetScene')
        self.__mp3.PlaySpecificInFolder(3, 1)
        self.__mp3.EnableLoop()
        self.__state.nextState()
