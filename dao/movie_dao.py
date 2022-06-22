from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def format_movie(self):
        return self.session.query(Movie.id,
                                  Movie.title,
                                  Movie.description,
                                  Movie.trailer,
                                  Movie.year,
                                  Movie.rating,
                                  Genre.name.label('genre_name'),
                                  Director.name.label('director_name'))\
            .join(Genre).join(Director)

    def get_all(self):
        return self.format_movie().all()

    def get_one(self, mid):
        return self.format_movie().get(mid)

    def get_all_director(self, director_id):
        return self.format_movie().filter(Movie.director_id == director_id).all()

    def get_all_genre(self, genre_id):
        return self.format_movie().filter(Movie.genre_id == genre_id).all()

    def get_movies_year(self, year):
        return self.format_movie().filter(Movie.year == year).all()

    def create(self, movie_data):
        movie = Movie(**movie_data)

        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
