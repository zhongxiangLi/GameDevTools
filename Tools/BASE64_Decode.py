#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
from . import Helper

#使用python 库  求MD5
def run():
    #求字符串MD5
    tmpStr=Helper.Remove_r_n(str(input("Input String:")))
    md5 = base64.b64decode(tmpStr)
    print(md5)

if __name__=="__main__":
    run()
