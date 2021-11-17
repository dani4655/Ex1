import json
import csv

import pandas as pd

import Calls

# from Elevator import Elevator
import pandas

import Output
from Building import Building
from Calls import Calls


def direction(id: int):
    call = Calls(id)
    x = call.destination - call.source
    if x < 0:
        return -1  # DOWN
    return 1  # UP


# check all calls
# UP = 1, DOWN = -1, equals = 0
def up_or_down(call: Calls):
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


# def time_to_arrive(call: calls, ele: int):
#     elev = Building['_elevators'][ele]
#     e = Building.list[ele]
#     if len(Elevator.list) > 0:
#         elev
#     dist = abs(e['floor'])  #need to get the distance from floor a to floor b
#     a_to_b= elev._closeTime+ elev._openTime + elev._startTime + elev._stopTime +

if __name__ == '__main__':
    # numOfEle = len(Building['_elevators'])
    # elevators = [numOfEle]
    # for j in len(calls.r):
    #     c = calls.r[j]
    #     if numOfEle == 1:  # one elevator
    #         ele = Building['_elevators'][0]
    #         if direction(0) == 1:
    #             ele.goto(c)
    # pd.read_json("B5.json")
    b = Building("B5.json")
    # b.add_calls(0,1,123124)
    # b.add_calls(0, 6, 235623)
    ele = b.elevators[0]
    c = Calls(0)
    numOfEle = len(b.elevators)
    Output.output(6)
