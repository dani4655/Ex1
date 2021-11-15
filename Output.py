import csv


class output:
    def __init__(self, callID=0) -> None:
        row = []
        f = open("Calls_a.csv")
        csv_writer = csv.writer(f)
        for line in csv_writer:
            row.append(line)
        self.callID = callID
        self.elevator_call = row[callID][0]
        self.time = row[callID][1]
        self.source = row[callID][2]
        self.destination = row[callID][3]
        self.status = row[callID][4]
        self.elevator = row[callID][5]
        self.done = row[callID][6]
        self.dt = row[callID][7]
        self.length = len(csv_writer)

    # def __str__(self) -> str:
    #     return f"Elevator_call: {self.elevator_call} time: {self.time} Source: {self.source} Destination: {self.destination} Status: {self.status} Elevator: {self.elevator}"