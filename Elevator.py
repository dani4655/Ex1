import Building
import json


class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._speed = speed
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self.status = 0  # UP = 1, Down = -1, RestMode = 0
        self.position = 0
        self.call_listUP = []
        self.call_listDOWN = []
        self.temp_call_listUP = []
        self.temp_call_listDOWN = []
        self.delay = self._stopTime + self._startTime + self._openTime + self._closeTime
        self.goto = 0

    def set_status(self, i: int) -> None:
        self.status = i

    """
     this function gets integer that 
     represent time since the simulator started
     and it calculate where is the elevator 
    :param time
    """

    def set_position(self) -> None:
        if self.status == 0:
            if self.goto < self._startTime:
                pass
            else:
                t = ((self.goto - self._startTime) * self._speed)
                self.position += t

        if self.goto < self.delay:
            pass
        else:
            t = ((self.goto - self.delay) * self._speed)
            t *= self.status
            toInt = int(t)
            self.position += toInt
        if self.position > self._maxFloor:
            self.position = self._maxFloor
        if self.position < self._minFloor:
            self.position = self._minFloor
        self.goto += 1

    def direction(self):
        if self.status == 1:
            if len(self.call_listUP) == 0:
                self.status = 0
        if self.status == -1:
            if len(self.call_listDOWN) == 0:
                self.status = 0
        if self.status == 0:
            if len(self.call_listUP) > 0:
                self.status = 1
            elif len(self.call_listDOWN) > 0:
                self.status = -1

#
# def add_calls(self, id: int, floor: int, arriving: float):
#     call_dictionary = {"id": id,
#                        "floor": floor,
#                        "arriving": arriving}
#     self.list.append(call_dictionary)
