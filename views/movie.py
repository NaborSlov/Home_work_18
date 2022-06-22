from flask_restx import Namespace, Resource

movie_ns = Namespace("movies")


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return ['get'], 200

    def post(self):
        return ['post'], 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return ['get_1'], 200

    def put(self, mid):
        return ['put'], 200

    def delete(self, mid):
        return ['del'], 200
