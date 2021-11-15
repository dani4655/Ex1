from Calls import Calls
from Building import Building
import Elevator

def time(e:Elevator, call:Calls, list:[] ):
    if list.size ==0:
        return e._speed * abs(call.source-e.position) + e._openTime +e._closeTime + e._startTime+ e._stopTime
    t= e._speed * abs(e.position-list[0])+ e._openTime + e._closeTime + e._startTime+ e._stopTime
    if e.status==1:
        for i in range(0,list.size-1):
            t+= e._speed* abs(list[i]-list[i+1]) +e._openTime + e._closeTime + e._startTime+ e._stopTime
        if e.temp_call_listUP.size >0 :
            for i in range(0, e.temp_call_listUP-1):
                t+= e._speed*abs(e.temp_call_listUP [i]-e.temp_call_listUP[i+1])+e._openTime + e._closeTime + e._startTime+ e._stopTime
    if e.status==-1:
        for i in range(0, list-1):
            if list[i]<call.source:
                break;
            t+= e._speed* abs(list[i]-list[i+1])+e._openTime + e._closeTime + e._startTime+ e._stopTime
        if e.temp_call_listDOWN.size>0:
            for i in range(0,e.temp_call_listDOWN-1):
                t+= e._speed* abs(e.temp_call_listDOWN[i]-e.temp_call_listDOWN[i+1])+e._openTime + e._closeTime + e._startTime+ e._stopTime
    return t;




class Simulator:
    time = float(Calls(Calls(0).length - 1).time) + 120
    i = 0
    # for t in range(time):
    #     for j in Calls:
    #         c = Calls(i)
    #         for e in Building['_elevators']:
    #             numOfEle = len(Building['_elevators'])
    #             ele = Building['_elevators'][0]
    #             if numOfEle == 1:
    #                 if c >= c.time:
    #                     if ele
    #
    #         i++