#!/usr/bin/python
# -*- coding: UTF-8 -*-
import zipfile
import sys
import os

#使用python 库
def run():
    if sys.version_info<(3,0):
        tmpZipFilePath=input("ZipFilePath:")
    else:
        tmpZipFilePath=input("ZipFilePath:")

    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    print(tmpZipFilePath)
    tmpZipFile=zipfile.ZipFile(tmpZipFilePath)
    print(tmpZipFile.namelist())


    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath):
        tmpIndex=1
        while os.path.isdir(tmpTargetDirPath+"_"+str(tmpIndex)):
            tmpIndex=tmpIndex+1

        tmpTargetDirPath=tmpTargetDirPath+"_"+str(tmpIndex)
        os.makedirs(tmpTargetDirPath)
    else:
        os.mkdir(tmpTargetDirPath)
    for tmpOneName in tmpZipFile.namelist():
        tmpZipFile.extract(tmpOneName,tmpTargetDirPath)
    tmpZipFile.close()

if __name__=="__main__":
    run()