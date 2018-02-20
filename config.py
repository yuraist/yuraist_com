import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'as394fda2n'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Commit database changes automatically
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Development configuration class"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration class"""

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # TODO implement message errors to admins


class UnixConfig(ProductionConfig):
    """Unix production configuration class"""
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # Setup logging
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)

config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'unix': UnixConfig,
    'default': DevelopmentConfig
}
