#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import Helper

#使用python 库  求MD5
def run():
    tmpExePath=os.getcwd()+"/Tools/MultiSizeIcon/MultiSizeIcon/bin/Debug/MultiSizeIcon.bat"
    # print(tmpExePath)
    Helper.OpenOneToolDir("MultiSizeIcon/MultiSizeIcon/bin/Debug/")
    os.system(tmpExePath)

if __name__=="__main__":
    run()
