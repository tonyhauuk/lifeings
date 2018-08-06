# -*- coding:utf-8 -*-

from pymongo import MongoClient
from app.key import Key


password = Key.db


class Conn:
    def connect(self):
        self.client = MongoClient('123.56.71.98', 27017)
        db = self.client.lifeings
        db.authenticate('lifeingsAdmin', password)

        return db

    def close(self):
        self.client.close()