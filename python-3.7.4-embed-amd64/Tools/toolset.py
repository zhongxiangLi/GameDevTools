#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper

#传入工具详细信息
def run(varToolInfo):
        tmpZipFilePath=os.getcwd()+"/Tools/"+varToolInfo["7zfile"]
        tmpZipFilePath=tmpZipFilePath.replace('\\','/')
        # print(tmpZipFilePath)
        tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
        if os.path.isdir(tmpTargetDirPath)==False:
                # 先解压
                print(u"第一次打开，先解压\n")
                Helper.Ex_7z(tmpZipFilePath,False)
                print(u"解压完成\n")

        tmpExePath=os.getcwd()+"/Tools/"+varToolInfo["exepath"]
        os.system("start "+tmpExePath)
