from unittest import TestCase

from Building import Building
from Calls import Calls
from Simulator import Simulator

b = Building("B5.json")
c = Calls(27)
c2 = Calls(15)
ele = b.elevators[0]


class Test(TestCase):

    def test_time(self):
        Simulator.add(self, c2, ele)
        print("down: ", ele.call_listDOWN)
        print("up", ele.call_listUP)
        print(ele.direction)
        ele.direction = 1
        t = Simulator.time(self, ele, ele.call_listUP, c)
        print(t)

    def test_one_ele(self):
        self.fail()

    def test_add(self):
        Simulator.add(self, c, ele)
        print(ele.call_listDOWN)
        down = ['0', '-1']
        self.assertEqual(down, ele.call_listDOWN)
        self.assertNotEqual(down, ele.call_listUP)

    def test_simulator(self):
        self.fail()
