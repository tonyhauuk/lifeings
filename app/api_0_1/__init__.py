# -*-coding:UTF-8-*-

from flask import Blueprint

api = Blueprint('api', __name__)

from . import view
from ..util import error