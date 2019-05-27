#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import codecs
import base64
import os
from . import Helper

# 设置导出目录
tmpExportDirPath="./Tools/HarExport/Export"

def SaveFileWithUrl(varUrl,varBytes):
    tmpUrlStr=varUrl.replace("https://","").replace("http://","")

    global tmpExportDirPath
    tmpDirPath=tmpExportDirPath+"/"
    tmpFileName=""

    # 以/ 拆分网址，创建文件夹
    while True:
        if tmpUrlStr=="":
            break
        tmpStrParts=tmpUrlStr.partition('/')
        if tmpStrParts[1]=='/':
            tmpUrlStr=tmpStrParts[2]

            tmpDirPath=tmpDirPath+"/"+tmpStrParts[0]
            print(tmpDirPath)
            
            # 创建文件夹
            if os.path.exists(tmpDirPath)==False:
                os.makedirs(tmpDirPath)
        else:
            tmpFileName=tmpStrParts[0]
            # 去除 ? 后面部分
            tmpStrParts=tmpFileName.partition('?')
            if tmpStrParts[1]=='?':
                tmpFileName=tmpStrParts[0]
            print(tmpFileName)
            tmpFilePath=tmpDirPath+"/"+tmpFileName

            if os.path.exists(tmpFilePath):
                os.remove(tmpFilePath)
            fo = open(tmpFilePath, "xb")
            fo.write(varBytes)
            fo.close()

            break


def run():
    Helper.ShowLogo(u"H5网页游戏素材提取工具\n\n第一次使用请阅读 README.pdf \n\n")
    Helper.OpenOneToolDir("HarExport/")

    tmpHarFilePath=str(input(u"输入har文件路径:")).replace('"','')
    global tmpExportDirPath
    tmpDirPath=str(input(u"设置导出目录 绝对路径 (默认为Export):")).replace('"','')
    if tmpDirPath!="":
        tmpExportDirPath=tmpDirPath
    # print(tmpExportDirPath)

    with codecs.open(tmpHarFilePath,"r","utf-8",errors='ignore') as tmpHarFile:
        harDic=json.load(tmpHarFile)
        print(len(harDic["log"]["entries"]))

        tmpEntries=harDic["log"]["entries"]
        for tmpEntry in tmpEntries:
            
            tmpContentDic=tmpEntry["response"]["content"]
            if 'encoding' in tmpContentDic:
                tmpEncoding=tmpEntry["response"]["content"]["encoding"]
                if tmpEncoding=="base64":
                    print(tmpEntry["request"]["url"])
                    # print(tmpEntry["response"]["content"]["text"])
                    tmpBytes=base64.b64decode(tmpEntry["response"]["content"]["text"])
                    SaveFileWithUrl(tmpEntry["request"]["url"],tmpBytes)
