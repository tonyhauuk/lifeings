# -*-coding:UTF-8-*-
__author__ = 'Wang Xiao'

from flask import Flask

from app.config import Conf


def createApp():
    app = Flask(__name__)
    app.config.from_object(Conf)
    app.secret_key = app.config['SECRET_KEY']
    app.debug = app.config['DEBUG']

    from app.api_0_1 import api as api_0_1_blueprint
    app.register_blueprint(api_0_1_blueprint, url_prefix = '/api/v0.1')

    return app


if __name__ == '__main__':
    app = createApp()
    app.run(debug = app.debug, host = '0.0.0.0', port = 5001)
