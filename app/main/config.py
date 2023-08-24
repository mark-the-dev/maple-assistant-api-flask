import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

"""
flask --app 'app/main:create_app("dev")' run
"""
class DevelopmentConfig(Config):
    ENV_NAME = "dev"

    # SQLAlchemy Config
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_DATABASE = os.getenv("DB_DATABASE")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
    
"""
flask --app 'app/main:create_app("test")' run
"""
class TestingConfig(Config):
    ENV_NAME = "test"
    TESTING = True

    # SQLAlchemy Config
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_DATABASE = os.getenv("DB_DATABASE")
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/TEST_{DB_DATABASE}"

"""
flask --app 'app/main:create_app("prod")' run
"""
class ProductionConfig(Config):
    ENV_NAME = "prod"

    # SQLAlchemy Config
    # DB_HOST = os.getenv("PROD_DB_HOST")
    # DB_USER = os.getenv("PROD_DB_USER")
    # DB_PASSWORD = os.getenv("PROD_DB_PASSWORD")
    # DB_DATABASE = os.getenv("PROD_DB_DATABASE")

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY