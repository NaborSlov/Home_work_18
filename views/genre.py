from flask_restx import Namespace, Resource
from implemented import genre_service, genre_schema, genres_schema

genre_ns = Namespace("genres")


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
