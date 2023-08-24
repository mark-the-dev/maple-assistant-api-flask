import unittest
from .. import TestGroup

from main.services.example_service import *
from main.models.example_model import *

class TestExampleService(TestGroup):

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
        
    def test_get_all_examples(self):
        # Arrange
        with self.app.app_context():
            example1 = Example(id=1)
            example2 = Example(id=2)
            self.db.session.add(example1)
            self.db.session.add(example2)
            self.db.session.commit()
        
        # Act
        with self.app.app_context():
            results = get_all_examples()
        
        # Assert
        self.assertEqual(len(results), 2)