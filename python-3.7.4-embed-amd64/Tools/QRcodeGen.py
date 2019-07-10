import os
import sys
from . import Helper
import qrcode
from PIL import Image
import matplotlib.pyplot as plt

def run():
        
        
        tmpStr=""
        while tmpStr=="":
                tmpStr=input(u"输入内容:")
                
                tmpStr=tmpStr.replace("\r","").replace("\n","")
        
        
        tmpImagePath=Helper.GetCacheDir_FilePath("qrcodegen.png")
        print(u"二维码图片保存在:"+tmpImagePath)
        img = qrcode.make(tmpStr)
        img.save(tmpImagePath)

        img=Image.open(tmpImagePath)
        plt.imshow(img)
        plt.show()
        # img.show()

if __name__=="__main__":
    run()
