#! /user/bin/python
# -*-coding:UTF-8-*-

from flask import Flask, request, jsonify, abort
from util import ErrorCode
#from .conn import ConnDB

app = Flask(__name__)
error = ErrorCode.ErrCode()

#conn = ConnDB()

@app.route('/lifeings/api/v1.0/signin', methods=['POST', 'GET'])
@auth.login_required

def signIn():
	try:
		userName = request.args.get('u', '')
		pwd = request.args.get('p', '')
	except ValueError:
		jsonStr = error.getErrorCode(3)
		return jsonStr
	else:
		if userName != '' and pwd != '':
			# conn to mongodb
			conn.user.find_one({'userName': userName})
		else:
			jsonStr = error.getErrorCode(2)
			return jsonStr

if __name == '__main__':
	app.run(host = '0.0.0.0', port = 80, debug = True)