#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from . import Helper


def run():
    tmp7zFilePath=input(u"输入7z文件路径:")
    tmp7zFilePath=tmp7zFilePath.replace("\r","").replace("\n","")
    Helper.Ex_7z(tmp7zFilePath)
    

if __name__=="__main__":
    run()
