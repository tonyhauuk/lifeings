# -*-coding:UTF-8-*-

from flask import Flask
from app.util.conf import Conf

def createApp():
    app = Flask(__name__)
    app.config.from_object(Conf)
    app.secret_key = app.config['SECRET_KEY']
    app.debug = app.config['DEBUG']

    return app


if __name__ == '__main__':
    app = createApp()
    app.run(debug = app.debug, host = '0.0.0.0', port = 5001)