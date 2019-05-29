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

def run():
    # print("to_JPG")

    tmpFilePath=str(input("Input PNG or dir Path:"))
    tmpFilePath=tmpFilePath.replace("\r","").replace("\n","")
    print('Convert '+tmpFilePath+':\n')

    tmpScaleStr=str(input("Input Scale eg:0.6:"))
    tmpScaleStr=Helper.Remove_r_n(tmpScaleStr)
    tmpScale=float(tmpScaleStr)

    tmpImage=Image.open(tmpFilePath)
    print("Image Size:"+str(tmpImage.width)+","+str(tmpImage.height))

    tmpWidth=tmpImage.width*tmpScale
    tmpHeight=tmpImage.height*tmpScale
    tmpImage.resize((int(tmpWidth),int(tmpHeight)),Image.ANTIALIAS).save(tmpFilePath)



    print("Convert Finish!\n")

if __name__=="__main__":
    run()

        
