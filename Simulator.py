from Calls import Calls


class Simulator:
    time = float(Calls(Calls(0).length - 1).time) + 120
    for t in range(time):
        c = Calls(t)
        if c >= c.time:
