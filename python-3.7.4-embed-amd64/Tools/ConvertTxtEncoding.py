#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from Tools import Helper
import io
import os
import shutil


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
    tmpBakDirPath=Helper.GetSystemAppDataDirPath()+"ConvertTxtEncoding/"
    shutil.copytree(tmPath,tmpBakDirPath)
    print(u"文件备份至:"+tmpBakDirPath)

    tmpCommandExe=os.getcwd()+"\\Tools\\linuxcommand\\usr\\bin\\file.exe "
    tmpCommandExe_iconv=os.getcwd()+"\\Tools\\linuxcommand\\usr\\bin\\iconv.exe "

    tmpFiles=Helper.list_all_files(tmPath,tmpFileType)
    for tmpOneFilePath in tmpFiles:
        # 首先获取文件编码
        tmpPrint,tmpRetCode=Helper.RunShellWithReturnCode(tmpCommandExe+'"'+tmpOneFilePath+'"')
        print(tmpPrint)
        tmpPrint=str(tmpPrint)

        tmpParts=tmpPrint.partition(': ')
        print(tmpParts)
        if tmpParts[1]==': ':
            tmpParts=tmpParts[2].partition(' ')
            if tmpParts[1]==' ':
                print(tmpParts[0])

                tmpFromEncode=tmpParts[0]
                tmpToEncode="utf-8"
                tmpCommandStr=tmpCommandExe_iconv+"-f "+tmpFromEncode+" -t "+tmpToEncode+' "'+tmpOneFilePath+'" >> "'+tmpOneFilePath+'"'
                print(tmpCommandStr)
                # tmpPrint,tmpRetCode=Helper.RunShellWithReturnCode(tmpCommandExe+'"'+tmpOneFilePath+'"')
                # print(tmpPrint)



    
    

if __name__=="__main__":
    run()

        
