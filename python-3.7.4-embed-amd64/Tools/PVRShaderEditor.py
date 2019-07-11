#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from . import Helper


def run():
    tmpZipFilePath=os.getcwd()+"/Tools/Imagination/PowerVR_Graphics/PowerVR_Tools/PVRShaderEditor.7z"
    tmpZipFilePath=tmpZipFilePath.replace('\\','/')
    # print(tmpZipFilePath)
    tmpTargetDirPath=os.path.splitext(tmpZipFilePath)[0]
    if os.path.isdir(tmpTargetDirPath)==False:
        # 先解压
        print(u"第一次打开，先解压\n")
        Helper.Ex_7z(tmpZipFilePath,False)
        print(u"解压完成\n")

    tmpExePath='"'+os.getcwd()+"\\Tools\\Imagination\\PowerVR_Graphics\\PowerVR_Tools\\PVRShaderEditor\\Start.bat"+'"'
    #print(tmpExePath)
    Helper.ShowReadme(u"PVRShaderEditor取自Imagination PowerVR Tools and SDK 开发者工具包。\n更多工具请访问https://www.imgtec.com/developers/powervr-sdk-tools/installers/")
    # Helper.OpenOneToolDir("Win32DiskImager/Win32DiskImager/")
    os.system(tmpExePath)
    

if __name__=="__main__":
    run()
