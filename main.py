import json
import csv
from Ex1.Building import Elevator

if __name__ == '__main__':
    with open('B5.json') as f:
        jfile = json.load(f)
        elv_d = jfile["_elevators"]
        elevators = []
        for v in elv_d:
            elvTmp = Elevator(_id=jfile['_id'], _speed=jfile['_speed'], _minFloor=jfile['_minFloor'],
                              _maxFloor=jfile['_maxFloor'], _closeTime=jfile['_closeTime'],
                              _openTime=jfile['_openTime'], _startTime=jfile['_startTime'],
                              _stopTime=jfile['_stopTime'])
            elevators.append(elvTmp)

        # build=Building(jfile['_minFloor'], jfile['_maxFloor'])

    # with open('Calls.csv') as c:
    #     cfile = csv.
