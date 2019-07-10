#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from Tools import Helper
import io
import os
try:
    from PIL import Image
except:
    Helper.InstallModule('Pillow')
    from PIL import Image

def Resize(varPath,varScale):
    tmpImage=Image.open(varPath)
    print("Image Size:"+str(tmpImage.width)+","+str(tmpImage.height))

    tmpWidth=tmpImage.width*varScale
    tmpHeight=tmpImage.height*varScale
    tmpImage.resize((int(tmpWidth),int(tmpHeight)),Image.ANTIALIAS).save(varPath)

def run():
    # print("to_JPG")

    tmpFilePath=str(input("Input PNG or dir Path:"))
    tmpFilePath=tmpFilePath.replace("\r","").replace("\n","").replace('"','')
    print('Convert '+tmpFilePath+':\n')

    tmpScaleStr=str(input("Input Scale eg:0.6:"))
    tmpScaleStr=Helper.Remove_r_n(tmpScaleStr)
    tmpScale=float(tmpScaleStr)

    if os.path.isdir(tmpFilePath):
        tmpFilePathList=Helper.list_all_files(tmpFilePath)
        for tmpOneFilePath in tmpFilePathList:
            Resize(tmpOneFilePath,tmpScale)

    elif os.path.isfile(tmpFilePath):
        Resize(tmpFilePath,tmpScale)

    



    print("Convert Finish!\n")

if __name__=="__main__":
    run()

        
