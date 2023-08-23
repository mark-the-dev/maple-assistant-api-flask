import unittest
from main.services.example_service import *

class TestExampleService(unittest.TestCase):

    def test_foo(self):
        # Arrange
        expected = "bar"

        # Act
        actual = foo()

        # Assert
        self.assertEqual(expected, actual, f"Got '{actual}' instead of '{expected}'")

    def test_fib(self):
        # Arrange
        expected = 3

        # Act
        actual = fib(4)

        # Assert
        self.assertEqual(expected, actual, f"Got '{actual}' instead of '{expected}'")

if __name__ == '__main__':
    unittest.main()