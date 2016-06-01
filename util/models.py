#! /user/bin/python
# -*-coding:UTF-8-*-

from pymongo import MongoClient

# from passlib.apps import custom_app_context as pwd_context

class Conn():
    def retDB(self):
        connection = MongoClient()
        connection.lifeings.authenticate('lifeings_admin', '2caa6884339980cae91ff273275a5129')
        db = connection.lifeings
        #user = db.User
        #connection.close()

        return db

db = Conn()

class User(object, db):
    def __init__(self, userName, email, pwd):
        self.userName = userName
        self.email = email
        self.pwd = pwd

    '''
    def hashPassword(self, password):
    self.pwd = pwd_context.encrypt(password)

    def verifyPassword(self, password):
    return pwd_context.verify(password, self.pwd)
    '''

    def save(self, db):
        user = {'userName': self.userName, 'email': self.email, 'pwd': self.pwd}
        userColl = db.User
        retID = coll.insert(user)
        db.close()
        return retID

    @staticmethod
    def queryUsers(email, db):
        user = getColl.findOne({"email": email})
        return user
