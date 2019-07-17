#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8 
import os
from . import Helper
import re

STR_DOWNLOAD_SUCCESS='Success!'
STR_DOWNLOAD_FAILED='Failed!'

def run():
    tmpUrl="http://ip.tool.chinaz.com/"
    if Helper.CheckUrl_Http_Https(tmpUrl):
        # 开始下载
        tmpRet=Helper.GetHtml_UTF_8(tmpUrl)
        if tmpRet!=False and len(tmpRet)>10000:
            #print(tmpRet)
            #正则匹配 <dd class="fz24">183.14.134.235</dd>
            # (.+?) 代表变量
            tmplist=re.findall(r"<dd class=\"fz24\">(.+?)</dd>",tmpRet,re.M)
            # print(tmplist)
            if len(tmplist)==1:
                print(tmplist[0])

            tmplist=re.findall(r"<dd>(.+?)<a href=\"http://tool.chinaz.com/contact",tmpRet,re.M)
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
