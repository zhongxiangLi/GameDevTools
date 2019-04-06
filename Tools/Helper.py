#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib 

# 不规范的Url 
STR_INVALID_URL='url begin with http:// or https://'

# 去除 \r \n
def Remove_r_n(varStr):
    tmpStr=str(varStr)
    return tmpStr.replace('\r','').replace('\n','')

# 检查Url是否以 https http 开头
def CheckUrl_Http_Https(varUrl):
    tmpUrl=varUrl
    if tmpUrl.startswith('http://') or  tmpUrl.startswith('https://'):
        return True
    else:
        return False

# 下载文件 返回 True False代表Url是否合法
def DownLoad(varUrl,varSavePath):
    if CheckUrl_Http_Https(varUrl):
        print(u"DownLoading:"+varUrl)
        varUrl=Remove_r_n(varUrl)
        urllib.urlretrieve(varUrl, varSavePath)
        return True
    else:
        print(STR_INVALID_URL)
        return False

if __name__=="__main__":
    DownLoad('http://pic.cnblogs.com/face/u337375.jpg','./u337375.jpg')
