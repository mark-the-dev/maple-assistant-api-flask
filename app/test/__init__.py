import os
import sys

import unittest
from main import create_app, db

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.db = db
        
    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()