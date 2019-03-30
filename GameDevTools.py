#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tools import GetFileMD5
from Tools import GetStrMD5
from Tools import GetUnixTimeStamp
from Tools import GetUnixTimeStamp_ms
from Tools import MultiSizeIcon
from Tools import HttpServer
from Tools import CheckServerPortOpen


toolSets=\
{
    # 注册程序 与 关键字，关键字有多个
    # Module:['keyword1','keyword2']

    # 获取文件MD5
    GetFileMD5:['md5','file md5','file'],

    # 获取字符串MD5
    GetStrMD5:['md5','string md5','string','str md5'],

    # 获取 10位 Unix时间戳 单位秒
    GetUnixTimeStamp:['unix','time','timestamp'],

    # 获取 13位 Unix时间戳 单位毫秒
    GetUnixTimeStamp_ms:['unix','time','timestamp','ms'],

    # MultiSizeIcon
    MultiSizeIcon:['icon','icon size'],

    # HttpServer
    HttpServer:['http','httpserver','http server'],

    # CheckServerPortOpen
    CheckServerPortOpen:['telnet','checkserverportopen','port','network','server','net'],
}

toolSets_old=toolSets
toolSets={}
# 反转
for tmpTool,tmpKeywords in toolSets_old.items():
    for tmpOneKeyword in tmpKeywords:
        if toolSets.has_key(tmpOneKeyword)==False:
            toolSets[tmpOneKeyword]=[]
        toolSets[tmpOneKeyword].append(tmpTool)



# print(toolSets)
# print(toolSets[GetFileMD5])

def searchKeyword(varKeyword):
    if toolSets.has_key(varKeyword):
        tmpTools=toolSets[varKeyword]
        for tmpIndex in range(len(tmpTools)):
            tmpOneTool=tmpTools[tmpIndex]
            print(str(tmpIndex)+":"+tmpOneTool.__name__)
        tmpIndex=input("Choose:")

        print("-------"+tmpTools[tmpIndex].__name__+"-------")
        tmpTools[tmpIndex].run()

    else:
        print("not found")

def sayHello():
    tmpKeyword=raw_input("Search:")
    searchKeyword(tmpKeyword.rstrip('\r'))
    print('\n\n')
        
    sayHello()

if __name__=="__main__":
     sayHello()