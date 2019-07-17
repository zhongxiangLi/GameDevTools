#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8 
import os
from . import Helper
import re
import requests

STR_DOWNLOAD_SUCCESS='Success!'
STR_DOWNLOAD_FAILED='Failed!'

def run():
    tmpStr_IP=""
    while tmpStr_IP=="":
        tmpStr_IP=input(u"输入IP:").replace('\r','').replace('\n','').replace('"','')
    tmpUrl="http://www.ip138.com/"
    if Helper.CheckUrl_Http_Https(tmpUrl):
        # 开始下载
        tmpRet=requests.get(tmpUrl)
        if tmpRet!=None:
            print(tmpRet)
            #正则匹配 <dd class="fz24">183.14.134.235</dd>
            # (.+?) 代表变量
            tmplist=re.findall(r"<td align=\"center\"><h1>(.+?)</h1></td>",tmpRet.text,re.M)
            # print(tmplist)
            if len(tmplist)==1:
                print(tmplist[0])

            tmplist=re.findall(r"<td align=\"center\"><ul class=\"ul1\">(.+?)</ul></td>",tmpRet.text,re.M)
            # print(tmplist)
            if len(tmplist)==1:
                print(tmplist[0])
        else:
            print(STR_DOWNLOAD_FAILED)
            run()
    else:
        print(Helper.STR_INVALID_URL)
        run()


if __name__=="__main__":
    
    run()
