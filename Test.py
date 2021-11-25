#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import SS

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to get sum square of two numbers
        """
        data = [3, 2]
        result = Avg(data)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
