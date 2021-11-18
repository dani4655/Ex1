from Calls import Calls


class Elevator:
    time = 0

    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.eleid = id
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._speed = speed
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self.delay = self._stopTime + self._startTime + self._openTime + self._closeTime
        self.elecalls = 0


    def time_travel(self, c: Calls):
        df = abs(int(c.destination) - int(c.source))
        return self.delay + df / self._speed

