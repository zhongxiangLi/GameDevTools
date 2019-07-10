#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def run():
    tmpExePath=os.getcwd()+"/Tools/putty/puttygen.exe"
    # print(tmpExePath)
    os.system("start " + tmpExePath)

if __name__=="__main__":
    run()
