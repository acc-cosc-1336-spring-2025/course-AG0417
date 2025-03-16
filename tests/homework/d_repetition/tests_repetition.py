import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers
class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        #test that the function get_factorial returns a valid factorio
        self.assertEqual(24, get_factorial(4))
        self.assertEqual(120, get_factorial(5))
        self.assertEqual(720, get_factorial(6))
    
    def test_sum_odd_numbers(self):
        #test that the function sum_odd_numbers returns a valid sum
        self.assertEqual(25, sum_odd_numbers(9))
        