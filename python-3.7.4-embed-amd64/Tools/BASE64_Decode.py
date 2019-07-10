#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
from . import Helper

#使用python 库  求MD5
def run():
    print("打印结果为 b'字符串',取字符串即可\n")
    tmpStr=Helper.Remove_r_n(str(input("Input String:")))
    md5 = base64.b64decode(tmpStr.encode("utf-8"))
    print(md5)

if __name__=="__main__":
    run()
