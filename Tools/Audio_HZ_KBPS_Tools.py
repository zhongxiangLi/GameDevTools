#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tools import Helper
import io
import os
import zipfile

#使用python 库  求MD5
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


    print(u"MP3的采样频率分为48000 44100 32000 24000 22050 16000 12050 8000等等。\n码率有320kbps 256 224 192 128 112 96 80 64 56等等，都是2的n次方。\n")

    print(u"输入音效文件地址:")
    tmpFilePath=str(raw_input())
    tmpFilePath=Helper.Remove_r_n(tmpFilePath)
    
    print(u"输入采样(默认44100hz):")
    tmpHZ=str(raw_input())
    tmpHZ=Helper.Remove_r_n(tmpHZ)
    if tmpHZ=="":
        tmpHZ="44100"

    print(u"输入声道 数字(默认单声道 1):")
    tmpChannel=str(raw_input())
    tmpChannel=Helper.Remove_r_n(tmpChannel)
    if tmpChannel=="":
        tmpChannel="1"

    print(u"输入比特率 数字(默认96kbps):")
    tmpBits=str(raw_input())
    tmpBits=Helper.Remove_r_n(tmpBits)
    if tmpBits=="":
        tmpBits="96k"

    tmpStrParts=tmpFilePath.rpartition('.')
    tmpNewPath=tmpStrParts[0]+'_new'+tmpStrParts[1]+tmpStrParts[2]
    os.system(os.getcwd()+"/Tools/ffmpeg/ffmpeg/ffmpeg.exe  -y -i "+tmpFilePath+" -ar "+tmpHZ+" -ac "+tmpChannel+" -ab "+tmpBits+"k "+tmpNewPath)

if __name__=="__main__":
    run()
