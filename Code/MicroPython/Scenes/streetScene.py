from collections import deque
from . import renderStreet
from . import player
import time

playerPosition = [
    [1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0],
]

renderRate = 0
trafficRate = 0
while True:

    renderDelta = time.ticks_diff(time.ticks_ms(), renderRate)
    trafficDelta = time.ticks_diff(time.ticks_ms(), trafficRate)

    # Move traffic
    if (trafficDelta > 800):
        renderStreet.moveTraffic()
        trafficRate = time.ticks_ms()

    player.checkMove(playerPosition)

    # render Led strips
    if (renderDelta > 10):

        renderStreet.renderStreetLeds(playerPosition)
        renderRate = time.ticks_ms()
