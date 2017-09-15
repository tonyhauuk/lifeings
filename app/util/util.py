# -*-coding:UTF-8-*-
import urllib
import urllib.request as req
import random

def sendSms(mobile):
    data = {}
    data['mobile'] = mobile
    data['verify'] = str(random.randint(1000 ,10000))

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