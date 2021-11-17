import Building
import json


class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.eleid = id
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._speed = speed
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self.status = 0  # unpicked = 1, PickUp = 2, Done = 3
        self.position = 0
        self.direction = 0  # UP = 1, Down = -1, RestMode = 0
        self.call_listUP = []
        self.call_listDOWN = []
        self.temp_call_listUP = []
        self.temp_call_listDOWN = []
        self.calls_l = []
        self.delay = self._stopTime + self._startTime + self._openTime + self._closeTime
        self.goto = 0  # counts the seconds since the elevator started to move

    def set_direction(self, i: int) -> None:
        self.direction = i

    """
     this function gets integer that 
     represent time since the simulator started
     and it calculate where is the elevator 
    :param time
    """

    def set_position(self) -> None:
        if self.direction() == 1 or self.direction() == -1:
            if self.direction == 0:
                if self.goto < self._startTime:
                    pass
                else:
                    t = ((self.goto - self._startTime) * self._speed)
                    self.position += t

            if self.goto < self.delay:
                pass
            else:
                t = ((self.goto - self.delay) * self._speed)
                t *= self.direction
                toInt = int(t)
                self.position += toInt
            if self.position > self._maxFloor:
                self.position = self._maxFloor
            if self.position < self._minFloor:
                self.position = self._minFloor
            self.goto += 1

    def set_direction(self):
        if self.direction == 1:
            if len(self.call_listUP) == 0:
                self.direction = 0
        if self.direction == -1:
            if len(self.call_listDOWN) == 0:
                self.direction = 0
        if self.direction == 0:
            if len(self.call_listUP) > 0:
                self.direction = 1
            elif len(self.call_listDOWN) > 0:
                self.direction = -1

#
# def add_calls(self, id: int, floor: int, arriving: float):
#     call_dictionary = {"id": id,
#                        "floor": floor,
#                        "arriving": arriving}
#     self.list.append(call_dictionary)
