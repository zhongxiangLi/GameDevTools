#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tools import Helper
import io
import os
import shutil
import time
import codecs

# 读取Txt,返回字符串
def ReadTxtFileToStr(varTxtFilePath):
    try:
        tmpTxtFile=codecs.open(varTxtFilePath,"r","utf-8")
        tmpStr=tmpTxtFile.read()
        tmpTxtFile.close()
    except UnicodeDecodeError:
        print("unicode decode error")
        tmpTxtFile=codecs.open(varTxtFilePath,"r","gbk")
        tmpStr=tmpTxtFile.read()
        tmpTxtFile.close()
    return tmpStr

# 将字符串写入一个Txt
def WriteStrToTxtFile(varStr,varTxtFilePath):
    print("WriteStrToTxtFile "+varTxtFilePath)
    tmpTxtFile=codecs.open(varTxtFilePath,"w","utf-8",errors='ignore')
    tmpTxtFile.write(varStr)
    tmpTxtFile.close()

def run():
    # print("to_JPG")
    print(u"转换一个文件夹的文本编码\n\n")

    tmPath=str(input(u"输入文件夹路径:"))
    # 要做带空格目录的处理
    tmPath=tmPath.replace("\r","").replace("\n","").replace('"','')

    print(u'转换 '+tmPath+':\n')

    tmpFileType=str(input(u"限定文件后缀(默认 .txt):"))
    tmpFileType=tmpFileType.replace("\r","").replace("\n","")
    if tmpFileType=="":
        tmpFileType=".txt"

    # 先备份文件夹
    now = time.time()
    now = (int(now * 1000))
    tmpBakDirPath=Helper.GetSystemAppDataDirPath()+"ConvertTxtEncoding/"+str(now)
    shutil.copytree(tmPath,tmpBakDirPath)
    print(u"文件备份至:"+tmpBakDirPath)


    tmpFiles=Helper.list_all_files(tmPath,tmpFileType)
    for tmpOneFilePath in tmpFiles:
        tmpStr=ReadTxtFileToStr(tmpOneFilePath)
        WriteStrToTxtFile(tmpStr,tmpOneFilePath)




    
    

if __name__=="__main__":
    run()

        
