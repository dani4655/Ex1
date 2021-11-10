import json
import csv
from Building import building

if __name__ == '__main__':
    with open('Building.json') as f:
        jfile = json.load(f)
        Building=building(jfile['_minFloor'], jfile['_maxFloor'])

    with open('Calls.csv') as c:
        cfile = csv.