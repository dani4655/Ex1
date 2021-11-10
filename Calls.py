import csv


class calls:
    def __init__(self, elevator_call="", time=0, source=0, destination=0, status=0, elevator=0) -> None:
        self.elevator_call = elevator_call
        self.time = time
        self.source = source
        self.destination = destination
        self.status = status
        self.elevator = elevator

    def __str__(self) -> str:
        return f"Elevator_call: {self.elevator_call} time: {self.time} Source: {self.source} Destination: {self.destination} Status: {self.status} Elevator: {self.elevator}"

    # def __repr__(self) -> str:
    #     return f"Elevator_call: {self.elevator_call} time: {self.time} Source: {self.source} Destination: {self.destination} Status: {self.status} Elevator: {self.elevator}"

