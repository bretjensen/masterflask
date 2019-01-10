class Config(object):
    POSTS_PER_PAGE = 5


class ProdConfig(Config):
    SECRET_KEY = '\x01"{\xcd\x08\'~\xc9\xdc\x84r\xfa\x02\xads&\xc3\xee\'\x1cG\x98\xd4\x89'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_ECHO = True
    SECRET_KEY = '\xdf\x0b\xaf\xa4\xf6\xa1H\x12\x89a\xf4B\t\xab{_\\\x1e6\x04\x0e\xd4;)'