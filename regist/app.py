#! /user/bin/python
# -*-coding:UTF-8-*-

from flask import request, Flask, jsonify, abort
from util import ErrorCode
from util import models

app = Flask(__name__)
error = ErrorCode.ErrCode()


@app.route('/lifeings/api/v1.0/reg', methods=['POST'])
def createUser():
    userName = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    mobile = request.json.get('mobile')
    birthday = request.json.get('birthday')
    city = request.json.get('city')

    if userName is None or password is None:
        abort(400)  # Missing arguments

    # if User.query.filter_by(userName = userName).first() is not None:
    #       abort(400) # Existing user
    try:
        if userName != '' and password != '' and email != '':
            if queryUsers(email) == '':
                user = User(userName, email, password)
                retID = user.save()
                jsonStr = error.getErrorCode(0)
                print (jsonStr)
                return jsonStr
            else:
                jsonStr = error.getErrorCode(4)
                return jsonStr
        else:
            jsonStr = error.getErrorCode(1)
            print (jsonStr)
            return jsonStr
    except ValueError:
        print 'Return id is NONE'

def queryUsers(str):
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

class User(name, email, pwd):
    def __init__(self):
        pass

