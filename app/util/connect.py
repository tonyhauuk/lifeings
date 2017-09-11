from pymongo import MongoClient

class Conn():
    def connect(self):
        self.client = MongoClient('123.56.71.98:27017')
        db = self.client.lifeings
        db.authenticate('lifeingsAdmin', 'a9270ae592bd52cceb7e7736a434506d')

        return db

    def close(self):
        self.client.close()