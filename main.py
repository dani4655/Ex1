import json
import csv
import Calls

from Ex1.Elevator import Elevator

if __name__ == '__main__':
    pass
"""
this function calculate the time it will take to the elevator to go from source floor to dest not including any stops in the way
"""
def time(source: int, dest: int, eleveator: Elevator):
    return (abs(dest - source)) / eleveator._speed + eleveator._openTime + eleveator._closeTime + eleveator._startTime + eleveator._stopTime


def timeAll(calls:[]):
    for i in calls:
        calls[i]