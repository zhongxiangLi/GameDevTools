#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper


def run():
    tmpZipFilePath=os.getcwd()+"/Tools/Imagination/PowerVR_Graphics/PowerVR_Tools/PVRTexTool.7z"
    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    # print(tmpZipFilePath)
    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath)==False:
        # 先解压
        print(u"第一次打开，先解压\n")
        Helper.Ex_7z(tmpZipFilePath,False)
        print(u"解压完成\n")

    tmpExePath='"'+os.getcwd()+"\\Tools\\Imagination\\PowerVR_Graphics\\PowerVR_Tools\\PVRTexTool\\Start.bat"+'"'
    #print(tmpExePath)
    Helper.ShowReadme(u"PVRTexTool取自Imagination PowerVR Tools and SDK 开发者工具包。\n更多工具请访问https://www.imgtec.com/developers/powervr-sdk-tools/installers/\n第一次使用请看说明文档\n"+os.getcwd()+u"\\Tools\\Imagination\\PowerVR_Graphics\\PowerVR_Tools\\PVRTexTool\\PVRTexTool使用说明.pdf")
    # Helper.OpenOneToolDir("Win32DiskImager/Win32DiskImager/")
    os.system(tmpExePath)
    

if __name__=="__main__":
    run()
