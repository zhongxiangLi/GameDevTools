#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from Tools import Helper
import io
import os




def run():
    # print("to_JPG")
    print(u"合并一个文件夹的文本 到一个文本里，以文件夹名字命名，存放在文件夹同层目录。\n例如合并 C:/WorkSpace/Data 所有 lua 到 C:/WorkSpace/Data.lua。\n\n")

    tmPath=str(input(u"输入文件夹路径:"))
    tmPath=tmPath.replace("\r","").replace("\n","")
    print(u'合并 '+tmPath+':\n')

    tmpFileType=str(input(u"限定文件后缀 输入 .lua:"))
    tmpFileType=tmpFileType.replace("\r","").replace("\n","")

    tmpCombineTxtFilePath=Helper.CombineTxtToOneFile(tmPath,tmpFileType)

    print(u"保存到:"+tmpCombineTxtFilePath)

    

if __name__=="__main__":
    run()

        
