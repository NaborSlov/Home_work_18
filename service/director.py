class DirectorService:
    def __init__(self, dao_director):
        self.dao_director = dao_director

    def get_all(self):
        return self.dao_director.get_all()

    def get_one(self, did):
        return self.dao_director.get_one(did)
