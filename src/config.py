import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration with common settings."""
    SECRET_KEY = os.environ.get("SECRET_KEY", os.getenv("MY_KEY"))
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://user:pass@localhost/dbname")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600  # 1 hour

class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Logs SQL queries

class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory DB for tests

class ProductionConfig(Config):
    """Configuration for production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://user:pass@localhost/dbname")
    SESSION_COOKIE_SECURE = True  # Secure cookies for production
    REMEMBER_COOKIE_DURATION = 86400  # 1 day

# Dictionary to map configurations
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
