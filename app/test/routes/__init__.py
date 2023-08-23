import unittest
from main import create_app

"""
This is a super class for testing any API endpoints
"""

class TestAPIResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test").test_client()