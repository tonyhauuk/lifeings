with open('../../../../KEY', 'r') as f:
    file = f.read()

class Config(object):
    SECRET_KEY = file

class DevelopmentConfig(Config):
    DEBUG = True


Conf = DevelopmentConfig