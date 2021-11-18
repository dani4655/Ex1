from Building import Building
from Calls import Calls
from Elevator import Elevator
from Output import Output

b = Building("B5.json")
def calls():
    for i in range(Calls(0).length):
        c = Calls(i)
        t = b.elevators[2].time_travel(Calls(2))
        eleid = 0
        index = 0
        el = 0
        for e in b.elevators:  # Elevators
            if b.elevators[el].status == 2:
                continue
            ele_time = e.time_travel(c)
            if e.status == 2:
                ele_time += e.delay
            if ele_time < t:
                t = e.time_travel(c)
                eleid = index
            index = index + 1
            b.elevators[eleid].time_from_call = c.time
            b.elevators[eleid].time_to_finish = float(c.time) + float(ele_time)
            b.elevators[eleid].status = 2
            Output(c.callID, eleid)
            el += 1

def check_ele(i):
    e = 0
    for j in b.elevators:
        if i >= b.elevators[e].time_to_finish:
            b.elevators[e].time_from_call = 0
            b.elevators[e].time_to_finish = 0
            b.elevators[e].status = 0
        e += 1

if __name__ == '__main__':
    calls()

