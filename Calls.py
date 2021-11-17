import csv
from Elevator import Elevator


class Calls:
    def __init__(self, callID=0) -> None:
        row = []
        f = open("Calls_a.csv")
        csv_reader = csv.reader(f)
        for line in csv_reader:
            row.append(line)
        self.callID = callID
        self.elevator_call = row[callID][0]
        self.time = row[callID][1]
        self.source = row[callID][2]
        self.destination = row[callID][3]
        self.status = row[callID][4]
        self.elevator = row[callID][5]
        self.length = len(row)
        self.r = row
        x = abs(int(self.destination) - int(self.source))
        if x < 0:
            self.direction = -1  # DOWN
        else:
            self.direction = 1  # UP
    #
    # def set_direction(self):
    #     x = abs(int(self.destination) - int(self.source))
    #     if x < 0:
    #         self.direction = -1  # DOWN
    #     else:
    #         self.direction = 1  # UP
