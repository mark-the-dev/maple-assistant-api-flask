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
    from .models.user import User
    from .models.character import Character, Class, load_classes
    
    with app.app_context():
        db.create_all()
        
        if Class.query.count() == 0:
            load_classes()
    
    # Establish Endpoint Connections    
    from .routes.auth_routes import auth
    api.add_namespace(auth)
    
    from .routes.character_routes import character
    api.add_namespace(character)
    
    return app