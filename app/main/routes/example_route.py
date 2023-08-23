from flask_restx import Resource, Namespace
from main.services.example_service import foo

example = Namespace("example")

@example.route('/')
class Example(Resource):
    def get(self):
        data = { 'message': f"{foo()}" }
        return data, 200
    def post(self):
        data = { 'message': f"{foo()}" }
        return data, 200