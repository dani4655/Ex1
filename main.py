import json
import csv
<<<<<<<<< Temporary merge branch 1
import Calls

from Ex1.Elevator import Elevator

if __name__ == '__main__':
    pass
"""
this function calculate the time it will take to the elevator to go from source floor to dest not including any stops in the way
"""
def time(source: int, dest: int, eleveator: Elevator):
    return (abs(dest - source)) / eleveator._speed + eleveator._openTime + eleveator._closeTime + eleveator._startTime + eleveator._stopTime

=========

import pandas

from Elevator import Elevator
from Building import Building
from Calls import calls

# check call direction (UP or DOWN)
def direction(id: int):
    call = calls(id)
    x = call.destination - call.source
    if x < 0:
        return -1  # DOWN
    return 1  # UP

# check all calls
# UP = 1, DOWN = -1, equals = 0
def up_or_down(call: calls):
    up = 0
    down = 0
    for i in call:
        if direction(call.callID) == 1:
            up += 1
        if direction(call.callID) == -1:
            down += 1
    if up > down:
        return 1
    if down < up:
        return -1
    return 0


if __name__ == '__main__':
    numOfEle = len(Building['_elevators'])
    elevators = [numOfEle]
    for j in calls:
        c = calls(j)
        if numOfEle == 1: #one elevator
            ele = Building['_elevators'][0]
            if direction(0) == 1:
                ele.goto(c)


def timeAll(calls:[]):
    for i in calls:
        calls[i]