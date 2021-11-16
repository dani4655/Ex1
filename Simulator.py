from Calls import Calls
from Building import Building

b = Building("B5.json")


def time(e: b.elevators, call: Calls, list: []):
    if list.size == 0:
        return e._speed * abs(call.source - e.position) + e._openTime + e._closeTime + e._startTime + e._stopTime
    t = e._speed * abs(e.position - list[0]) + e._openTime + e._closeTime + e._startTime + e._stopTime
    if e.status == 1:
        for i in range(0, list.size - 1):
            t += e._speed * abs(list[i] - list[i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
        if e.temp_call_listUP.size > 0:
            for i in range(0, e.temp_call_listUP - 1):
                t += e._speed * abs(e.temp_call_listUP[i] - e.temp_call_listUP[
                    i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
    if e.status == -1:
        for i in range(0, list - 1):
            if list[i] < call.source:
                break;
            t += e._speed * abs(list[i] - list[i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
        if e.temp_call_listDOWN.size > 0:
            for i in range(0, e.temp_call_listDOWN - 1):
                t += e._speed * abs(e.temp_call_listDOWN[i] - e.temp_call_listDOWN[
                    i + 1]) + e._openTime + e._closeTime + e._startTime + e._stopTime
    return t;


def one_ele(c: int):
    ele = b.elevators[0]
    if ele.status == 0:  # RESTMODE
        add(c, ele)
    if ele.status == 1:  # UP
        add(c, ele)
    if ele.status == -1:  # DOWN
        add(c, ele)


def add(c: Calls, ele: b.elevators):
    if ele.status == 1:  # UP
        addUP(c, ele)
    elif ele.status == -1:  # DOWN
        addDOWN(c, ele)
    elif ele.status == 0:
        if c.direction == 1:
            ele.call_listUP.append(c.source)
            ele.call_listUP.append(c.destination)
            ele.call_listUP.sort()
        ele.call_listDOWN.append(c.source)
        ele.call_listDOWN.append(c.destination)
        ele.call_listDOWN.sort(reverse=True)


def addUP(c: Calls, ele: b.elevators):
    if ele.call_listUP.size > 0 and ele.call_listUP[0]:
        ele.temp_call_listUP.append(c.source)
        ele.temp_call_listUP.append(c.destination)
        ele.temp_call_listUP.sort()
    else:
        ele.call_listUP.append(c.source)
        ele.call_listUP.append(c.destination)
        ele.temp_call_listUP.sort()


def addDOWN(c: Calls, ele: b.elevators):
    if ele.call_listDOWN.size > 0 and ele.call_listDOWN[0]:
        ele.temp_call_listDOWN.append(c.source)
        ele.temp_call_listDOWN.append(c.destination)
        ele.temp_call_listDOWN.sort(reverse=True)

    else:
        ele.call_listDOWN.append(c.source)
        ele.call_listDOWN.append(c.destination)
        ele.call_listDOWN.sort(reverse=True)


class Simulator:
    numOfEle = len(b.elevators)
    calls_time = float(Calls(Calls(0).length - 1).time) + 120
    i = 0
    ans = None
    for t in range(calls_time):  # TIME
        for j in Calls:  # Calls
            c = Calls(i)
            if numOfEle == 1:  # 1 Elevator
                if t >= c.time:
                    one_ele(c)
                else:
                    break
                j += 1
                continue
            p = 99999
            for e in range(numOfEle):  # Elevators
                ele = b.elevators[e]
                if ele.status == 0 and ele.position == c.source:  # elev at the call floor and "rest mode"
                    add(c, ele)
                    break
                if ele.status == 1 and ele.position == c.source:  # elev at the call floor and UP
                    add(c, ele)
                    break
                if ele.status == -1 and ele.position == c.source:  # elev at the call floor and DOWN
                    add(c, ele)
                    break
                if ele.status == 1:  # UP
                    if time(ele, ele.call_listUP.append, c) < p:
                        p = time(ele, ele.call_listUP.append, c)
                        ans = ele
                if ele.status == -1:  # DOWN
                    if time(ele, ele.call_listDOWN.append, c) < p:
                        p = time(ele, ele.call_listDOWN.append, c)
                        ans = ele
                if ele.status == 0:  # REST MODE
                    if time(ele, ele.call_listDOWN.append, c) < p:
                        p = time(ele, ele.call_listDOWN.append, c)
                        ans = ele
            if ans != None:
                add(c, ans)
            i += 1

