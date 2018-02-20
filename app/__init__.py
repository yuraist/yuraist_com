from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Initialize instances of libraries
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    """Initialize an application with defined configuration"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize the app in instances of libraries
    db.init_app(app)
    bootstrap.init_app(app)

    # Register a main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register a bot blueprint
    from .bot import bot as bot_blueprint
    app.register_blueprint(bot_blueprint)

    return app
