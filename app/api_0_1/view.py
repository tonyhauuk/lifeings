# -*-coding:UTF-8-*-

from flask import request, Flask, g, jsonify
from app.util.error import getCode
from app.util.models import Process
from . import api
import hashlib
from functools import wraps
from app.util.util import *
from app.util.connect import Conn
import time


app = Flask(__name__)
c = Conn()


def loginCheck(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return getCode(3)

        return func(*args, **kwargs)
    return decorator

# Login
@api.route('/login', methods=['POST'])
def login():
    confirm = -1
    password, pwd, phone = '', '', ''
    db = c.connect()
    try:
        phone = request.get_json().get('phone')
        password = request.get_json().get('password')
        confirm = Process(db).checkExistUser(phone)
        data = {'mobile': phone}
        setter = {'password': 1, '_id': 0}
        pwd = Process(db).findByCondition(data, setter, 'User')
    except Exception as e:
        print(e)

    if confirm == 0:
        return getCode(5)

    if password != pwd:
        return getCode(1)
        

    m = hashlib.md5()
    m.update(phone)
    token = m.hexdigest()

    try:
        aging = 3600 * 24 * 30
        t = round(time.time())
        data = {'mobile': phone}
        setter = {'token': token, 'expire': t + aging}
        results = Process(db).setUpdate(data, setter, 'User')
        result = results['updatedExisting']

        if result:
            data = {'mobile': phone}
            infos = Process(db).find(data, 'User')
            nickname = infos['nickname']
            msg = {'code': 0, 'message': 'success', 'nickname': nickname, 'token': token}
            return msg
    except:
        return getCode(8)
    finally:
        c.close()


# Upload avatar
@api.route('/set-avatar', methods=['POST'])
@loginCheck
def setAvatar():
    avatar = request.get_json().get('avatar')
    user = g.current_user
    user.avatar = avatar
    try:
        pass    # db commit
    except Exception as e:
        print(e)
        return getCode(8)
        

    # db commit photo upload
    return getCode(0)


# Send sms
@api.route('/reg-1', methods=['POST'])
def sendSMS():
    phone = str(request.get_json().get('phone'))
    index = phone.find('1')

    if phone == '' or len(phone) < 11 or index != 0:
        return getCode(11)

    confirm = 0
    db = c.connect()
    try:
        confirm = Process(db).checkExistUser(phone)
        data = {'mobile': phone}
        condition = {'isValidate': 1, '_id': 0}
        info = Process(db).findByCondition(data, condition, 'User')
        isValidate = info['isValidate']
    except KeyError:
        isValidate = 0
        confirm = -1


    if confirm == 1 or isValidate == 1:
        return getCode(13)

    validate = str(random.randint(1000, 10000))
    send = sendSms(phone, validate)

    try:
        if send == 'OK':
            data = {'verification': validate, 'mobile': phone}
            Process(db).insert(data, 'User')

            return getCode(0)
        else:
            return getCode(12)
    except:
        return getCode(8)
    finally:
        c.close()


# Receive sms & validate sms
@api.route('/reg-2', methods=['POST'])
def receiveSMS():
    phone = request.get_json().get('phone')
    validateCode = request.get_json().get('validate')

    try:
        # Get db verification info
        data = {'mobile': phone}
        condition = {'verification': 1, '_id': 0}
        db = c.connect()
        validate = Process(db).findByCondition(data, condition, 'User')
        code = validate['verification']

        index = phone.find('1')
        if phone == '' or len(phone) < 11 or index != 0:
            return getCode(11)

        confirm = Process(db).checkExistUser(phone)
        currentTime = time.time()

        if confirm == 1:
            return getCode(13) # exist

        recvTime = querySms(phone)
        st = time.strptime(recvTime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(recvTime.mktime(st)) + 300

        if currentTime < timeStamp and code == validateCode:
            data = {'mobile': phone}
            setter = {'isValidate': 1}
            results = Process(db).setUpdate(data, setter, 'User')
            result = results['updatedExisting']

            if result:
                return getCode(0)
            else:
                return  getCode(3)
        else:
            return getCode(3)
    except:
        getCode(3)
    finally:
        c.close()


# Commit password
@api.route('/reg-3', methods=['POST'])
def commitPasswd():
    phone = request.get_json().get('phone')
    password = request.get_json().get('password')
    confirm = request.get_json().get('confirm')

    if len(password) < 6:
        return getCode(9)
        

    if password != confirm:
        return getCode(10)

    try:
        db = c.connect()
        data = {'mobile': phone}
        condition = {'isValidate': 1, '_id': 0}
        info = Process(db).findByCondition(data, condition, 'User')
        isValidate = info['isValidate']

        if isValidate != 1:
            return getCode(11)

        m = hashlib.md5()
        m.update(phone)
        token = m.hexdigest()

        setter = {'password': password, 'token': token, 'nickname': phone}
        results = Process(db).setUpdate(data, setter, 'User')
        result = results['updatedExisting']

        if not result:
            return getCode(4)

        return getCode(0)
    except:
        return getCode(4)
    finally:
        c.close()


