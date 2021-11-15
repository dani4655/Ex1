import csv


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
        self.direction = 0

    def direction(self):
        x = self.destination - self.source
        if x < 0:
            self.direction = -1  # DOWN
        self.direction = 1  # UP

    # def __str__(self) -> str:
    #     return f"Elevator_call: {self.elevator_call} time: {self.time} Source: {self.source} Destination: {self.destination} Status: {self.status} Elevator: {self.elevator}"
