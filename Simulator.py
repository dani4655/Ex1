from Output import Output
from Elevator import Elevator
from Calls import Calls
from Building import Building


class Simulator:
    b = Building("B5.json")

    def time(self, e: b.elevators, list: [], call: Calls):
        if list.size == 0:
            return e._speed * abs(call.source - e.position) + e._openTime + e._closeTime + e._startTime + e._stopTime
        t = e._speed * abs(e.position - list[0]) + e._openTime + e._closeTime + e._startTime + e._stopTime
        if e.direction == 1:
            for i in range(0, list.size - 1):
                t += e._speed * abs(list[i] - list[i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
            if e.temp_call_listUP.size > 0:
                for i in range(0, e.temp_call_listUP - 1):
                    t += e._speed * abs(e.temp_call_listUP[i] - e.temp_call_listUP[
                        i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
        if e.direction == -1:
            for i in range(0, list - 1):
                if list[i] < call.source:
                    break
                t += e._speed * abs(list[i] - list[i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
            if e.temp_call_listDOWN.size > 0:
                for i in range(0, e.temp_call_listDOWN - 1):
                    t += e._speed * abs(e.temp_call_listDOWN[i] - e.temp_call_listDOWN[
                        i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
        return t

    def one_ele(self, c: Calls):
        ele = self.b.elevators[0]
        if ele.direction == 0:  # RESTMODE
            self.add(c, ele)
        if ele.direction == 1:  # UP
            self.add(c, ele)
        if ele.direction == -1:  # DOWN
            self.add(c, ele)

    def add(self, c: Calls, ele: Elevator):
        if ele.direction == 1:  # UP
            self.addUP(c, ele)
        elif ele.direction == -1:  # DOWN
            self.addDOWN(c, ele)
        elif ele.direction == 0:
            if c.direction == 1:
                ele.call_listUP.append(c.source)
                ele.call_listUP.append(c.destination)
                ele.call_listUP.sort()
                ele.calls_l.append(c)
            ele.call_listDOWN.append(c.source)
            ele.call_listDOWN.append(c.destination)
            ele.call_listDOWN.sort(reverse=True)
            ele.calls_l.append(c)

    def addUP(self, c: Calls, ele: Elevator):
        if ele.call_listUP.size > 0 and ele.call_listUP[0]:
            ele.temp_call_listUP.append(c.source)
            ele.temp_call_listUP.append(c.destination)
            ele.temp_call_listUP.sort()
            ele.calls_l.append(c)
        else:
            ele.call_listUP.append(c.source)
            ele.call_listUP.append(c.destination)
            ele.temp_call_listUP.sort()
            ele.calls_l.append(c)

    def addDOWN(self, c: Calls, ele: Elevator):
        if ele.call_listDOWN.size > 0 and ele.call_listDOWN[0]:
            ele.temp_call_listDOWN.append(c.source)
            ele.temp_call_listDOWN.append(c.destination)
            ele.temp_call_listDOWN.sort(reverse=True)
            ele.calls_l.append(c)

        else:
            ele.call_listDOWN.append(c.source)
            ele.call_listDOWN.append(c.destination)
            ele.call_listDOWN.sort(reverse=True)
            ele.calls_l.append(c)

    def pos(self, num: int):
        for i in range(num):
            self.b.elevators[i].set_position()
            self.start_call(self.b.elevators[i])
            self.write_call(self.b.elevators[i])

    def start_call(self, ele: Elevator):
        if len(ele.calls_l) > 0:
            c = ele.calls_l[0]
            if ele.position == c.source:
                c.status = 2


    def write_call(self, ele: Elevator):
        if len(ele.calls_l) > 0:
            c = ele.calls_l[0]
            if c.status == 2 and c.destination == ele.position:
                c.status = 3
                c.elevator = ele.eleid
                Output(c.callID)
                ele.calls_l.remove(0)


    def sim(self):
        numOfEle = len(self.b.elevators)
        calls_time = float(Calls(Calls(0).length - 1).time) + 120
        i = 0
        ans = None
        for t in range(int(calls_time)):  # TIME

            self.pos(numOfEle)  # set elevators position
            for j in Calls:  # Calls
                c = Calls(i)
                if numOfEle == 1:  # 1 Elevator
                    if t >= c.time:
                        self.one_ele(c)
                    else:
                        break
                    j += 1
                    continue
                p = 99999
                for e in range(numOfEle):  # Elevators
                    ele = self.b.elevators[e]
                    if t >= c.time:
                        if ele.direction == 0 and ele.position == c.source:  # elev at the call floor and "rest mode"
                            self.add(c, ele)
                            ele.set_direction()
                            break
                        if ele.direction == 1 and ele.position == c.source:  # elev at the call floor and UP
                            self.add(c, ele)
                            ele.set_direction()
                            break
                        if ele.direction == -1 and ele.position == c.source:  # elev at the call floor and DOWN
                            self.add(c, ele)
                            ele.set_direction()
                            break
                        if ele.direction == 1:  # UP
                            if self.time(ele, ele.call_listUP.append, c) < p:
                                p = self.time(ele, ele.call_listUP.append, c)
                                ans = ele
                        if ele.direction == -1:  # DOWN
                            if self.time(ele, ele.call_listDOWN.append, c) < p:
                                p = self.time(ele, ele.call_listDOWN.append, c)
                                ans = ele
                        if ele.direction == 0:  # REST MODE
                            if self.time(ele, ele.call_listDOWN.append, c) < p:
                                p = self.time(ele, ele.call_listDOWN.append, c)
                                ans = ele
                    if ans != None:
                        self.add(c, ans)
                        ele.set_direction()
                i += 1
