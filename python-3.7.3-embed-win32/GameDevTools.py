#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
print(os.getcwd())
os.chdir(os.getcwd())

from Tools import Helper
Helper.Checkpip()

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
from Tools import VisitFreeSoundEffect
from Tools import SqliteStudio_2_1_5
from Tools import putty
from Tools import GetStrSHA1
from Tools import GetStrBASE64
from Tools import BASE64_Decode
from Tools import UnityAssetStudio
from Tools import to_JPG
from Tools import GetMediBangPaintPro
from Tools import ImageResize
from Tools import ImageScale
from Tools import Audio_HZ_KBPS_Tools
from Tools import MergeVideo
from Tools import APKTools
from Tools.HarExport import HarExport
from Tools import Everything
from Tools import Shadowsocks
from Tools import Ex7z
from Tools import Archive7z
from Tools import Win32DiskImager
from Tools import PhpStudy
from Tools import CombineTxtToOneFile
from Tools import ProfilerLuaMemory
from Tools import FileZilla
from Tools import Postman


os.system("mode con cols=121 lines=35")

HarExport.Helper.ShowLogo("游戏开发 工具套装")

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
    UnicodeToChinese:[['unicode','gbk','chinese','\\u','url','urlencode','code','codec'],'Unicode 转 普通中文显示 \\u4eba\\u751f\\u82e6\\u77ed\\uff0cpy\\u662f\\u5cb8 人生苦短，py是岸'],

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

    # VisitFreeSoundEffect
    VisitFreeSoundEffect:[['visitfreesoundeffect','mp3','audio','wav','audio'],u'免费的音效网站'],

    # SqliteStudio_2_1_5
    SqliteStudio_2_1_5:[['sqlitestudio_2_1_5','db','sqlite3'],u'sqlite3管理软件'],

    # putty
    putty:[['putty','ssh'],u'远程Linux'],

    # SHA1
    GetStrSHA1:[['sha1hash'],u'sha1编码'],

    # Base64编码
    GetStrBASE64:[['base64encode'],u'Base64编码'],

    # Base64解码
    BASE64_Decode:[['base64decode'],u'Base64解码'],

    # AssetStudioGUI Unity 资源导出工具
    UnityAssetStudio:[['unityassetstudiogui','unitystudio','unityassetbundleexport'],u'Unity 资源导出工具'],

    # 转JPG工具 支持单文件与文件夹
    to_JPG:[['image conv','webp','bmp','jpg','png'],u'图片转JPG工具 支持单文件与文件夹'],


    # MediBangPaintPro
    GetMediBangPaintPro:[['medibangpaintpro','png','image editor','jpg','photoshop','texture','ps'],u'免费的图片编辑工具，替代Photoshop'],
    # 图片缩放工具
    ImageResize:[['imageresize','png','jpg'],u'图片缩放 指定尺寸'],

    # 图片缩放工具 指定比例
    ImageScale:[['imagerescale','png','jpg','resize'],u'图片缩放 指定比例'],

    # 音效格式转换工具 设置hz 比特率 
    Audio_HZ_KBPS_Tools:[['audio_hz_kbps_bits','mp3','ogg','wav'],u'音效格式转换工具 设置hz 比特率'],

    # 视频合并工具
    MergeVideo:[['mergevideo','combine','add','mp4','flv','wmv','mkv'],u'视频合并工具'],

    # APKTool APK反编译工具套装
    APKTools:[['apktools','adb','jdjui','aapt'],u'APK反编译工具套装'],

    # HarExport H5网页游戏资源提取
    HarExport:[['harexport','h5','html','web'],u'H5网页游戏资源提取'],

    # Everything 极速搜索电脑文件
    Everything:[['everything','find','search','file','dir','sousuo'],u'极速搜索电脑文件'],

    # Shadowsocks 代理 翻墙 VPN
    Shadowsocks:[['shadowsocks','vpn','fanqiang','daili','proxy'],u'代理 翻墙 VPN'],

    # Ex7z 7z lzma解压
    Ex7z:[['7z','zip','rar','lzma','jieyasuo'],u'7z lzma解压'],

    # Archive7z 7z lzma压缩
    Archive7z:[['7z','zip','rar','lzma','yasuo'],u'7z lzma压缩'],

    # Win32DiskImager IOS 写入ISO系统到U盘 树莓派安装系统 
    Win32DiskImager:[['win32diskimager','iso','shumeipai','raspberrypi','raspberry pi'],u'写入ISO系统到U盘 树莓派安装系统'],

    # phpStudy 2016版  集成最新的Apache+Nginx+LightTPD+PHP+MySQL+phpMyAdmin+Zend Optimizer+Zend Loader 官网 http://phpstudy.php.cn/wenda/407.html
    PhpStudy:[['phpstudy','Apache+Nginx+LightTPD+PHP+MySQL+phpMyAdmin+Zend Optimizer+Zend Loader'],u'phpStudy 2016版  集成最新的Apache+Nginx+LightTPD+PHP+MySQL+phpMyAdmin+Zend Optimizer+Zend Loader'],

    # CombineTxtToOneFile 合并文本到一个文件
    CombineTxtToOneFile:[['CombineTxtToOneFile',],u'合并文本到一个文件'],

    # ProfilerLuaMemory 获取一个lua 数据表所占用内存
    ProfilerLuaMemory:[['ProfilerLuaMemory',],u'获取一个lua 数据表所占用内存'],

    # FileZilla FTP SFTP 文件上传下载工具
    FileZilla:[['FileZilla® is a cross-platform FTP, SFTP, and FTPS client with a vast list of features, which supports Windows, Mac OS X, Linux, and more. ','download'],u'FTP SFTP 文件上传下载工具'],

    # Postman HTTP requests  Get Post Patch Delete Put Postman是google开发的一款功能强大的网页调试与发送网页HTTP请求工具
    Postman:[['Postman HTTP requests  Get Post Patch Delete Put',],u'google开发的一款功能强大的网页调试与发送网页HTTP请求工具'],
}

toolSets_old=toolSets
toolSets={}
# 反转
for tmpTool,tmpToolInfo in toolSets_old.items():
    for tmpOneKeyword in tmpToolInfo[0]:
        tmpOneKeyword=tmpOneKeyword.lower()#使用小写字母作为关键词检索
        if (tmpOneKeyword in toolSets)==False:
            toolSets[tmpOneKeyword]=[]
        toolSets[tmpOneKeyword].append(tmpTool)



# print(toolSets)
# print(toolSets[GetFileMD5])

# 第一次进入Choose 提示按回车返回Search
_Show_Choose_Tips=True

def searchKeyword(varKeyword):
    varKeyword=varKeyword.lower()#使用小写字母作为关键词检索

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
        
    tmpIndex=input("Choose:").replace('\r','').replace('\n','').replace(' ','')
    tmpIndexStr=str(tmpIndex).strip()
    
    if tmpIndexStr=="":
        sayHello()
    else:
        try:
            tmpIndex=int(tmpIndexStr)
            print("-------"+tmpTools_for_Search[tmpIndex].__name__+"-------")
            tmpTools_for_Search[tmpIndex].run()
        except ex:
            print(ex)
            sayHello()

def sayHello():
    tmpKeyword=input("Search:")
    tmpKeyword=tmpKeyword.rstrip('\r')

    if tmpKeyword.startswith(':'):
        print(u"识别为控制台命令\n")

        tmpBatPath=os.getcwd()+"/Tools/RunSystemCmd.bat"
        os.system("start "+tmpBatPath+" "+tmpKeyword[1:])
    else:
        searchKeyword(tmpKeyword)
    print('\n\n')
        
    sayHello()

if __name__=="__main__":
    print(u'tips:\n比如我想查找打图集工具，关键词 texturepacker。\n那么输入 texture 或者 pack 或者 tex ，只要输入关键词部分字母 即可查找。\n')
    sayHello()