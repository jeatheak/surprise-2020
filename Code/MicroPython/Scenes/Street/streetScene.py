from .Street import renderStreet
from .Street import player
import time

playerPosition = [
    [1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0],
]


def streetScene(neopixel, state):

    # Move traffic
    if state == 3:
        renderStreet.moveTraffic()

    # Perform Player check
    if state == 3:
        player.checkMove(playerPosition)

    # render Led strips
    renderStreet.renderStreetLeds(playerPosition, neopixel, state)
    time.sleep(0.01)

    return state
