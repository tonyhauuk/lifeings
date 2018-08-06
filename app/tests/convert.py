# !/usr/local/bin/python3
# -*- coding:utf-8 -*-

import time, json
from ShowapiRequest import ShowapiRequest


class Convert:
    def __init__(self):
        self.appID = '70177'
        self.secertCode = '23fd11a8b128419d933c687b4765d71e'

    def doPost(self, url, account = '', biz = ''):
        appID = self.appID
        secert = self.secertCode

        t = time.time()
        start = int(round(t * 1000))

        r = ShowapiRequest("http://route.showapi.com/1456-1", appID, secert)
        r.addBodyPara("url", url)
        r.addBodyPara("account", account)
        r.addBodyPara("biz", biz)
        res = r.post()
        result = res.text

        t1 = time.time()
        end = int(round(t1 * 1000))
        print('\nUsed time: ' + str(end - start) + 'ms')

        jsonStr = json.loads(result)
        resCode = jsonStr['showapi_res_code']
        if resCode == 0:
            body = jsonStr['showapi_res_body']
            retCode = body['ret_code']
            if retCode == 0:
                permanentUrl = body['url']
                tempUrl = body['src_url']
                print('\nPermanten Url: ' + permanentUrl + '\nTemporary Url: ' + tempUrl)
            else:
                errorMsg = body['error']
                print('\nConvert Failed! & Error Message: ' + errorMsg)
        else:
            error = jsonStr['showapi_res_error']
            print('error message: ' + error)


if __name__ == '__main__':
    url = ('https://mp.weixin.qq.com/s?timestamp=1533262921&src=3&ver=1&signature=0sxpyCRiJYv*ccvOSkenDk'
           'hDwOZZ6FwLp*ZquVkt58E5kLBZgyvvviWVgL-Y2f08SPRFo2aQGRkjy0GYx5nbvgZiF0lS0EvhdS3sE6E1NLDfzSHMN9'
           'kFajfxWELUtJfAyn5GVfUAe4hrjQi0ssiSw-1RNkoEZfADDAcnYojwJPg=')
    account = 'Ford_Go_Further'
    biz = ''

    c = Convert()
    c.doPost(url, account)
