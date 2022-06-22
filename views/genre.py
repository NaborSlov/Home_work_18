from flask_restx import Namespace, Resource

genre_ns = Namespace("genres")


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return ['get'], 200


@genre_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        return ['get_1'], 200
