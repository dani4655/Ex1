import json
import csv
import Calls

from Elevator import Elevator
import pandas
from Building import Building
from Calls import calls


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
        if numOfEle == 1:  # one elevator
            ele = Building['_elevators'][0]
            if direction(0) == 1:
                ele.goto(c)

