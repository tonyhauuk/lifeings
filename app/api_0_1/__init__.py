# -*-coding:UTF-8-*-

from flask import Blueprint

api = Blueprint('api', __name__)

from app.api_0_1 import view

