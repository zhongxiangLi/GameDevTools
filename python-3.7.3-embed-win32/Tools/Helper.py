#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib 
import codecs
from urllib import request

# 不规范的Url 
STR_INVALID_URL='url begin with http:// or https://'

# 去除 \r \n
def Remove_r_n(varStr):
    tmpStr=str(varStr)
    return tmpStr.replace('\r','').replace('\n','')

# 检查Url是否以 https http 开头
def CheckUrl_Http_Https(varUrl):
    tmpUrl=varUrl
    if tmpUrl.startswith('http://') or  tmpUrl.startswith('https://'):
        return True
    else:
        return False

# 下载文件 返回 True False代表Url是否合法
def DownLoad(varUrl,varSavePath):
    if CheckUrl_Http_Https(varUrl):
        print(u"DownLoading:"+varUrl)
        varUrl=Remove_r_n(varUrl)
        request.urlretrieve(varUrl, varSavePath)
        return True
    else:
        print(STR_INVALID_URL)
        return False

def OpenOneToolDir(varDir):
    tmpExePath=os.getcwd()+"/Tools/"+varDir
    # print(tmpExePath)
    os.system('start explorer '+tmpExePath)

# 打开目录
def OpenDir(varDir):
    print("OpenDir:"+varDir)
    if ' ' in varDir:#目录有空格
        if varDir.startswith('"')==False:#目录非 双引号开头
            varDir='"'+varDir
        if varDir.endswith('"')==False:#目录非 双引号开头
            varDir=varDir+'"'
    os.system('start explorer '+varDir)


# if __name__=="__main__":
    # DownLoad('http://pic.cnblogs.com/face/u337375.jpg','./u337375.jpg')

# 检查pip是否安装
def Checkpip():
    # print("Checkpip")
    try:
        import pip
    except:
        print("pip not install,now intall...")
        os.system('python ./Tools/Depends/get-pip.py')

# 安装模块
def InstallModule(varModuleName):
    print("Pillow not install,now intall...")
    os.system('pip install '+varModuleName)
    print('Pillow install finish')

# 获取目录文件列表 包括子目录
def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

def getUnixPath(varpath):
    return varpath.replace('\\\\','/').replace('\\','/')

def getWinPath(varpath):
    varpath=varpath.replace('//','\\\\').replace('/','\\\\')

    tmpNewPath=""
    for tmpIndex in range(len(varpath)):
        if (tmpIndex>0 and varpath[tmpIndex-1]!='\\') and varpath[tmpIndex]=='\\' and (tmpIndex<(len(varpath)-1) and varpath[tmpIndex+1]!='\\'):
            tmpNewPath=tmpNewPath+'\\'
        tmpNewPath=tmpNewPath+varpath[tmpIndex]

    return tmpNewPath


# 从文件路径 获取文件夹路径
def getdirpath(varfilepath):
    varfilepath=getUnixPath(varfilepath)
    tmpStrParts=varfilepath.rpartition('/')
    return tmpStrParts[0]+'/'
# Checkpip()

# 显示Logo
def ShowLogo(varToolTitle):
    with codecs.open("./data.bin","r","utf-8",errors='ignore') as tmpLogoFile:
        print(tmpLogoFile.read())
    print(varToolTitle)
    print("\n\n")

# 获取文件所在文件夹
def GetDirFromPath(varPath):
    return os.path.split(varPath)[0]

# 获取父目录 文件的父目录就是文件所在目录 目录的父目录就是上一层目录
def GetParentDirFromPath(varPath):
    if os.path.isdir(varPath):
        return os.path.dirname(os.path.dirname(varPath))
    else:
        return GetDirFromPath(varPath)

# 获取文件名带后缀
def GetFileNameFromPath(varPath):
    return os.path.split(varPath)[1]

# 获取文件名不带后缀
def GetFileNameWithoutExtFromPath(varPath):
    tmpFileName=os.path.split(varPath)[1]
    return os.path.splitext(tmpFileName)[0]

# 获取文件名后缀
def GetFileExtFromPath(varPath):
    return os.path.splitext(varPath)[1]

# 替换文件名后缀 .7z
def ChangePathExt(varPath,varExt):
    tmpFilePath,tmpExt=os.path.splitext(varPath)
    return tmpFilePath+varExt

# 7z解压,传入7z文件路径，解压目录
def Ex_7z(var7zFilePath,varOpenDir=True):
    tmpPath=var7zFilePath.replace('"','')

    tmp7zExePath=os.getcwd()+"/Tools/7z/7za.exe"
    tmpExDirPath=GetDirFromPath(tmpPath)
    tmpCommand=tmp7zExePath+" x \""+tmpPath+"\" -o\""+tmpExDirPath+"\""
    print(tmpCommand)
    os.system(tmpCommand)
    if varOpenDir:
        OpenDir(tmpExDirPath)

# 7z压缩,传入目录
def Archive_7z(varPath=""):
    print("path:" + varPath+"\n")
    tmp7zExePath=os.getcwd()+"/Tools/7z/7za.exe"

    tmpPath=varPath.replace('"','')
    if os.path.isdir(tmpPath):
        print("is dir\n")
        if tmpPath.endswith('/') or tmpPath.endswith('\\'):
            tmpPath=tmpPath[0:-1]
            if tmpPath.endswith('/') or tmpPath.endswith('\\'):
                tmpPath=tmpPath[0:-1]
        print(tmpPath)

        
        tmp7zFilePath=ChangePathExt(tmpPath,".7z")
        tmp7zFileDirPath=GetDirFromPath(tmp7zFilePath)
        tmpCommand=tmp7zExePath+" a -t7z \""+tmp7zFilePath+"\" \""+tmpPath+"\"\\ -r -mx=9 -m0=LZMA2 -ms=10m -mf=on -mhc=on -mmt=on"
        print(tmpCommand)
        os.system(tmpCommand)
        OpenDir(tmp7zFileDirPath)
    elif os.path.isfile(tmpPath):
        print("is file\n")
        tmp7zFilePath=ChangePathExt(varPath,".7z")
        tmp7zFileDirPath=GetDirFromPath(tmp7zFilePath)
        tmpCommand=tmp7zExePath+" a -t7z \""+tmp7zFilePath+"\" \""+tmpPath+"\" -r -mx=9 -m0=LZMA2 -ms=10m -mf=on -mhc=on -mmt=on"
        print(tmpCommand)
        os.system(tmpCommand)
        OpenDir(tmp7zFileDirPath)


# 读取Txt,返回字符串
def ReadTxtFileToStr(varTxtFilePath,varIgnore=False):
    if varIgnore:
        tmpTxtFile=codecs.open(varTxtFilePath,"r","utf-8",errors='ignore')
    else:
        tmpTxtFile=codecs.open(varTxtFilePath,"r","utf-8")
    
    tmpStr=tmpTxtFile.read()
    tmpTxtFile.close()
    return tmpStr

# 读取Txt,一行一行 返回数组
def ReadTxtAllLineToArray(varFilePath,varIgnore=False):
    if varIgnore:
        tmpTxtFile=codecs.open(varFilePath,"r","utf-8",errors='ignore')
    else:
        tmpTxtFile=codecs.open(varFilePath,"r","utf-8")
    tmpLines=tmpTxtFile.readlines()
    tmpLines.extend("\n")
    tmpTxtFile.close()
    return tmpLines

# 将字符串写入一个Txt
def WriteStrToTxtFile(varStr,varTxtFilePath):
    tmpTxtFile=codecs.open(varTxtFilePath,"w","utf-8",errors='ignore')
    tmpTxtFile.write(varStr)
    tmpTxtFile.close()

# 将字符串数组写入到一个Txt
def WriteLineArrayToTxtFile(varLineArray,varTxtFilePath):
    for tmpIndex in range(len(varLineArray)):
        varLineArray[tmpIndex]=Remove_r_n(varLineArray[tmpIndex])+"\n"
    tmpTxtFile=codecs.open(varTxtFilePath,"w","utf-8",errors='ignore')
    tmpTxtFile.writelines(varLineArray)
    tmpTxtFile.close()

# 合并一个文件夹的文本 到一个文本里，以文件夹名字命名，存放在文件夹同层目录。
# 例如合并 C:/WorkSpace/Data 所有 lua 到 C:/WorkSpace/Data.lua。
def CombineTxtToOneFile(varDirPath,varFileType):
    tmPath=varDirPath
    tmPath=tmPath.replace("\r","").replace("\n","")


    tmpFileType=varFileType
    tmpFileType=tmpFileType.replace("\r","").replace("\n","")

    tmpCombineLineArray=[]

    if os.path.isdir(tmPath):
        tmPath=tmPath+"/"
        tmpFilePathList=list_all_files(tmPath)
        for tmpOneFilePath in tmpFilePathList:
            if tmpOneFilePath.endswith(tmpFileType):
                # print(u"[读取] "+tmpOneFilePath)
                tmpOneTxtLines=ReadTxtAllLineToArray(tmpOneFilePath)
                tmpCombineLineArray.extend(tmpOneTxtLines)

    elif os.path.isfile(tmPath):
        # print(u"路径错误，请输入文件夹路径\n")
        return

    
    # print(tmpCombineLineArray)

    tmpCombineTxtFilePath=os.path.dirname(tmPath)+varFileType

    WriteLineArrayToTxtFile(tmpCombineLineArray,tmpCombineTxtFilePath)

    # print(u"保存到:"+tmpCombineTxtFilePath)

    return tmpCombineTxtFilePath

def ShowReadme(varStr):
    print(u"软件使用说明："+varStr+"\n")