from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_by_parameters(self, director_id, genre_id, year):
        query = self.session.query(Movie)

        if director_id:
            query = query.filter(Movie.director_id == director_id)

        if genre_id:
            query = query.filter(Movie.genre_id == genre_id)

        if year:
            query = query.filter(Movie.year == year)

        return query.all()

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def get_one_update(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, movie_data):
        movie = Movie(**movie_data)

        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        self.session.query(Movie).filter(Movie.id == mid).delete()
        self.session.commit()
