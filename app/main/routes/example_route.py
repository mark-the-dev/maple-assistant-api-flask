from flask_restx import Resource, Namespace
from main.services.example_service import foo

example = Namespace("api")

@example.route('/example')
class Example(Resource):
    def get(self):
        return { 'message': foo() }
    def post(self):
        return { 'message': foo() }