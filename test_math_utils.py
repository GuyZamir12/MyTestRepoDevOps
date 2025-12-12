# test_math_utils.py
import unittest
from math_utils import add_numbers, multiply_numbers, divide_numbers

class TestMathUtils(unittest.TestCase):

    # Test 1: Simple addition
    def test_add_numbers(self):
        result = add_numbers(3, 7)
        self.assertEqual(result, 10)

    # Test 2: Simple multiplication
    def test_multiply_numbers(self):
        result = multiply_numbers(5, -2)
        self.assertEqual(result, -10)

    # Test 3: Handling an exception (Edge Case)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()