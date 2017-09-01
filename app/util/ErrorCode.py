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
            obj = {'code': 0, 'message': 'success', 'date': time.time()}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 1:
            obj = {'code': 1, 'message': 'password incorrect'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 2:
            obj = {'code': 2, 'message': 'args incomplete'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 3:
            obj = {'code': 3, 'message': 'args code'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 4:
            obj = {'code': 4, 'message': 'already taken'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 5:
            obj = {'code': 5, 'message': 'unregistered'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 6:
            obj = {'code': 6, 'message': 'create failed'}
            jsonStr = json.dumps(obj)
            return jsonStr

        elif code == 7:
            obj = {'code': 7, 'message': 'delete taken'}
            jsonStr = json.dumps(obj)
            return jsonStr
