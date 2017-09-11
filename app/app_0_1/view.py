from flask import request, Flask, g, current_app
from ..util import error
from ..util import models
from . import api
import hashlib
from functools import wraps
import random


app = Flask(__name__)
code = error.StatusCode()

def loginCheck(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        pass


# Login
@api.route('/login', methods=['POST'])
def login():
    confirm, phoneNum = 0, 0
    passwd = ''

    try:
        phoneNum = int(request.get_json().get('phone'))
        passwd = request.get_json().get('password')
        confirm = models.Process(phoneNum).checkExistUser()
    except Exception as e:
        print(e)

    if confirm == 0:
        msg = code.getCode(5)
        return msg

    if passwd != passwd: # user.password
        msg = code.getCode(1)
        return msg

    m = hashlib.md5()
    m.update(phoneNum)
    m.update(passwd)

    token = m.hexdigest()

    msg = code.getCode(0)
    return msg


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
        msg = code.getCode(8)

        return msg

    # db commit photo upload
    msg = code.getCode(0)
    return msg


# Receive sms
@api.route('/reg-1', methods=['POST'])
def receiveSMS():
    phoneNum = request.get_json().get('phone')
    user = User.query.filter_by(phoneNum = phoneNum).first()

    if user:
        msg = code.getCode(4)
        return msg

    validateNum = str(random.randint(1000, 10000))

    '''
        write db
    '''

    msg = code.getCode(0)
    return msg


# Validate sms
@api.route('/reg-2', methods=['POST'])
def verifySMS():
    phoneNum = request.get_json().get('phone')
    validateNum = request.get_json().get('validate number')
    validateMongoDB = ''

    if validateNum != validateMongoDB:
        msg = code.getCode(3)
        return msg

    '''
        db commit
        把验证信息写入数据库，提交密码时候需要验证是否通过
    '''

    msg = code.getCode(0)
    return msg


# Commit password
@api.route('/reg-3', methods=['POST'])
def commitPasswd():
    phoneNum = request.get_json().get('phone')
    passwd = request.get_json().get('password')
    confirm = request.get_json().get('password confirm')

    if len(passwd) < 6:
        msg = code.getCode(9)
        return msg

    if passwd != confirm:
        msg = code.getCode(10)
        return msg

    isValidate = '数据库获取的验证通过信息(用 phoneNum)'

    if isValidate != 1:
        msg = code.getCode(11)
        return msg

    '''
        数据库提交密码
    '''

    msg = code.getCode(0)
    return msg



