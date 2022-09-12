import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, True)
    def test_another_something(self):
        self.assertEqual(True, True)