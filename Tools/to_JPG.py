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

def convert_one(varFilePath):
    print('Convert '+varFilePath+':\n')
    tmpJpgPath=varFilePath[:-4]+'.jpg'
    print('Save:'+tmpJpgPath+'\n')
    try:
        Image.open(varFilePath).convert('RGB').save(tmpJpgPath)
    except:
        print(varFilePath+' not image or disk no space\n')

def run():
    # print("to_JPG")

    tmpFilePath=str(input("Input PNG or dir Path:"))
    tmpFilePath=tmpFilePath.replace("\r","").replace("\n","")
    # print('Convert '+tmpFilePath+':\n')
    
    if os.path.isdir(tmpFilePath):
        tmpFilePathList=Helper.list_all_files(tmpFilePath)
        for tmpOneFilePath in tmpFilePathList:
            convert_one(tmpOneFilePath)
    elif os.path.isfile(tmpFilePath):
        convert_one(tmpFilePath)


    print("Convert Finish!\n")

if __name__=="__main__":
    run()

        
