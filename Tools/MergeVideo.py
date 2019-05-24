#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tools import Helper
import io
import os
import zipfile

def Make_actemp(varVideoPath):
    tmpOutputPath=varVideoPath+".actemp"
    os.system(os.getcwd()+"/Tools/ffmpeg/ffmpeg/ffmpeg.exe -i "+varVideoPath+" -f mpeg -qscale 0.01 -y -r 29.97 "+tmpOutputPath)
    return tmpOutputPath

def run():
    tmpZipFilePath=os.getcwd()+"/Tools/ffmpeg/ffmpeg.zip"
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


    

    print(u"输入第一个视频文件地址:")
    tmpFirstFilePath=str(input())
    tmpFirstFilePath=Helper.Remove_r_n(tmpFirstFilePath)

    print(u"输入第二个视频文件地址:")
    tmpSecondFilePath=str(input())
    tmpSecondFilePath=Helper.Remove_r_n(tmpSecondFilePath)
    
    # 首先生成 .actemp 文件
    tmpFistOutputPath=Make_actemp(tmpFirstFilePath)
    tmpSecondOutputPath=Make_actemp(tmpSecondFilePath)

    # copy 操作 将两个 .actemp 文件合并
    tmpMergeFilePath=Helper.getdirpath(tmpSecondFilePath)+"combine.flv.actemp"
    tmpMergeFilePath=Helper.getWinPath(tmpMergeFilePath)

    tmpFistOutputPath=Helper.getWinPath(tmpFistOutputPath)

    tmpSecondOutputPath=Helper.getWinPath(tmpSecondOutputPath)

    tmpCommand='copy /b "'+tmpFistOutputPath+'"+"'+tmpSecondOutputPath+'" "'+tmpMergeFilePath+'" /y'
    print(tmpCommand)
    os.system(tmpCommand)

    # 生成视频格式
    tmpMergeVideoFilePath=Helper.getdirpath(tmpSecondFilePath)+"combine.mp4"
    tmpMergeVideoFilePath=Helper.getWinPath(tmpMergeVideoFilePath)
    tmpCommand=os.getcwd()+'/Tools/ffmpeg/ffmpeg/ffmpeg.exe -i "'+tmpMergeFilePath+'" -f mp4 -qscale 0.01 -y "'+tmpMergeVideoFilePath+'"'
    print(tmpCommand)
    os.system(tmpCommand)

if __name__=="__main__":
    run()
