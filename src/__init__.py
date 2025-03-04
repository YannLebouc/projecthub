import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config import config_dict
from src.controllers.user_controller import user_bp
from dotenv import load_dotenv
from src.models import base

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy(model_class=base.Base)
migrate = Migrate()


def create_app():
    """Flask application factory"""
    app = Flask(__name__)

    # Load config based on environment
    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_dict[env])

    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)
    # Initialize blueprints
    app.register_blueprint(user_bp, url_prefix="/users")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
