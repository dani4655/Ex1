import json
import csv

import pandas

from Elevator import Elevator
from Building import Building
from Calls import calls


def up_down(id: int):
    call = calls(id)
    x = call.destination - call.source
    if x < 0:
        return -1  # DOWN
    return 1  # UP


def up_or_down(call: calls):
    up = 0
    down = 0
    for i in call:
        if up_down(call.callID) == 1:
            up += 1
        if up_down(call.callID) == -1:
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
        if numOfEle == 1:
            for i in numOfEle:
                if up_or_down(calls) == 1:

