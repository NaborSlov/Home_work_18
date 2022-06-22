class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATION = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}