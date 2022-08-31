import base64


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = base64.b64decode('salt')
    PWD_HASH_ITERATIONS = 1000
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 1320
    SECRET_KEY = 'jkasdhuiwq&*^&*11356454'
    ALGORITHM = 'sha256'

