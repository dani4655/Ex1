import json


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            dict = json.load(f)
            self._minFloor=int (dict["_minFloor"])
            self._maxFloor=int(dict['_maxFloor'])
            # self._elevators=[](dict['_elevators'])
            self._elevators =[]
            for k in dict['_elevators']:
                self._elevators.append(k)






