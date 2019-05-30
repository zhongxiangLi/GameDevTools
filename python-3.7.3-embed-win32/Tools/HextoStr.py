#!/usr/bin/python
# -*- coding: UTF-8 -*-

import binascii

#使用python 库  求MD5
def run():
    #求字符串MD5
    tmpHexStr=input(u"输入16进制字符串 eg:\\x67\\x65\\x74\\x54\\x69\\x6D\\x65:").replace("'",'').replace('"','').replace('\r','').replace('\n','').replace('\\x','')
    print(binascii.unhexlify(tmpHexStr.encode("utf-8")).decode('utf8'))

if __name__=="__main__":
    run()
