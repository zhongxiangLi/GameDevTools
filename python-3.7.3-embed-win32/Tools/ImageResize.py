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

    tmpNewSize=str(input("Input Size eg:100,100:"))
    tmpNewSize=Helper.Remove_r_n(tmpNewSize)
    tmpStrParts=tmpNewSize.partition(',')
    tmpWidth=int(tmpStrParts[0])
    tmpHeight=int(tmpStrParts[2])
    try:
        Image.open(tmpFilePath).resize((tmpWidth,tmpHeight),Image.ANTIALIAS).save(tmpFilePath)
    except:
        print(tmpFilePath+' not image or disk no space\n')


    print("Convert Finish!\n")

if __name__=="__main__":
    run()

        
