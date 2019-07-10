#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper

def run():
    Helper.ShowReadme("点击Generate生成之后，鼠标要在窗口上面的空白地方 移动，不然进度条就不会走。")
    tmpExePath=os.getcwd()+"/Tools/putty/puttygen.exe"
    # print(tmpExePath)
    os.system("start " + tmpExePath)

if __name__=="__main__":
    run()
