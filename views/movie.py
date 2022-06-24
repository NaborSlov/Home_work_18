from flask import request
from flask_restx import Namespace, Resource

from implemented import movie_service, movie_schema, movies_schema
# создаем namespace фильмов
movie_ns = Namespace("movies")


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Получаем фильмы по введенным параметрам, если параметров нет выведем все фильмы
        """
        search_director = request.args.get('director', type=int)
        search_genre = request.args.get('genre', type=int)
        search_year = request.args.get('year', type=int)
        # получаем результат
        movies = movie_service.get_all_by_parameters(search_director, search_genre, search_year)
        # если фильмов выводим 204
        if not movies:
            return '', 204
        # сериализация и возврат фильмов
        return movies_schema.dump(movies), 200

    def post(self):
        """
        Добавление нового фильма
        """
        # получим данные для нового фильма
        movie_data = request.json
        # добавляем новый фильм в базу данных
        movie_service.create(movie_data)
        # возвращаем ответ
        return f"Фильм с названием {movie_data.get('title')} добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """
        Получаем фильм по его id
        """
        # получаем фильм по id
        movie = movie_service.get_one(mid)
        # если нет фильма возвращаем 204
        if not movie:
            return '', 204
        # сериализация и возврат фильма
        return movie_schema.dump(movie), 200

    def put(self, mid):
        """
        Изменение данных фильма по id
        """
        # получение данных для изменения
        movie_data = request.json
        # изменение данных фильма
        movie_service.update(mid, movie_data)
        return '', 204

    def patch(self, mid):
        """
        Частичное изменение данных
        """
        movie_data = request.json
        movie_service.partial_update(mid, movie_data)
        return '', 204

    def delete(self, mid):
        """
        Удаление фильма по id
        """
        movie_service.delete_movie(mid)
        return '', 204
