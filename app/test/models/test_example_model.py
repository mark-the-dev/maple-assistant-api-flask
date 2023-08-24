import unittest
from .. import TestGroup

from app.main import db
from app.main.models.example_model import Example

class TestExampleModel(TestGroup):

    def test_id_field(self):
        with self.app.app_context():
            example = Example()
            self.assertEqual(example.id, None)
            
            self.db.session.add(example)
            self.db.session.commit()
            self.assertIsInstance(example.id, int)
            
if __name__ == '__main__':
    unittest.main()
