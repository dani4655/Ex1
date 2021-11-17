from unittest import TestCase

from Building import Building
from Calls import Calls
from Simulator import Simulator

b = Building("B5.json")
c = Calls(0)
ele = b.elevators[0]


class Test(TestCase):

    def test_time(self):
        self.fail()

    def test_one_ele(self):
        self.fail()

    def test_add(self):
        Simulator.add(self,c,ele)

    def test_add_up(self):
        self.fail()

    def test_add_down(self):
        self.fail()

    def test_simulator(self):
        self.fail()
