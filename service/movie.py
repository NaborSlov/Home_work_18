from marshmallow.fields import Int

from dao.model.shemas import MovieSchema


class MovieService:
    def __init__(self, dao_movie, dao_director, dao_genre):
        self.dao_movie = dao_movie
        self.dao_directory = dao_director
        self.dao_genre = dao_genre

    def get_all(self):
        self.dao_movie.get_all()

    def get_one(self, mid):
        movie = self.dao_movie.get_one(mid)
        return MovieSchema().dump(movie)



