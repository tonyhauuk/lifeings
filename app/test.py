from pymongo import MongoClient


def connect():
    client = MongoClient('123.56.71.98:27017')
    db = client.lifeings
    db.authenticate('lifeingsAdmin', 'a9270ae592bd52cceb7e7736a434506d')

    return db


def close():
    client = MongoClient('123.56.71.98:27017')
    client.close()


def checkExistUser():
    db = connect()
    user = db.User
    n = int('13261593150')
    isExist = user.find_one({'mobile': n})

    s = getCol('City').find_one()
    print(s)

    #print(isExist)


    if isExist is None:
        result = 0
    else:
        result = 1

    close()

    return result

def getCol(collection = None):
    if collection == None:
        return 2
    else:
        db = connect()
        name = db.get_collection(collection)
        close()
        return name


if __name__ == '__main__':
    connect()
    r = checkExistUser()
   # print(r)
