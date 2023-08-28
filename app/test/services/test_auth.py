from .. import TestGroup

from main.services.auth import *
from main.models.user import User

import hashlib

class TestAuth(TestGroup):
    
    def test_create_user_success(self):
        with self.app.app_context():
            # Arrange
            username = "test"
            password = "123"
            password_hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            
            # Act
            user = create_new_user(username, password)
            
            # Assert
            self.assertEqual(username, user.username)
            self.assertEqual(password_hashed, user.password)
        
    def test_create_user_duplicate_username(self):
        with self.app.app_context():
            # Arrange
            username = "test"
            password = "123"
            
            user = create_new_user(username, password)
            
            # Act
            # Assert
            with self.assertRaises(Exception):
                create_new_user(username, password)