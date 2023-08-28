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
            user = User(username=username, password=hashlib.sha256(password.encode('utf-8')).hexdigest())
            self.db.session.add(user)
            self.db.session.commit()
            
            # Act
            # Assert
            with self.assertRaises(Exception):
                create_new_user(username, password)

    def test_verify_login_success(self):
        with self.app.app_context():
            # Arrange
            username = "test"
            password = "password123"
            user = User(username=username, password=hashlib.sha256(password.encode('utf-8')).hexdigest())
            self.db.session.add(user)
            self.db.session.commit()
            
            # Act
            result = verify_login(username, password)
            
            # Assert
            self.assertEqual(user, result)

    def test_verify_login_unknown_username(self):
        with self.app.app_context():
            # Arrange
            username = "test"
            password = "password123"
            user = User(username=username, password=hashlib.sha256(password.encode('utf-8')).hexdigest())
            self.db.session.add(user)
            self.db.session.commit()
            
            # Act
            result = verify_login("tes", password)
            
            # Assert
            self.assertIsNone(result)

    def test_verify_login_incorrect_password(self):
        with self.app.app_context():
            # Arrange
            username = "test"
            password = "password123"
            user = User(username=username, password=hashlib.sha256(password.encode('utf-8')).hexdigest())
            self.db.session.add(user)
            self.db.session.commit()
            
            # Act
            result = verify_login(username, "password")
            
            # Assert
            self.assertFalse(result)
