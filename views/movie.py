from flask import request
from flask_restx import Namespace, Resource

from implemented import movie_service, movie_schema, movies_schema

movie_ns = Namespace("movies")


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        search_director = request.args.get('director', type=int)
        search_genre = request.args.get('genre', type=int)
        search_year = request.args.get('year', type=int)

        movies = movie_service.get_all_by_parameters(search_director, search_genre, search_year)

        if not movies:
            return '', 204

        return movies_schema.dump(movies), 200

    def post(self):
        movie_data = request.json
        movie_service.create(movie_data)
        return f"Фильм с названием {movie_data.get('title')} добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        if not movie:
            return '', 204

        return movie_schema.dump(movie), 200

    def put(self, mid):
        movie_data = request.json
        movie_service.update(mid, movie_data)
        return '', 204

    def patch(self, mid):
        movie_data = request.json
        movie_service.partial_update(mid, movie_data)
        return '', 204

    def delete(self, mid):
        movie_service.delete_movie(mid)
        return '', 204
