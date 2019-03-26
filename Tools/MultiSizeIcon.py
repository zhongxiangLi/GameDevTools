#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

#使用python 库  求MD5
def run():
    tmpExePath=os.getcwd()+"/Tools/MultiSizeIcon/MultiSizeIcon/bin/Debug/MultiSizeIcon.exe"
    # print(tmpExePath)
    os.system(tmpExePath)

if __name__=="__main__":
    run()
