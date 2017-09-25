from pymongo import MongoClient

with open('KEY', 'r') as f:
    file = f.read()

class Conn():
    def connect(self):
        self.client = MongoClient('123.56.71.98:27017')
        db = self.client.lifeings
        db.authenticate('lifeingsAdmin', file)

        return db

    def close(self):
        self.client.close()