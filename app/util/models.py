# -*-coding:UTF-8-*-
from .connect import Conn
from .error import StatusCode

c = Conn()
code = StatusCode()

class Process():
    def __init__(self, data):
        self.data = data

    def checkExistUser(self):
        db = c.connect()
        user = db.User
        isExist = user.find_one({'mobile': self.data})

        if isExist is None:
            result = 0
        else:
            result = 1

        c.close()

        return result

    def insert(self, collection = None):
        if collection == None:
            return code.getCode(2)
        else:
            sql = self.data
            coll = self.getCol(collection)
            c.connect()
            coll.insert(sql)
            c.close()


    def delete(self):
        pass

    def update(self):
        pass

    def find(self):
        pass

    # Get collection name
    def getCol(self, collection):
        db = c.connect()
        name = db.get_collection(collection)
        c.close()

        return name

