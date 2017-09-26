class Config(object):
    SECRET_KEY = 'ZYXWVUTSRQPONMLKJIHGFEDCBA1234567890'


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_ADDR = '123.56.71.98:27017'
    PASSWORD = 'a9270ae592bd52cceb7e7736a434506d'


class ProductionConfig(Config):
    DEBUG = False
    MONGODB_ADDR = None
    PASSWORD = 'a9270ae592bd52cceb7e7736a434506d'


Conf = DevelopmentConfig