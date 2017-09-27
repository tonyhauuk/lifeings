# -*-coding:UTF-8-*-
import urllib
import urllib.request as req

def sendSms(mobile, verify):
    data = {}
    data['mobile'] = mobile
    data['verify'] = verify

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    return result

def querySms(mobile):
    data = {}
    data['mobile'] = mobile

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    return result