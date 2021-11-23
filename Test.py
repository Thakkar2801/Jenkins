#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get average of two numbers
        """
        data = [3, 2]
        result = summation(data)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
