#!/usr/bin/python
# -*- coding: UTF-8 -*-

import binascii
import codecs

def hexToStr(varHexStr):
    # print(varHexStr)
    if '\\u' in varHexStr:
        return varHexStr

    if '\\x' in varHexStr:
        tmpHexStr=varHexStr.replace("'",'').replace('"','').replace('\r','').replace('\n','').replace('\\x','')
        return binascii.unhexlify(tmpHexStr.encode("utf-8")).decode('utf8')
    # if '\\u' in varHexStr:
    #     return varHexStr
    #     tmpStr_Unicode=varHexStr.replace('\r','').replace('\n','')
    #     return tmpStr_Unicode.encode('utf-8').decode("unicode_escape")
    return varHexStr

def run():
    tmpHarFilePath=str(input(u"输入txt文件路径:")).replace('"','')
    with codecs.open(tmpHarFilePath,"r","utf-8",errors='ignore') as tmpHarFile:
        tmpContentStr=tmpHarFile.read()

        # 按 , 切割
        tmpHexSentenceArr=tmpContentStr.split(',')

        tmpWordSentenceArr={}
        tmpIndex=0
        for tmpHexSentence in tmpHexSentenceArr:
            # print(hexToStr(tmpHexSentence))
            tmpWordSentenceArr["__Ox3fa21["+str(hex(tmpIndex))+"]"]=hexToStr(tmpHexSentence)
            tmpIndex=tmpIndex+1
            

        print(tmpWordSentenceArr)
        f=open("test.txt",'w')
        f.write(str(tmpWordSentenceArr))
        f.close()



if __name__=="__main__":
    run()
