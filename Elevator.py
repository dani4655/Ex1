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

    def setstatus(self, i: int) -> None:
        self.status = i

    def setposition(self, i: int) -> None:
        self.position = i

#
# def add_calls(self, id: int, floor: int, arriving: float):
#     call_dictionary = {"id": id,
#                        "floor": floor,
#                        "arriving": arriving}
#     self.list.append(call_dictionary)
