# test_divisible.py
import unittest

from divisible import divisible_by


class DivisibleTestCase(unittest.TestCase):

    def test_divisible(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertFalse(divisible_by(10, 3))


if __name__ == "__main__":
    unittest.main()
