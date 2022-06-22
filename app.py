from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db


def create_app(config_app: Config):
    applications = Flask(__name__)
    applications.config.from_object(config_app)
    applications.app_context().push()
    return applications


def configure_app(applications: Flask):
    db.init_app(applications)
    api = Api(applications)
    api.add_namespace(None)
    api.add_namespace(None)
    api.add_namespace(None)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    configure_app(app)
    app.run()
