#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64

from . import Helper

#字符串转全大写
def run():
    print(u"字符串转全小写\n")
    tmpStr=Helper.Remove_r_n(str(input("Input String:")))
    tmpLowerStr =tmpStr.lower()
    print(tmpLowerStr)
    print(u"已经复制到粘贴板\n")

    Helper.SetClipboard(tmpLowerStr)

if __name__=="__main__":
    run()
