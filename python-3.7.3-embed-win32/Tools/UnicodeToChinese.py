#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def run():
    tmpStr_Unicode=input("Input Unicode:").replace('\r','').replace('\n','')
    # tmpStr_Normal=tmpStr_Unicode.encode("GBK")
    print(tmpStr_Unicode.encode('utf-8').decode("unicode_escape"))

if __name__=="__main__":
    run()