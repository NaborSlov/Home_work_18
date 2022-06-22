from dao.movie_dao import MovieDAO
from setup_db import db


movie_dao = MovieDAO(db.session)
