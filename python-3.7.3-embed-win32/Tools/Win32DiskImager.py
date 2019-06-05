#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper

#使用python 库  求MD5
def run():
    tmpZipFilePath=os.getcwd()+"/Tools/Win32DiskImager/Win32DiskImager.7z"
    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    # print(tmpZipFilePath)
    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath)==False:
        # 先解压
        print(u"第一次打开，先解压\n")
        Helper.Ex_7z(tmpZipFilePath,False)
        print(u"解压完成\n")

    tmpExePath=os.getcwd()+"/Tools/Win32DiskImager/Win32DiskImager/Win32DiskImager.exe"
    # print(tmpExePath)
    # Helper.OpenOneToolDir("Win32DiskImager/Win32DiskImager/")
    os.popen(tmpExePath)

if __name__=="__main__":
    run()
