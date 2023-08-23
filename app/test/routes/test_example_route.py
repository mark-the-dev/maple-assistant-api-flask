import unittest
import json
from . import TestAPIResource
from flask import Response

class TestExampleRoute(TestAPIResource):
    
    def test_get_example_status_code_200(self):
        response = self.app.get('/example/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_example_proper_output(self):
        response = self.app.get('/example/')
        
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], 'bar')
    
if __name__ == '__main__':
    unittest.main()