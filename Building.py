import json


class Building:
    def __init__(self, min_floor: int, max_floor: int, elevators:Elevator):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevetors = []


class Elevator:
    def __init__(self, _id: int, _speed: float, _minFloor: int, _maxFloor: int, _closeTime: float, _openTime: float,
                 _startTime: float, _stopTime: float):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
