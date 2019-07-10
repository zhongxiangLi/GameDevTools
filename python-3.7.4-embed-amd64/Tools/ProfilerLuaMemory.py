#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
from Tools import Helper
import io
import os



def run():
    # print("to_JPG")
    print(u"检测一个Lua数据表占用的内存\nlua文件不能太大，90m的文件就会出错，可以分成多个文件.\n\n")

    tmPath=str(input(u"输入lua路径:"))
    tmPath=tmPath.replace("\r","").replace("\n","")

    tmpBeginLines=["collectgarbage(\"collect\")\n","local profilerLuaMemory_beginmemory=collectgarbage(\"count\")\n"]

    tmpEndLines=["local profilerLuaMemory_endmemory=collectgarbage(\"count\")","print(profilerLuaMemory_endmemory-profilerLuaMemory_beginmemory)"]

    tmpOneTxtLines=Helper.ReadTxtAllLineToArray(tmPath)

    tmpBeginLines.extend(tmpOneTxtLines)
    tmpBeginLines.extend(tmpEndLines)

    tmpLuaFilePath=os.getcwd()+"/Tools/lua.5.3.5.Debug/tmp.lua"

    Helper.WriteLineArrayToTxtFile(tmpBeginLines,tmpLuaFilePath)


    tmpLuaExeFilePath=os.getcwd()+"/Tools/lua.5.3.5.Debug/lua.exe"

    tmpCommand=tmpLuaExeFilePath+" "+tmpLuaFilePath
    # print(tmpCommand)

    # 打开lua 并传递 lua文件路径
    os.system(tmpCommand)

if __name__=="__main__":
    run()

        
