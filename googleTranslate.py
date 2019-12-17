# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:04:42 2019

@author: 40346
"""
import re
import urllib.request
import HandleJs
from HandleJs import Py4Js
from langconv import *

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data


def translate(content, trans_direction):
    js = Py4Js()
    tk = js.getTk(content)
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return None
    content = urllib.parse.quote(content)
    if trans_direction == 'zh2en':
        url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
        tk, content)
    if trans_direction == 'en2zh':
        url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
        tk, content)
    if trans_direction == 'fr2zh':
        url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=fr&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
        tk, content)
    if trans_direction == 'zh2fr':
        url = "http://translate.google.cn/translate_a/single?client=t" + "&sl=zh-CN&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" + "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" + "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
        tk, content)
    result = open_url(url)
    end = result.find("\",")
    if end > 4:
        translation = result[4:end]
        return translation

def transPredicts(p,d):
    results=[]
    for ps in p:
        trans=translate(ps,d)
        complexTrans=Converter('zh-hant').convert(trans)
        results.append(trans)
        results.append(complexTrans)
    return results


