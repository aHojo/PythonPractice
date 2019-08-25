import unittest


def multiply(x, y):
    # return x * y
    return x + y

# Usually test live in a test file or module not inline


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50")


# if __name__ == "__main__":
#     unittest.main()

# Or in the terminal python -m unittest multiply.py -v
