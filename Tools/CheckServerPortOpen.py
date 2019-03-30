#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

#使用python 库  求MD5
def run():
    #求字符串MD5
    tmpStr_IP=raw_input("Input IP:").replace('\r','').replace('\n','')
    tmpStr_Port=raw_input("Input Port:").replace('\r','').replace('\n','')
    s = socket.socket()
    tmpPort=int(tmpStr_Port)
    try:
        print("Connect ing ...")
        s.connect((tmpStr_IP,tmpPort))
        print('connect success\n')
    except Exception as e:
        print('connect failed\n')

if __name__=="__main__":
    run()
