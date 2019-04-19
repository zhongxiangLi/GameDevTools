#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import zipfile
import Helper

#使用python 库  求MD5
def run():
    tmpZipFilePath=os.getcwd()+"/Tools/MultiSizeIcon/MultiSizeIcon.zip"
    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    # print(tmpZipFilePath)
    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath)==False:
        # 先解压
        print(u"第一次打开，先解压\n")
        tmpZipFile=zipfile.ZipFile(tmpZipFilePath)
        print(tmpZipFile.namelist())


        tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
        os.mkdir(tmpTargetDirPath)
            

        for tmpOneName in tmpZipFile.namelist():
            tmpZipFile.extract(tmpOneName,tmpTargetDirPath)
        tmpZipFile.close()
        print(u"解压完成\n")

    tmpExePath=os.getcwd()+"/Tools/MultiSizeIcon/MultiSizeIcon/MultiSizeIcon/MultiSizeIcon.bat"
    # print(tmpExePath)
    Helper.OpenOneToolDir("MultiSizeIcon/MultiSizeIcon/MultiSizeIcon/")
    os.system(tmpExePath)

if __name__=="__main__":
    run()
