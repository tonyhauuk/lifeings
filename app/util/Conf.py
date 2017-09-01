class Config(object):
    SECRET_KEY = ''

class DevelopmentConfig(Config):
    DEBUG = True


Conf = DevelopmentConfig