from Output import Output
from Elevator import Elevator
from Calls import Calls
from Building import Building

b = Building("B5.json")


def time(e: b.elevators, list: [], call: Calls):
    if len(list) == 0:  # if no calls
        return abs(int(call.source) - int(e.position)) + e.delay
    t = 0
    if e.direction == 1:  # if elevator on the move - UP
        for i in range(len(list) - 1):  # main list
            if list[i + 1] < call.source:
                t += abs(int(list[i]) - int(list[i + 1])) / e._speed + e.delay
            if list[i + 1] > call.source:
                t += abs(int(list[i]) - int(call.source)) / e._speed + e.delay
        if len(e.temp_call_listUP) > 0:  # check temp list
            for i in range(len(e.temp_call_listUP) - 1):
                t += abs(int(e.temp_call_listUP[i]) - int(e.temp_call_listUP[
                                                              i + 1])) / e._speed + e.delay
    if e.direction == -1:  # if elevator on the move - DOWN
        for i in range(len(list) - 1):  # main list
            if list[i + 1] > call.source:
                t += abs(list[i] - list[i + 1]) / e._speed + e.delay
            if list[i + 1] < call.source:
                t += abs(int(list[i]) - int(call.source)) / e._speed + e.delay
        if len(e.temp_call_listDOWN) > 0:
            for i in range(len(e.temp_call_listDOWN) - 1):  # check temp list
                t += abs(int(e.temp_call_listDOWN[i]) - int(e.temp_call_listDOWN[
                                                                i + 1])) / e._speed + e.delay
    return t


def one_ele(c: Calls):
    ele = b.elevators[0]
    if ele.direction == 0:  # RESTMODE
        add(c, ele)
    if ele.direction == 1:  # UP
        add(c, ele)
    if ele.direction == -1:  # DOWN
        add(c, ele)


def add(c: Calls, ele: Elevator):
    if ele.direction == 1:  # UP
        addUP(c, ele)
    elif ele.direction == -1:  # DOWN
        addDOWN(c, ele)
    elif ele.direction == 0:
        if c.direction == 1:
            ele.call_listUP.append(c.source)
            ele.call_listUP.append(c.destination)
            ele.call_listUP.sort()
            ele.calls_l.append(c)
        else:
            ele.call_listDOWN.append(c.source)
            ele.call_listDOWN.append(c.destination)
            ele.call_listDOWN.sort()
            ele.call_listDOWN.reverse()
            ele.calls_l.append(c)


def addUP(c: Calls, ele: Elevator):
    if len(ele.call_listUP) > 0 and ele.call_listUP[0]:
        ele.temp_call_listUP.append(c.source)
        ele.temp_call_listUP.append(c.destination)
        ele.temp_call_listUP.sort()
        ele.calls_l.append(c)
    else:
        ele.call_listUP.append(c.source)
        ele.call_listUP.append(c.destination)
        ele.call_listUP.sort()
        ele.calls_l.append(c)


def addDOWN(c: Calls, ele: Elevator):
    if len(ele.call_listDOWN) > 0 and ele.call_listDOWN[0]:
        ele.temp_call_listDOWN.append(c.source)
        ele.temp_call_listDOWN.append(c.destination)
        ele.temp_call_listDOWN.sort()
        ele.temp_call_listDOWN.reverse()
        ele.calls_l.append(c)

    else:
        ele.call_listDOWN.append(c.source)
        ele.call_listDOWN.append(c.destination)
        ele.call_listDOWN.sort()
        ele.call_listDOWN.reverse()
        ele.calls_l.append(c)


def arr_move_up(ele: Elevator):
    while ele.temp_call_listUP != 0:
        ele.call_listUP.append(ele.temp_call_listUP[0])
        ele.temp_call_listUP.remove(0)
    ele.call_listUP.sort()


def arr_move_down(ele: Elevator):
    while ele.temp_call_listDOWN != 0:
        ele.call_listDOWN.append(ele.temp_call_listDOWN[0])
        ele.temp_call_listDOWN.remove(0)
    ele.call_listDOWN.sort()
    ele.call_listDOWN.reverse()


def pos(num: int):
    for i in range(num):
        ele = b.elevators[i]
        if len(ele.call_listDOWN) == 0 and len(ele.temp_call_listDOWN) > 0:
            arr_move_down(ele)
        if len(ele.call_listUP) == 0 and len(ele.temp_call_listUP) > 0:
            arr_move_up(ele)
        ele.set_position()
        start_call(ele)
        write_call(ele)


def start_call(ele: Elevator):
    if len(ele.calls_l) > 0:
        c = ele.calls_l[0]
        if int(ele.position) == int(c.source):
            c.status = 2


def write_call(ele: Elevator):
    if len(ele.calls_l) > 0:
        c = ele.calls_l[0]
        if int(c.status) == 2 and int(c.destination) == int(ele.position):
            c.status = 3
            c.elevator = ele.eleid
            Output(c.callID)
            ele.calls_l.remove(0)


def sim():
    numOfEle = len(b.elevators)
    calls_time = 200
    i = 0
    ans = None
    for t in range(int(calls_time)):  # TIME

        pos(numOfEle)  # set elevators position
        for j in range(Calls(0).length):  # Calls
            c = Calls(j)
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
                if t < float(c.time):
                    break
                if t >= float(c.time):
                    if int(ele.direction) == 0 and int(ele.position) == int(c.source):  # elev at the call floor and "rest mode"
                        add(c, ele)
                        ele.set_direction()
                        break
                    if int(ele.direction) == 1 and int(ele.position) == int(c.source):  # elev at the call floor and UP
                        add(c, ele)
                        ele.set_direction()
                        break
                    if int(ele.direction) == -1 and int(ele.position) == int(c.source):  # elev at the call floor and DOWN
                        add(c, ele)
                        ele.set_direction()
                        break
                    if int(ele.direction) == 1:  # UP
                        if time(ele, ele.call_listUP, c) < p:
                            p = time(ele, ele.call_listUP, c)
                            ans = ele
                    if int(ele.direction) == -1:  # DOWN
                        if time(ele, ele.call_listDOWN, c) < p:
                            p = time(ele, ele.call_listDOWN, c)
                            ans = ele
                    if int(ele.direction) == 0:  # REST MODE
                        if time(ele, ele.call_listDOWN, c) < p:
                            p = time(ele, ele.call_listDOWN, c)
                            ans = ele
                if ans != None:
                    add(c, ans)
                    ele.set_direction()
            i += 1


if __name__ == '__main__':
    sim()
    # for i in range(len(b.elevators)):
    #     ele = b.elevators[i]
    #     c = ele.calls_l[0]
    #     c.status = 3
    #     c.elevator = ele.eleid
    #     Output(c.callID)
        # ele.calls_l.remove(0)
    # ele = b.elevators[0]
    # ele.calls_l.append(Calls(0))
    # ele.calls_l.append(Calls(2))
    # start_call(ele)
    # ele.position = -1
    # write_call(ele)
