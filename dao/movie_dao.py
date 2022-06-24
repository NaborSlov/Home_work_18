from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_by_parameters(self, director_id, genre_id, year):
        """
        Получение фильма по параметрам
        """
        # начальный запрос получение всех фильмов из таблицы movie
        query = self.session.query(Movie)
        # если есть соответствующий параметр, то добавляем фильтр к запросу
        if director_id:
            query = query.filter(Movie.director_id == director_id)
        if genre_id:
            query = query.filter(Movie.genre_id == genre_id)
        if year:
            query = query.filter(Movie.year == year)
        # возвращаем фильмы
        return query.all()

    def get_one(self, mid):
        """
        Получение фильма по его id
        """
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def create(self, movie_data):
        """
        Добавление нового фильма
        """
        # создание объекта Movie по полученным данным
        movie = Movie(**movie_data)
        # добавление фильма в базу
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        # изменение данных
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        # удаление фильма по его id
        self.session.query(Movie).filter(Movie.id == mid).delete()
        self.session.commit()
