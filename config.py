import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '\x01"{\xcd\x08\'~\xc9\xdc\x84r\xfa\x02\xads&\xc3\xee\'\x1cG\x98\xd4\x89'
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SLQALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SLQALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
