import json
#from Elevator import Elevator


class Building:
    def __init__(self, file_name):
        with open("B5.json", "r") as f:
            dict = json.load(f)
            self._minFloor = int(dict["_minFloor"])
            self._maxFloor = int(dict['_maxFloor'])
            # self._elevators=[](dict['_elevators'])
            self._elevators = []
            for k in dict['_elevators']:
                self._elevators.append(k)
            # self.list = Elevator.dict_list

    # def add_calls(self, id: int, floor: int, arriving: float):
    #     call_dictionary = {"id": id,
    #                        "floor": floor,
    #                        "arriving": arriving}
    #     self.list.append(call_dictionary)
