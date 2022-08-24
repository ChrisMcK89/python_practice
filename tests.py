import unittest
from composition import *

class TestComposition(unittest.TestCase):

    def test_monthly_income(self):
        employee1 = Employee(2500, 500)
        actual = employee1.get_total()
        expected = 30500
        self.assertEqual(actual, expected)


