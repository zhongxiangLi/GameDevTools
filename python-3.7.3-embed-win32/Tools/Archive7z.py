#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from . import Helper


def run():
    tmpFilePath=input(u"输入文件或文件夹路径:")
    tmpFilePath=tmpFilePath.replace("\r","").replace("\n","")
    Helper.Archive_7z(tmpFilePath)
    

if __name__=="__main__":
    run()
