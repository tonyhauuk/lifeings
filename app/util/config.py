from app.key import Key

key = Key.flask
password = Key.db

class Config(object):
    SECRET_KEY = key

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_ADDR = '123.56.71.98'
    MONGODB_PORT = 27017
    PASSWORD = password


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_ADDR = None
    MONGODB_PORT = None
    PASSWORD = password


Conf = DevelopmentConfig