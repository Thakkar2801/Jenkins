#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import Avg

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get average of two numbers
        """
        data = [3, 2]
        result = Avg(data)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
