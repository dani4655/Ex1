import io
import os
from unittest import TestCase
import Algo


class Test(TestCase):
    def test_algo(self):
        os.remove("Test1_out_new.csv")
        os.remove("Test2_out_new.csv")
        os.remove("Test3_out_new.csv")
        Algo.building_file_name = "B2.json"
        Algo.calls_file_name = "Test1.csv"
        Algo.output_file_name = "Test1_out_new.csv"

        self.assertListEqual(
            list(io.open("Test1_out.csv")),
            list(io.open("Test1_out_new.csv")))

        Algo.building_file_name = "B2.json"
        Algo.calls_file_name = "Test2.csv"
        Algo.output_file_name = "Test2_out_new.csv"
        self.assertListEqual(
            list(io.open("Test1_out.csv")),
            list(io.open("Test1_out_new.csv")))

        Algo.building_file_name = "B2.json"
        Algo.calls_file_name = "Test3.csv"
        Algo.output_file_name = "Test3_out_new.csv"
        self.assertListEqual(
            list(io.open("Test1_out.csv")),
            list(io.open("Test1_out_new.csv")))




