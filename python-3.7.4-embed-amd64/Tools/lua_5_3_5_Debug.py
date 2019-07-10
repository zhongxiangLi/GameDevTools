#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def run():
    tmpExePath=os.getcwd()+"/Tools/lua.5.3.5.Debug"
    # print(tmpExePath)
    os.system('start '+tmpExePath)

if __name__=="__main__":
    tmpExePath=os.getcwd()
    os.system('start '+os.getcwd())
