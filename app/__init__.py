from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    from . import models # noqa
    Migrate(app, db)


def register_blueprints(app):
    from app.api import api
    app.register_blueprint(api, url_prefix='/')
