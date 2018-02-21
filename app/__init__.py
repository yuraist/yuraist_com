from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_pagedown import PageDown


# Initialize instances of libraries
db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    """Initialize an application with defined configuration"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize the app in instances of libraries
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    # Register a main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register an auth blueprint
    from .auth import auth as auth_bluepring
    app.register_blueprint(auth_bluepring, url_prefix='/auth')

    # Register a bot blueprint
    from .bot import bot as bot_blueprint
    app.register_blueprint(bot_blueprint)

    return app
