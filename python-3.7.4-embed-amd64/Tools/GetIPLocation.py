#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8 
import os
from . import Helper
import re

STR_DOWNLOAD_SUCCESS='Success!'
STR_DOWNLOAD_FAILED='Failed!'

def run():
    tmpStr_IP=""
    while tmpStr_IP=="":
        tmpStr_IP=input(u"输入IP/域名:").replace('\r','').replace('\n','').replace('"','')
    tmpUrl="http://ip.tool.chinaz.com/?IP="+str(tmpStr_IP)
    if Helper.CheckUrl_Http_Https(tmpUrl):
        # 开始下载
        tmpRet=Helper.GetHtml_UTF_8(tmpUrl)
        if tmpRet!=False:
            # print(tmpRet)
            #正则匹配 <dd class="fz24">183.14.134.235</dd>
            # (.+?) 代表变量
            tmplist=re.findall(r"<span class=\"Whwtdhalf w15-0\">(.+?)</span>",tmpRet,re.M)
            if len(tmplist)==6:
                print(tmplist[0:3])
                print(tmplist[3:])

            tmplist=re.findall(r"<span class=\"Whwtdhalf w50-0\">(.+?)</span>",tmpRet,re.M)
            
            if len(tmplist)==2:
                print(tmplist[0])
                print(tmplist[1])
        else:
            print(STR_DOWNLOAD_FAILED)
            run()
    else:
        print(Helper.STR_INVALID_URL)
        run()


if __name__=="__main__":
    
    run()
