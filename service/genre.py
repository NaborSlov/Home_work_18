class GenreService:
    def __init__(self, dao_genre):
        self.dao_genre = dao_genre

    def get_all(self):
        return self.dao_genre.get_all()

    def get_one(self, gid):
        return self.dao_genre.get_one(gid)
