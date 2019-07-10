#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json

class Item:
    object_id=0
    object_name=""
    object_icon=""
    color=0
    object_type=0
    object_rank=0
    profession=0
    stacklimit=0
    usedlevel=0
    sellid=0
    sellgold=0
    auction=0
    use_type=0
    result=0
    describe=""
    buynumber=0
    price=0
    time=0
    usenumber=0
    shortcut=0

    def toDic(self):
        return self.__dict__

def CreateNormalKeyValueJson():
    tmpDic={}
    for index in range(100000):
        tmpItem=Item()
        tmpItem.object_id=index
        tmpItem.object_name="name"+str(index)
        tmpItem.object_icon="icon"+str(index)
        tmpItem.color=index
        tmpItem.object_type=index
        tmpItem.object_rank=index
        tmpItem.profession=index
        tmpItem.stacklimit=index
        tmpItem.usedlevel=index
        tmpItem.sellid=index
        tmpItem.sellgold=index
        tmpItem.auction=index
        tmpItem.use_type=index
        tmpItem.result=index
        tmpItem.describe="describe"+str(index)
        tmpItem.buynumber=index
        tmpItem.price=index
        tmpItem.time=index
        tmpItem.usenumber=index
        tmpItem.shortcut=index
        tmpDic[index]=tmpItem.toDic()

    tmpJson=json.dumps(tmpDic)

    # 写文件
    with open(os.getcwd()+"/test_normal.json", "wt") as out_file:
        out_file.write(tmpJson)
        out_file.close()

def CreateArrayJson():
    tmpDic={}

    tmpValues=[]
    for index in range(100000):
        tmpItem=Item()
        tmpItem.object_id=index
        tmpItem.object_name="name"+str(index)
        tmpItem.object_icon="icon"+str(index)
        tmpItem.color=index
        tmpItem.object_type=index
        tmpItem.object_rank=index
        tmpItem.profession=index
        tmpItem.stacklimit=index
        tmpItem.usedlevel=index
        tmpItem.sellid=index
        tmpItem.sellgold=index
        tmpItem.auction=index
        tmpItem.use_type=index
        tmpItem.result=index
        tmpItem.describe="describe"+str(index)
        tmpItem.buynumber=index
        tmpItem.price=index
        tmpItem.time=index
        tmpItem.usenumber=index
        tmpItem.shortcut=index
        tmpItemDic={}
        tmpItemDic=tmpItem.toDic()
        tmpValues.append(list(tmpItemDic.values()))

        if index==0:
            tmpKeyList=list(tmpItemDic.keys())
            tmpKeyDic={}
            for tmpKeyIndex in range(len(tmpKeyList)):
                tmpKey=tmpKeyList[tmpKeyIndex]
                tmpKeyDic[tmpKey]=tmpKeyIndex
            tmpDic["key"]=tmpKeyDic

    tmpDic["value"]=tmpValues
    tmpJson=json.dumps(tmpDic)

    # 写文件
    with open(os.getcwd()+"/test_array.json", "wt") as out_file:
        out_file.write(tmpJson)
        out_file.close()


#使用python 库  求MD5
def run():
    CreateArrayJson()


if __name__=="__main__":
    run()
