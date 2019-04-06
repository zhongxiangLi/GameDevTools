#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tools import GetFileMD5
from Tools import GetStrMD5
from Tools import GetUnixTimeStamp
from Tools import GetUnixTimeStamp_ms
from Tools import MultiSizeIcon
from Tools import HttpServer
from Tools import CheckServerPortOpen
from Tools import UnZipTools
from Tools import UnicodeToChinese
from Tools import ScreenCaptureGif
from Tools import Notepad
from Tools import PNGoo_Win
from Tools import lua_5_3_5_Debug
from Tools import luac_5_3_5_Debug
from Tools import TextureMerger
from Tools import GetGIMP
from Tools import WinMerge
from Tools import GetBigJPG
from Tools import SimpleDownload

toolSets=\
{
    # 注册程序 与 关键字，关键字有多个
    # Module:[['keyword1','keyword2'],'注释'],

    # 获取文件MD5
    GetFileMD5:[['md5','file md5','file'],u'获取文件MD5'],

    # 获取字符串MD5
    GetStrMD5:[['md5','string md5','string','str md5'],u'获取字符串MD5'],

    # 获取 10位 Unix时间戳 单位秒
    GetUnixTimeStamp:[['unix','time','timestamp'],u'获取 10位 Unix时间戳 单位秒'],

    # 获取 13位 Unix时间戳 单位毫秒
    GetUnixTimeStamp_ms:[['unix','time','timestamp','ms'],u'获取 13位 Unix时间戳 单位毫秒'],

    # 一键生成Android、IOS 多尺寸Icon
    MultiSizeIcon:[['icon','icon size'],u'一键生成Android、IOS 多尺寸Icon'],

    # 简单http服务器
    HttpServer:[['http','httpserver','http server'],u'简单http服务器'],

    # telnet 测试端口是否开启
    CheckServerPortOpen:[['telnet','checkserverportopen','port','network','server','net'],u'测试端口是否开启'],

    # 解压ZIP
    UnZipTools:[['zip','unzip','extra','extract'],u'解压ZIP'],

    # Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸
    UnicodeToChinese:[['unicode','gbk','chinese','\u','url','urlencode','code','codec'],u'Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸'],

    # 屏幕录制Gif
    ScreenCaptureGif:[['gif','screen','capture','rec','url','licecap','cap'],u'屏幕录制Gif'],

    # Notepad 文本编辑器
    Notepad:[['txt','exe','edit','note','notepad','text'],u'文本编辑器'],

    # PNGoo PNG无损压缩
    PNGoo_Win:[['png','compress','png compress','image','image compress','yasuo'],u'PNG无损压缩'],

    # lua.5.3.5.Debug
    lua_5_3_5_Debug:[['lua','LUA'],u'lua.5.3.5.Debug'],

    # luac.5.3.5.Debug
    luac_5_3_5_Debug:[['luac','lua'],u'lua5.3.5编译字节码工具 Debug版本'],

    # TextureMerger
    TextureMerger:[['png','jpg','texturepacker','texturemerger'],u'打图集工具 提取自Egret'],

    # GIMP
    GetGIMP:[['gimp','png','image editor','jpg','photoshop','texture','ps'],u'免费开源的图片编辑工具，替代Photoshop'],

    # WinMerge
    WinMerge:[['diff','beyond compare','winmerge'],u'对比代码工具，也可以对比文件夹 文件，替代beyond compare'],

    # GetBigJPG
    GetBigJPG:[['imagescale','bigjpg','ai'],u'AI人工智能图片放大'],

    # SimpleDownload
    SimpleDownload:[['http download','xunlei','xuanfeng','kuaiche','idm'],u'单文件下载器，省的打开迅雷或者浏览器'],
}

toolSets_old=toolSets
toolSets={}
# 反转
for tmpTool,tmpToolInfo in toolSets_old.items():
    for tmpOneKeyword in tmpToolInfo[0]:
        if toolSets.has_key(tmpOneKeyword)==False:
            toolSets[tmpOneKeyword]=[]
        toolSets[tmpOneKeyword].append(tmpTool)



# print(toolSets)
# print(toolSets[GetFileMD5])

# 第一次进入Choose 提示按回车返回Search
_Show_Choose_Tips=True

def searchKeyword(varKeyword):
    # 先提取所有Keyword
    tmpAllKeyword=toolSets.keys()
    # 然后提取包含 搜索字的 关键词
    tmpKeyword_ContainsSearch=[]
    for tmpOneKeyword in tmpAllKeyword:
        if varKeyword in tmpOneKeyword:
            tmpKeyword_ContainsSearch.append(tmpOneKeyword)

    if len(tmpKeyword_ContainsSearch)==0:
        print("not found")
        return

    # 提取关键字对应的Tool,去重
    tmpTools_for_Search=[]
    for tmpOneKeyword in tmpKeyword_ContainsSearch:
        tmpTools=toolSets[tmpOneKeyword]
        for tmpTool in tmpTools:
            if tmpTool not in tmpTools_for_Search:
                tmpTools_for_Search.append(tmpTool)

    # 输出结果
    print('\n----------------------------------------')
    for tmpIndex in range(len(tmpTools_for_Search)):
        tmpOneTool=tmpTools_for_Search[tmpIndex]
        print(str(tmpIndex)+":"+tmpOneTool.__name__+" -"+toolSets_old[tmpOneTool][1])
    print('----------------------------------------\n')

    global _Show_Choose_Tips
    if _Show_Choose_Tips:
        print(u'\n直接按回车，可以返回Search')
        _Show_Choose_Tips=False
        
    tmpIndex=raw_input("Choose:").replace('\r','').replace('\n','').replace(' ','')
    tmpIndexStr=str(tmpIndex).strip()
    
    if tmpIndexStr=="":
        sayHello()
    else:
        try:
            tmpIndex=int(tmpIndexStr)
            print("-------"+tmpTools_for_Search[tmpIndex].__name__+"-------")
            tmpTools_for_Search[tmpIndex].run()
        except:
            sayHello()

def sayHello():
    tmpKeyword=raw_input("Search:")
    searchKeyword(tmpKeyword.rstrip('\r'))
    print('\n\n')
        
    sayHello()

if __name__=="__main__":
    print(u'tips:\n比如我想查找打图集工具，关键词 texturepacker。\n那么输入 texture 或者 pack 或者 tex ，只要输入关键词部分字母 即可查找。\n')
    sayHello()