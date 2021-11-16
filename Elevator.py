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

    def set_status(self, i: int) -> None:
        self.status = i

    """
     this function gets integer that 
     represent time since the simulator started
     and it calculate where is the elevator 
    :param time
    """
    def set_position(self, time: int) -> None:
        if self.status == 0:
            if time < self._startTime:
                pass
            else:
                t = ((time - self._startTime) * self._speed)
                self.position += t

        if time < self.delay:
            pass
        else:
            t=((time-self.delay)*self._speed)
            t*=self.status
            toInt = int(t)
            self.position += toInt




#
# def add_calls(self, id: int, floor: int, arriving: float):
#     call_dictionary = {"id": id,
#                        "floor": floor,
#                        "arriving": arriving}
#     self.list.append(call_dictionary)
