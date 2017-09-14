from pymongo import MongoClient
#from flask import jsonify
from flask import Flask
import json
import random
import uuid
from app.util.verify import *
from app.util.connect import Conn
import time
import datetime

c = Conn()

app = Flask(__name__)



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



def insert():
    connect()
    ss = "{'userName': 'wangxiao','userID':1,'email': 'wangxiao@estarinfo.net','mobile': '13261593150','password': '800915'," \
         "'birthday': '','city': 'Beijing', 'token': 'q938479r8uasfijda8shd9f8a9sdfha','expire': 1505121083000}"
    sql = json.dumps(ss)
    coll =  getCol('User')
    r = coll.insert(sql)
    print('ret status:  ' + r)
    close()

def ran():
    #r = random.randint(1000, 10000)
    r = uuid.uuid1()
    print(r)


def send():
    template_code = 'SMS_95510025'
    sign_name = '城市生活'
    verify = str(random.randint(1000, 10000))
    phone = str(13261593150)

    __business_id = uuid.uuid1()
    print(__business_id)

    params = '{\"verify\":' + verify + '}'
    print(send_sms(__business_id, phone, sign_name, template_code, params))

    time = datetime.datetime.now().strftime('%Y%m%d')

    print (query_send_detail(__business_id, phone, 10, 1, time))

if __name__ == '__main__':
    time = datetime.datetime.now().strftime('%Y%m%d')
    #print(time)

    send()
    #a = c.connect().City.find_one()
   # print(a)
    #ran()
   #insert()

    #connect()
    #r = checkExistUser()
   # print(r)






