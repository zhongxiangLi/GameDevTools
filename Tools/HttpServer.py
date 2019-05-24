#!/usr/bin/python
# -*- coding: UTF-8 -*-
from . import SimpleHTTPServer_WithPath
import SocketServer

#使用python 库  求MD5
def run():
    tmpWWW_Dir=raw_input("Input WWW Dir:").replace('\r','').replace('\n','')
    SimpleHTTPServer_WithPath.test(tmpWWW_Dir)

if __name__=="__main__":
    run()
