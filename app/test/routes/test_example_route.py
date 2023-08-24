import unittest
from .. import TestGroup

import json
from flask import Response

class TestExampleRoute(TestGroup):
    
    def test_get_example_status_code_200(self):
        response = self.client.get('/example/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_example_proper_output(self):
        response = self.client.get('/example/')
        
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], 'bar')