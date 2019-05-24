#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib

#使用python 库  求MD5
def run():
    #求字符串MD5
    tmpStr=input("Input String:")
    md5 = hashlib.sha1(tmpStr).hexdigest()
    print(md5)

if __name__=="__main__":
    run()
