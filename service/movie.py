class MovieService:
    def __init__(self, dao_movie):
        self.dao_movie = dao_movie

    def get_one(self, mid):
        return self.dao_movie.get_one(mid)

    def create(self, movie_data):
        self.dao_movie.create(movie_data)

    def update(self, mid, movie_data):
        movie = self.dao_movie.get_one_update(mid)

        movie.title = movie_data["title"]
        movie.description = movie_data["description"]
        movie.trailer = movie_data["trailer"]
        movie.year = movie_data["year"]
        movie.rating = movie_data["rating"]
        movie.genre_id = movie_data["genre_id"]
        movie.director_id = movie_data["director_id"]

        self.dao_movie.update(movie)

    def partial_update(self, mid, movie_data):
        movie = self.dao_movie.get_one_update(mid)

        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie_data.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie_data.get("trailer")
        if "year" in movie_data:
            movie.year = movie_data.get("year")
        if "rating" in movie_data:
            movie.rating = movie_data.get("rating")
        if "genre_id" in movie_data:
            movie.genre_id = movie_data.get("genre_id")
        if "director_id" in movie_data:
            movie.director_id = movie_data.get("director_id")

        self.dao_movie.update(movie)

    def get_all_by_parameters(self, director_id, genre_id, year_id):
        return self.dao_movie.get_all_by_parameters(director_id, genre_id, year_id)

    def delete_movie(self, mid):
        self.dao_movie.delete(mid)
