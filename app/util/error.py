# -*-coding:UTF-8-*-

import time
from flask import jsonify


def getCode(code, t = time.time()):
    if code == 0:
        obj = {'code': 0, 'message': 'success', 'date': t}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 1:
        obj = {'code': 1, 'message': 'password incorrect'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 2:
        obj = {'code': 2, 'message': 'parameter incomplete'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 3:
        obj = {'code': 3, 'message': 'verification failed'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 4:
        obj = {'code': 4, 'message': 'register failed'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 5:
        obj = {'code': 5, 'message': 'unregistered'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 6:
        obj = {'code': 6, 'message': 'create failed'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 7:
        obj = {'code': 7, 'message': 'delete taken'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 8:
        obj = {'code': 8, 'message': 'upload failed'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 9:
        obj = {'code': 9, 'message': 'password length must be over 6 numbers including letters'}
        jsonStr = jsonify(obj)
        return  jsonStr

    elif code == 10:
        obj = {'code': 10, 'message': 'password must be consistent'}
        jsonStr = jsonify(obj)
        return  jsonStr

    elif code == 11:
        obj = {'code': 11, 'message': 'illegal parameter'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 12:
        obj = {'code': 12, 'message': 'send failed'}
        jsonStr = jsonify(obj)
        return jsonStr

    elif code == 13:
        obj = {'code': 13, 'message': 'user exist'}
        jsonStr = jsonify(obj)
        return jsonStr