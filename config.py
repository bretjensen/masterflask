class Config:
    pass


class ProdConfig:
    pass


class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
