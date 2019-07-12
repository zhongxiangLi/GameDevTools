#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib

#使用python 库  求MD5
def run():
    #求字符串MD5
    # md5 = hashlib.md5('字符串').hexdigest()
    #求文件md5
    tmpFilePath=input("Input FilePath:")
    tmpFilePath=tmpFilePath.replace("\r","").replace("\n","").replace('"','')
    tmpFile = open(tmpFilePath,'rb')
    md5 = hashlib.md5(tmpFile.read()).hexdigest()
    tmpFile.close()
    print(md5)

if __name__=="__main__":
    run()
