import codecs
import os

def ShowLogo(varToolTitle):

    

    with codecs.open("./data.bin","r","utf-8",errors='ignore') as tmpLogoFile:
        print(tmpLogoFile.read())
    print(varToolTitle)
    print("\n\n")

def OpenOneToolDir(varDir):
    tmpExePath=os.getcwd()+"/Tools/"+varDir
    # print(tmpExePath)
    os.system('start '+tmpExePath)