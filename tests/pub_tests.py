import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
      self.pub = Pub("The Prancing Pony", 100.00) 

    def test_has_name(self):
        actual = self.pub.get_name()
        expected = "The Prancing Pony"
        self.assertEqual(actual, expected)

    def test_increase_till(self):
      actual = self.pub.increase_till(20.00)
      expected = 121.00
      self.assertEqual(actual, expected)

      
    