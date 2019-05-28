#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile
import sys
import os

#使用python 库
def run():
    # 直接打开
    tmpExePath=os.getcwd()+"/Tools/Shadowsocks/Shadowsocks.exe"
    print(tmpExePath)
    os.popen(tmpExePath)

if __name__=="__main__":
    run()