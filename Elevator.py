import Building
import json


class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime,stopTime):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._speed = speed
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime
        self.status = 0  # UP = 1, Down = -1, RestMode = 0

    def setstatus(self,i:int)->int:
        self.status = i
        return self.status

#
# def add_calls(self, id: int, floor: int, arriving: float):
#     call_dictionary = {"id": id,
#                        "floor": floor,
#                        "arriving": arriving}
#     self.list.append(call_dictionary)
