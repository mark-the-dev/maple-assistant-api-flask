from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from .config import config_by_name

# Create extensions
api = Api()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    
    # Configure the application based on <config_name>
    app.config.from_object(config_by_name[config_name])
    
    # Initialize app with extensions
    db.init_app(app)
    api.init_app(app)
    
    # Establish Database Tables
    from .models.example_model import Example
    
    with app.app_context():
        db.create_all()
    
    # Establish Endpoint Connections
    from .routes.example_route import example
    api.add_namespace(example)
    
    return app