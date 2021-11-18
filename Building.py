import json
from Elevator import Elevator


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            dict = json.load(f)
            self._minFloor = int(dict["_minFloor"])
            self._maxFloor = int(dict['_maxFloor'])
            self.elevators = []
            self.status = int
            for k in dict['_elevators']:
                ele = Elevator(id=k["_id"], speed=k["_speed"], minFloor=k["_minFloor"], maxFloor=k["_maxFloor"],
                               closeTime=k["_closeTime"], openTime=k["_openTime"], startTime=k["_startTime"], stopTime=k["_stopTime"])
                self.elevators.append(ele)
            # self.list = Elevator.dict_list


    def getstatus(self):
        return self.elevators['_status']
    def getspeed(eleid: int):
        return Elevator.Elevator(eleid)['_speed']
    def getminfloor(eleid: int):
        return Elevator.Elevator(eleid)['_minFloor']

    # def add_calls(self, id: int, floor: int, arriving: float):
    #     call_dictionary = {"id": id,
    #                        "floor": floor,
    #                        "arriving": arriving}
    #     self.list.append(call_dictionary)
