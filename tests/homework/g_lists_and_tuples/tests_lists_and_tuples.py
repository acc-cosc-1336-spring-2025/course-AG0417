import unittest
from src.homework.g_lists_and_tuples.lists import get_highest_list_value, get_lowest_list_value, get_p_distance, get_p_distance_matrix
class Test_Config(unittest.TestCase):
    def test_get_lowest_list_value(self):
        #test that the function get_lowest_list_value returns a valid lowest value
        self.assertEqual(1, get_lowest_list_value([8,10,1,50,20]))
    
    def test_get_highest_list_value(self):
        #test that the function get_highest_list_value returns a valid highest value
        self.assertEqual(50, get_highest_list_value([8,10,1,50,20]))
    def test_get_p_distance(self):
        # test that the get_p_distance function returns a valid p distance
        self.assertEquals(.4, get_p_distance(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C']))
    def test_get_p_distance_matrix(self):
        # test that the get_p_distance_matrix function returns a valid matrix
        lists = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        self.assertEquals(expected, get_p_distance_matrix(lists))
        