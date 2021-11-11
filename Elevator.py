import Building
import json

class Elevator:
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            dict = json.load(f)
            self._minFloor = int(dict['_minFloor'])
            self._maxFloor = int(dict['_maxFloor'])
            self._speed=float(dict['_speed'])
            self._closeTime = float(dict['_closeTime'])
            self._openTime = float(dict['_openTime'])
            self._startTime = float(dict['_startTime'])
            self._stopTime = float(dict['_stopTime'])
