#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tools import GetFileMD5
from Tools import GetStrMD5
from Tools import GetUnixTimeStamp
from Tools import GetUnixTimeStamp_ms
from Tools import MultiSizeIcon
from Tools import HttpServer
from Tools import CheckServerPortOpen
from Tools import UnZipTools
from Tools import UnicodeToChinese
from Tools import ScreenCaptureGif
from Tools import Notepad
from Tools import PNGoo_Win

toolSets=\
{
    # 注册程序 与 关键字，关键字有多个
    # Module:[['keyword1','keyword2'],'注释'],

    # 获取文件MD5
    GetFileMD5:[['md5','file md5','file'],u'获取文件MD5'],

    # 获取字符串MD5
    GetStrMD5:[['md5','string md5','string','str md5'],u'获取字符串MD5'],

    # 获取 10位 Unix时间戳 单位秒
    GetUnixTimeStamp:[['unix','time','timestamp'],u'获取 10位 Unix时间戳 单位秒'],

    # 获取 13位 Unix时间戳 单位毫秒
    GetUnixTimeStamp_ms:[['unix','time','timestamp','ms'],u'获取 13位 Unix时间戳 单位毫秒'],

    # 一键生成Android、IOS 多尺寸Icon
    MultiSizeIcon:[['icon','icon size'],u'一键生成Android、IOS 多尺寸Icon'],

    # 简单http服务器
    HttpServer:[['http','httpserver','http server'],u'简单http服务器'],

    # telnet 测试端口是否开启
    CheckServerPortOpen:[['telnet','checkserverportopen','port','network','server','net'],u'测试端口是否开启'],

    # 解压ZIP
    UnZipTools:[['zip','unzip','extra','extract'],u'解压ZIP'],

    # Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸
    UnicodeToChinese:[['unicode','gbk','chinese','\u','url','urlencode','code','codec'],u'Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸'],

    # 屏幕录制Gif
    ScreenCaptureGif:[['gif','screen','capture','rec','url','licecap','cap'],u'屏幕录制Gif'],

    # Notepad 文本编辑器
    Notepad:[['txt','exe','edit','note','notepad','text'],u'文本编辑器'],

    # PNGoo PNG无损压缩
    PNGoo_Win:[['png','compress','png compress','image','image compress','yasuo'],u'PNG无损压缩'],
}

toolSets_old=toolSets
toolSets={}
# 反转
for tmpTool,tmpToolInfo in toolSets_old.items():
    for tmpOneKeyword in tmpToolInfo[0]:
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
            print(str(tmpIndex)+":"+tmpOneTool.__name__+" -"+toolSets_old[tmpOneTool][1])
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