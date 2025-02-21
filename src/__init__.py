from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.update(test_config)
    return app
