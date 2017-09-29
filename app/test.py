from pymongo import MongoClient
from gridfs import *
from flask import jsonify, request
from flask import Flask
import random
import uuid
from app.util.connect import Conn
import time
import json
import urllib
import urllib.request as req
from app.util.models import Process
import pprint
from app.util.error import getCode




c = Conn()
p = Process(c.connect())
app = Flask(__name__)

def checkExistUser1():
    db = c.connect()
    user = db.User
    n = '13261593150'
    isExist = user.find_one({'mobile': n})

    s = p.getCol('User').find_one()
    #print(s)
    pprint.pprint(s)
    #print(isExist)


    if isExist is None:
        result = 0
    else:
        result = 1

    c.close()

    return result

def getCol1(collection = None):
    if collection == None:
        return 2
    else:
        db = c.connect()
        name = db.get_collection(collection)
        c.close()
        return name



def insert1():
    c.connect()
    ss = "{'userName': 'wangxiao','userID':1,'email': 'wangxiao@estarinfo.net','mobile': '13261593150','password': '800915'," \
         "'birthday': '','city': 'Beijing', 'token': 'q938479r8uasfijda8shd9f8a9sdfha','expire': 1505121083000}"
    sql = json.dumps(ss)
    coll =  p.getCol('User')
    r = coll.insert(sql)
    print('ret status:  ' + r)
    c.close()

def ran():
    #r = random.randint(1000, 10000)
    r = uuid.uuid1()
    print(r)



def send():
    data = {}
    data['mobile'] = '13261593150'
    data['verify'] = str(random.randint(1000, 10000))

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    print(result)


def querySms(mobile):
    data = {}
    data['mobile'] = mobile

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    print(result)

def time2str():
    time1 = "2017-09-18 14:52:21"
    st = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
    timeStamp1 = int(time.mktime(st))

    time2 = "2017-09-18 14:57:21"
    st1 = time.strptime(time2, "%Y-%m-%d %H:%M:%S")
    timeStamp2 = int(time.mktime(st1))

    timeStamp = timeStamp2 - timeStamp1

    print(timeStamp)


def getType():
    with app.app_context():
        validate = '8800'
        phone = '132615965465'
        obj = {'verification': validate, 'mobile': phone}
        data = jsonify(obj)

        print(type(obj))

def findfind():
    name = p.getCol('User')
    phone = '13261593150'
    dates = {'mobile': phone}
    condition =  {'verification': 1, '_id': 0}
    value = p.findByCondition(dates, condition, 'User')
    print(value['verification'])

def findStrIndex():
    m = '13811300140'
    n = m.find('1')
    print(n)



def setUpdate():
    data = {'mobile': '13261593150'}
    set = {'birthday': 1}
    coll = p.getCol('User')
    result = coll.update(data, {'$set': set})
    #result = result['updatedExisting']

    if result:
        pprint.pprint(result)
    elif not result:
        print(2)

    #print(result)

    #print(p.find(data , 'User'))


def comfirmd():
    phone = '13261593150'
    data = {'mobile': phone}
    condition = {'isValidate': 1, '_id': 0}
    info = p.findByCondition(data, condition, 'User')
    isValidate = info['isValidate']



    if isValidate != 1:
        return getCode(11)
    elif isValidate == 1:
        return 'ok'


def insert111():
    validate = '5599'
    phone = '13811300144'
    obj = {'verification': validate, 'mobile': phone}
    #data = jsonify(obj)
    p.insert(obj, 'User')

    #pprint.pprint(p.find({'mobile': phone}, 'User'))
    try:
        data = {'mobile': phone}
        condition = {'isValidate': 1, '_id': 0}
        info = p.findByCondition(data, condition, 'User')
        isValidate = info['isValidate']
    except KeyError as e:
        print('mei you')

        #print(isValidate)

def findInfos():
    """

    :rtype: object
    """
    r = p.find({'mobile': '13261593150'}, 'User')
    pprint.pprint(r)

def test1():
    a = 'sdfsdfsdfsdf'
    return a


def test2():
    return test1()


def test3():
    raise Exception


def calc():
    a = 3600 * 24 * 30
    t = round(time.time())
    print(t + a)


def trycatch():
    #r = 1
    try :
        r = 899
        with open('!KEY', 'r') as f:
            file = f.read()

    except Exception as e:
        y = 0
        #r = 5
        print(r)
        #r = 7

    t = 2 * 4
    #print(r)

@app.route('/json')
def getJson():
    msg = getCode(2)
   #print(type(msg))
    return str(type(msg))

def getDBVersion():
    db = c.connect()
    print(db.version)

#if __name__ == '__main__':


    #getDBVersion()
    pass
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = s[::-1]
    print(s)

    #app.run(debug=True, host='0.0.0.0', port=5001)

    # data2 = json.loads('http://localhost:5001/json')
    # print('code :' + data2['code'])
    #trycatch()
    #calc()
    #test3()
    #print(test2())
    #findInfos()

    #setUpdate()
    #findfind()
    #findStrIndex()
    #getType()
    #time2str()
    #send()

    #querySms(13261593150)

    #
    # if not name:
    #     print('not null')
    # else:
    #     print('is null')
    #time = datetime.datetime.now().strftime('%Y%m%d')
    #print(time)

    #send()
    #a = c.connect().City.find_one()
   # print(a)
    #ran()
   #insert()
    #checkExistUser1()
    #connect()
    #r = checkExistUser()
   # print(r)
    #print(comfirmd())
    #insert111()
import json


class Test_0_1(object):
    baseUrl = 'http://localhost:5001/api/v0.1'


    def __init__(self):
        self.headers = {}
        self.token = None


    def login(self, phone, password, path = '/login'):
        load = {'phone': phone, 'password': password}
        self.headers = {'content-type': 'application/json'}
        response = req.Request(url = self.baseUrl + path, data = json.dumps(load), headers = self.headers)
        resData = json.loads(response.data)
        self.token = resData.get('token')
        return resData


    def user(self, path = '/user'):
        self.headers = {'token': self.token}
        response = req.Request(url = self.baseUrl + path, headers = self.headers)
        resData = json.loads(response.data)
        return resData


    def reg1(self, phone, path = '/reg-1'):
        load = {'phone': phone}
        self.headers = {'content-type': 'application/json'}
        response = req.post(url = self.baseUrl + path, data = json.dumps(load), headers = self.headers)
        resData = json.loads(response.content)
        print(resData.get('code'))
        print(resData.get('message'))
        return resData


    def reg2(self, phone, validateCode, path = '/reg-2'):
        load = {'phone': phone, 'validateCode':  validateCode}
        self.headers = {'content-type': 'application/json'}
        response = req.post(url=self.baseUrl + path, data=json.dumps(load), headers=self.headers)
        resData = json.loads(response.content)
        print(resData.get('message'))
        return resData


    def reg3(self, phone, password, confirm, paht = '/reg-3'):
        load = {'phone': phone, 'password': password, 'confirm': confirm}
        self.headers = {'content-type': 'application/json'}
        response = req.post(url=self.baseUrl + path, data=json.dumps(load), headers=self.headers)
        resData = json.loads(response.content)
        print(resData.get('message'))
        return resData


if __name__ == '__main__':
    api = Test_0_1()
    user = api.login('13261593150', '800915')
    print(user)

    u = api.user()
    print(u)
