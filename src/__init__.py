import os
from flask import Flask
from src.config import config_dict
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Flask application factory"""
    app = Flask(__name__)

    # Load config based on environment variable (default: development)
    # env = os.getenv("FLASK_ENV", "development")
    #app.config.from_object(config_dict[env])

    # Initialize extensions (e.g., SQLAlchemy)
    #db.init_app(app)

    return app
