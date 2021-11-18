# import io
# import os
# from unittest import TestCase
# import Algo
#
#
# class Test(TestCase):
#     def test_algo(self):
#         os.remove("Test1_out_new.csv")
#         os.remove("Test2_out_new.csv")
#         os.remove("Test3_out_new.csv")
#         Algo.algo("B2.json", "Test1.csv", "Test1_out_new.csv")
#         self.assertListEqual(
#             list(io.open("Test1_out.csv")),
#             list(io.open("Test1_out_new.csv")))
#
#         Algo.algo("B2.json", "Test2.csv", "Test2_out_new.csv")
#         self.assertListEqual(
#             list(io.open("Test1_out.csv")),
#             list(io.open("Test1_out_new.csv")))
#
#         Algo.algo("B2.json", "Test3.csv", "Test3_out_new.csv")
#         self.assertListEqual(
#             list(io.open("Test1_out.csv")),
#             list(io.open("Test1_out_new.csv")))
#
#
#
#
