# -*-coding:UTF-8-*-
from app.util.connect import Conn
from app.util.error import getCode

c = Conn()


class Process():
    def insert(self, dates, collection = None):
        if collection == None:
            return getCode(2)
        else:
            coll = self.getCol(collection)
            c.connect()
            coll.insert(dates)
            c.close()


    def delete(self):
        pass

    def update(self):
        pass

    def find(self, dates, collection = None):
        if collection == None:
            return getCode(2)
        else:
            coll = self.getCol(collection)
            c.connect()
            result = coll.find_one(dates)
            c.close()

            return result

    def findByCondition(self, dates, condition, collection = None):
        if collection == None:
            return getCode(2)
        else:
            coll = self.getCol(collection)
            c.connect()
            result = coll.find_one(dates, condition)
            c.close()

            return result


    # Get collection name
    def getCol(self, collection):
        db = c.connect()
        name = db.get_collection(collection)
        c.close()

        return name

    def checkExistUser(self, phone):
        db = c.connect()
        user = db.User
        isExist = user.find_one({'mobile': phone})

        if isExist is None:
            result = 0
        else:
            result = 1

        c.close()

        return result


