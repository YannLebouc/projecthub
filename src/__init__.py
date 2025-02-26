import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import config_dict
from src.controllers.user_controller import user_bp
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()


def create_app():
    """Flask application factory"""
    app = Flask(__name__)

    # Load config based on environment
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_dict[env])

    # Initialize database
    db.init_app(app)

    # Initialize blueprints
    app.register_blueprint(user_bp, url_prefix="/users")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
