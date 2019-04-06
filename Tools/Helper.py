#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib 


def DownLoad(varUrl,varSavePath):
    print(u"DownLoading:"+varUrl)
    urllib.urlretrieve(varUrl, varSavePath)

if __name__=="__main__":
    DownLoad('http://pic.cnblogs.com/face/u337375.jpg','./u337375.jpg')
