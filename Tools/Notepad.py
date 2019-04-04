#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def run():
    tmpExePath=os.getcwd()+"/Tools/Notepad/Notepad.exe"
    # print(tmpExePath)
    os.system(tmpExePath)

if __name__=="__main__":
    run()
