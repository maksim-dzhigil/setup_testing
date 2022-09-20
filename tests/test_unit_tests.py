import unittest

from project.utils.utils import *
from project.program import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_another_something(self):
        self.assertEqual(5, 5)

    def test_sum_func(self):
        a = 5
        b = 50
        self.assertEqual(sum_(a, b), a + b)

    def test_make_string_func(self):
        str1 = "ffff"
        str2 = "dgdfg"
        self.assertEqual(make_string(str1, str2), str1 + str2)
