from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config_app: Config):
    applications = Flask(__name__)
    applications.config.from_object(config_app)
    applications.app_context().push()
    return applications


def configure_app(applications: Flask):
    db.init_app(applications)
    api = Api(applications)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    configure_app(app)
    app.run()
