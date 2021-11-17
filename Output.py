import csv

from Calls import Calls
from Building import Building
from Elevator import Elevator

class Output:
    def __init__(self, callID) -> None:
        b = Building("B5.json")
        f = open("Calls_.csv", 'a', newline='')
        data = ['Done', 'dt']
        time = 0
        csv_writer = csv.writer(f)
        csv_writer.writerow(Calls(callID).r[callID])
        f.close()
        # with open("Calls_.csv") as myFile:
        #     lines = myFile.readlines()
        #     last_line = lines[len(lines) - 1]
        #     lines[len(lines) - 1] = last_line.rstrip()
        # with open("Calls_.csv", 'w') as myFile:
        #     myFile.writelines(lines)
