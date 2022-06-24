from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    director_movies = db.relationship('Movie', back_populates='director', foreign_keys='Movie.director_id')
