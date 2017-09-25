# -*-coding:UTF-8-*-
from app.util.connect import Conn
from app.util.error import getCode

c = Conn()


class Process():
    def __init__(self, db):
        self.db = db


    def insert(self, data, collection = None):
        if collection != None:
            coll = self.getCol(collection)
            coll.insert(data)
        else:
            return getCode(2)


    def delete(self):
        pass


    def update(self):
        pass


    def setUpdate(self, data, setter, collection = None):
        if collection != None:
            coll = self.getCol(collection)

            results = coll.update(data, {'$set': setter})
            result = results['updatedExisting']

            return result
        else:
            return getCode(2)



    def find(self, data, collection = None):
        if collection != None:
            coll = self.getCol(collection)
            result = coll.find_one(data)

            return result
        else:
            return getCode(2)


    def findByCondition(self, data, condition, collection = None):
        if collection != None:
            coll = self.getCol(collection)
            result = coll.find_one(data, condition)

            return result
        else:
            return getCode(2)


    # Get collection name
    def getCol(self, collection):
        db = self.db
        name = db.get_collection(collection)

        return name


    def checkExistUser(self, phone):
        db = self.db
        user = db.User
        isExist = user.find_one({'mobile': phone})

        if isExist is None:
            result = 0
        else:
            result = 1

        c.close()

        return result


