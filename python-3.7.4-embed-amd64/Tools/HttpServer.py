#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess

#使用python 库  求MD5
def run():
    tmpCWD=os.getcwd()
    tmpWWW_Dir=input("Input WWW Dir:").replace('\r','').replace('\n','')
    os.chdir(tmpWWW_Dir)

    tmpCommand="python -m http.server 8000"
    print(tmpCommand)
    os.system(tmpCommand)

    os.chdir(os.getcwd())
    
    

if __name__=="__main__":
    run()
