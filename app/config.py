# -*- coding:utf-8 -*-

from app.key import Key

key = Key.flask
password = Key.db


class Config():
    SECRET_KEY = key

    @staticmethod
    def init_app(app):
        pass


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

class UnixConfig(ProductionConfig):
    @classmethod
    def initApp(cls, app):
        ProductionConfig.init_app(app)

        # Write system log
        import logging as LOG
        from logging.handlers import SysLogHandler
        handler = SysLogHandler()
        handler.setLevel(LOG.WARNING)
        app.logger.addHandler(handler)

        LOG.basicConfig(level = LOG.INFO,
                        format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt = '%a, %d %b %Y %H:%M:%S',
                        filename = './test.log',
                        filemode = 'w')


Conf = DevelopmentConfig
