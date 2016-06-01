#! /user/bin/python
# -*-coding:UTF-8-*-

import json
import time


class ErrCode():
    '''docstring for ErrorCode
    def __init__(self, arg):
            super(ErrorCode, self).__init__()
            self.arg = arg
'''

    def getErrorCode(self, code):
        if code == 0:
            obj = {'error': 0, 'status': 'success', 'date': time.time()}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 1:
            obj = {'error': 1, 'status': 'password incorrect'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 2:
            obj = {'error': 2, 'status': 'args incomplete'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 3:
            obj = {'error': 3, 'status': 'args error'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 4:
            obj = {'error': 4, 'status': 'already taken'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 5:
            obj = {'error': 5, 'status': 'unregistered'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 6:
            obj = {'error': 6, 'status': 'create failed'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 7:
            obj = {'error': 7, 'status': 'delete taken'}
            jsonStr = json.dumps(obj)
            return jsonStr
