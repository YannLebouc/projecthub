import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development environment"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")

class TestingConfig(Config):
    """Testing environment"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(Config):
    """Production environment"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SESSION_COOKIE_SECURE = True

# Configuration dictionary
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
