import os
import sys
from . import Helper


def ShowReadme():
        Helper.ShowReadme("检测文件名或路径是否包含中文或其他非英文字符\n输入文件夹路径")

def run():
        ShowReadme()
        tmpDirPath=""
        while os.path.isdir(tmpDirPath)==False:
                tmpDirPath=input(u"输入文件夹路径:")
                tmpDirPath=tmpDirPath.replace("\r","").replace("\n","")


        #遍历目录与子目录
        tmpFilePathList=Helper.list_all_files(tmpDirPath)
        for tmpOneFilePath in tmpFilePathList:
                if Helper.StringOnlyEnglish(tmpOneFilePath)==False:
                        print(tmpOneFilePath)


if __name__=="__main__":
    run()
