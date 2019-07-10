#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile
import sys
import os


def run():
    # 首先查找C:\Users\Administrator\AppData\Local\Postman\Update.exe 看是否安装
    tmpAppData_Path=os.getenv('LOCALAPPDATA') # C:\Users\Administrator\AppData\Local
    tmpPostmanInstallPath=tmpAppData_Path+"\\Postman\\app-7.2.2\\Postman.exe"
    if os.path.exists(tmpPostmanInstallPath) and os.path.isfile(tmpPostmanInstallPath):
        os.system("start "+tmpPostmanInstallPath)

        return
    else:
        # 安装 第一次安装会自动打开
        print(u"第一次打开，先安装\n")
        tmpExePath=os.getcwd()+"/Tools/Postman/Postman-win64-7.2.2-Setup.exe"
        print(tmpExePath)
        os.system("start "+tmpExePath)

if __name__=="__main__":
    run()