#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper

STR_DOWNLOAD_SUCCESS='DownLoad Success!'
STR_DOWNLOAD_FAILED='DownLoad Failed!'

def run():
    tmpUrl=input("Input Url:")
    if Helper.CheckUrl_Http_Https(tmpUrl):
        tmpSavePath=input("Input SavePath:")
        tmpSavePathStr=str(tmpSavePath)
        tmpSavePathStr=Helper.Remove_r_n(tmpSavePathStr)

        # 开始下载
        tmpRet=Helper.DownLoad(tmpUrl,tmpSavePathStr)
        if tmpRet:
            print(STR_DOWNLOAD_SUCCESS)
        else:
            print(STR_DOWNLOAD_FAILED)
            run()
    else:
        print(Helper.STR_INVALID_URL)
        run()


if __name__=="__main__":
    run()
