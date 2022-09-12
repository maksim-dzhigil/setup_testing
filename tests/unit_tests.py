import unittest
import os

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)

    def test_another_something(self):
        self.assertEqual(True, True)

    def test_unpacking_at_ai_ad(self):
        self.name_list = os.listdir('./acdc_for_test')
        self.assertIsNotNone(self.name_list)