import unittest
import os


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_another_something(self):
        self.assertEqual(5, 5)
