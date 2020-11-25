from Scenes.Street.utils import Utils
from Scenes.Street.renderStreet import RenderStreet
from Scenes.Street.player import Player
from Utils.stateMachine import StateMachine
from Utils.timer import Timer
from Speech.player import Player


class streetScene(object):
    def __init__(self, neopixel, mp3: Player) -> None:
        self.__renderStreet = RenderStreet()
        self.__neo = neopixel
        self.__mp3 = mp3
        self.__state = StateMachine(True)
        self.__speechTimer = Timer(4000)
        self.playerPosition = [
            [1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0],
        ]

        self.__setStates()

    def __setStates(self) -> None:
        stateMachine = self.__state

        stateMachine.add(lambda: self.__GiveSpeech())
        stateMachine.add(lambda: self.__startStreetScene())
        stateMachine.add(lambda: self.__play())
        stateMachine.add(lambda: self.__finish())

    def __play(self) -> bool:
        # Move traffic
        self.__renderStreet.moveTraffic()

        # Perform Player check
        Player.checkMove(self.playerPosition)

        # render Led strips
        self.__renderStreet.renderStreetLeds(self.playerPosition, self.__neo)

        if self.playerPosition[5][0] == 1:
            print('Player has Finished!')
            return True

        return False

    def __finish(self) -> None:
        self.__renderStreet.renderFinish()

        return True

    def run(self):
        self.__state.checkState()

    def __GiveSpeech(self) -> bool:
        if self.__speechTimer.check():
            return True
        return False

    def __startStreetScene(self) -> bool:
        print('Starting StreetScene')
        self.__mp3.PlaySpecificInFolder(3, 1)
        self.__mp3.EnableLoop()

        return True
