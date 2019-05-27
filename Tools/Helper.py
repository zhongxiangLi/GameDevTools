#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib 
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
    os.system('start '+tmpExePath)

# if __name__=="__main__":
    # DownLoad('http://pic.cnblogs.com/face/u337375.jpg','./u337375.jpg')

# 检查pip是否安装
def Checkpip():
    print("Checkpip")
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