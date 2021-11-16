import csv
from Calls import Calls
from Building import Building
from Elevator import Elevator

class output:
    def __init__(self, callID) -> None:
        b = Building("B5.json")
        f = open("Calls_.csv", 'w')
        data = ['Done', 'dt']
        time = 0
        csv_writer = csv.writer(f)
        csv_writer.writerow(Calls(callID).r[callID]+data+time)
        f.close()
