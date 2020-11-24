from time import time_ms, ticks_diff

class Timer(object):
    def __init__(self, delay: int):
        self.Delay = delay
        self.Elapsed = 0
        self._lastRate = 0

    def check(self, delay: int = None) -> int:
        _delay = self.Delay
        if delay != None:
            _delay = delay

        self.Delay = _delay
        if ticks_diff(ticks_ms(), self._lastRate) > _delay:
            self._lastRate = ticks_ms()
            return 1
        
        return 0

    def reset(self):
        self._lastRate = time_ms()

class DoubleTimer(object):
    def __init__(self, delay: int, secondDelay: int):
        self.Delay = delay
        self.SecondDelay = secondDelay
        self.Elapsed = 0
        self._lastRate = 0

    def check(self, delay1: int = None, delay2: int = None) -> int:
        delta = ticks_diff(ticks_ms(), self._lastRate)

        _delay1 = self.Delay
        if delay1 != None:
            _delay1 = delay1

        _delay2 = self.SecondDelay
        if delay2 != None:
            _delay2 = delay2

        
        self.Delay = _delay1
        self.SecondDelay = _delay2
        
        if delta > _delay1 and delta <= _delay2:
            return 1
        elif delta > _delay2:
            self._lastRate = ticks_ms()
            return 2
        
        return 0

    def reset(self):
        self._lastRate = time_ms()