import unittest
from .. import TestGroup

from app.main import db
from app.main.models.user import User

class TestUser(TestGroup):
    
    def test_constructor(self):
        # Arrange
        username = "testuser"
        password = "testpassword"
        
        # Act
        user = User(
            username=username,
            password=password
        )
        
        # Assert
        self.assertEqual(username, user.username)
        self.assertEqual(password, user.password)
        
    def test_repr(self):
        # Arrange
        user = User(
            id=1,
            username="testuser",
            password="testpassword"
        )
        
        # Act
        repr_str = repr(user)
        
        # Assert
        self.assertEqual("User[id=1, username=testuser]", repr_str)