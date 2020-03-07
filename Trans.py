import http.client
import hashlib
import urllib.parse
import random
import json
import time
def baiduTranslate(q="苹果", fromLang="zh", toLang="en"):
    appid = '20200305000392975' #你的appid(这里是必填的, 从百度 开发者信息一览获取)
    secretKey = 'RjxBbx6zBrMGaYL8rrhI' #你的密钥(这里是必填的, 从百度 开发者信息一览获取)

    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode())
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    result = ""
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com',timeout=10)
        httpClient.request('GET', myurl)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
    except Exception as e:
        print (e)
        time.sleep(50)
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com',timeout=10)
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
    finally:
        if httpClient:
            httpClient.close()
    result=json.loads(result)['trans_result'][0]['dst']
    return result


def transList(ql,s,d):
    result=[]
    n=0
    for q in ql:
        r=baiduTranslate(q,s,d)
        if r!=None:
            result.append(r)
    return result

