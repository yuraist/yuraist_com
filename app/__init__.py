from flask import Flask
from config import config

def create_app(config_name):
    """Initialize an application with defined configuration"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Register a main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register a bot blueprint
    from .bot import bot as bot_blueprint
    app.register_blueprint(bot_blueprint)

    return app
