import unittest
from my_calculator import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(1, 2), 3)
    def test_negative_with_positive(self):
        self.assertEqual(my_adder(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
