import os
import sys
from . import Helper


def ShowReadme():
        Helper.ShowReadme("批量修改文件后缀，例如JPG改jpg\n输入文件夹路径")

def run():
        ShowReadme()
        tmpDirPath=""
        while os.path.isdir(tmpDirPath)==False:
                tmpDirPath=input(u"输入文件夹路径:")
                tmpDirPath=tmpDirPath.replace("\r","").replace("\n","")

        tmpOldExt=""
        while tmpOldExt=="":
                tmpOldExt=input(u"输入被替换的后缀 .JPG:")
                tmpOldExt=Helper.Remove_r_n(tmpOldExt)

        tmpNewExt=""
        while tmpNewExt=="":
                tmpNewExt=input(u"输入新的后缀 .jpg:")
                tmpNewExt=Helper.Remove_r_n(tmpNewExt)

        #遍历目录与子目录
        tmpFilePathList=Helper.list_all_files(tmpDirPath)
        for tmpOneFilePath in tmpFilePathList:
                if os.path.isfile(tmpOneFilePath) and tmpOneFilePath.endswith(tmpOldExt):
                        tmpNewFilePath=Helper.ChangePathExt(tmpOneFilePath,tmpNewExt)
                        print(tmpNewFilePath)
                        os.rename(tmpOneFilePath,tmpNewFilePath)

if __name__=="__main__":
    run()
