from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from .config import config_by_name

api = Api()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    api.init_app(app)

    from .routes.example_route import example
    api.add_namespace(example)
    
    return app