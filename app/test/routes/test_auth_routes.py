import unittest
from .. import TestGroup

import json
from flask import Response

from app.main.models.user import User
import hashlib

REGISTER_ROUTE = '/auth/register'

class TestAuthRoutes(TestGroup):
    
    # =-=-=-=-=-= /auth/register
    def test_post_register_200(self):
        # Arrange 
        id = 1
        username = "test_user"
        password = "test_pass"
        expected_user = "User[id=1, username=test_user]"
        
        # Act
        response = self.client.post(REGISTER_ROUTE, data={
            "id": id,
            "username": username,
            "password": password
        })
        
        # Assert
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_user, response.json['user'])
        
    def test_post_register_409(self):
        # Arrange
        username = "duplicate_user"
        password = "test_pass"
        
        with self.app.app_context():
            user = User(
                username=username,
                password=hashlib.sha256(password.encode('utf-8')).hexdigest()
            )
            self.db.session.add(user)
            self.db.session.commit()
            
        # Act
        response = self.client.post(REGISTER_ROUTE, data={
            "username": username,
            "password": password
        })
        
        # Assert
        self.assertEqual(409, response.status_code)
        
    def test_post_register_400_missing_username(self):
        # Arrange
        body = {
            "password": "123"
        }
        
        # Act
        response = self.client.post(REGISTER_ROUTE, data=body)
        
        # Assert
        self.assertEqual(400, response.status_code)
        self.assertTrue('username' in response.json['errors'])
        
    def test_post_register_400_missing_password(self):
        # Arrange
        body = {
            "username": "123"
        }
        
        # Act
        response = self.client.post(REGISTER_ROUTE, data=body)
        
        # Assert
        self.assertEqual(400, response.status_code)
        self.assertTrue('password' in response.json['errors'])

    # =-=-=-=-=-= /auth/login