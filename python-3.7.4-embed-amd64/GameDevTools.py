#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
print(os.getcwd())
os.chdir(os.getcwd())
import sys
import json
from Tools import ProfilerTime

ProfilerTime.BeginSample("import")
from Tools import Helper
#Helper.Checkpip()



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
from Tools import Postman
from Tools import ConvertLuaDicsToList
from Tools import FBX_Review
from Tools import Excel_to_lua
from Tools import puttygen
from Tools import QRcodeGen
from Tools import ChangeFileExt
from Tools import PVRTexTool
from Tools import PVRShaderEditor
from Tools import FilePathNotOnlyEnglish
from Tools import TextAnalysisTool
from Tools import GetMyIPLocation
from Tools import GetIPLocation
from Tools import mysql_to_lua
from Tools import GBK_to_UTF8
# from Tools import UpStr
# from Tools import LowerStr
from Tools import toolset

tmpInitCostTime=ProfilerTime.EndSample()

os.system("mode con cols=121 lines=35")

HarExport.Helper.ShowLogo("游戏开发 工具套装\n启动耗时:"+str(tmpInitCostTime))

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

    # Postman HTTP requests  Get Post Patch Delete Put Postman是google开发的一款功能强大的网页调试与发送网页HTTP请求工具
    Postman:[['Postman HTTP requests  Get Post Patch Delete Put',],u'google开发的一款功能强大的网页调试与发送网页HTTP请求工具'],

    # ConvertLuaDicsToList
    ConvertLuaDicsToList:[['ConvertLuaDicsToList'],u'转换Lua字典形式的数据表为数组形式数据表'],

    # FBX_Review 3d模型查看工具 Autodesk官方出品
    FBX_Review:[['FBX Review A cross-platform 3D model viewer,Open files in a variety of common 3D formats to help improve the speed of asset review: .zip, .abc* .fbx, .3ds, .obj, .dxf, .dae, .bvh, .htr, .trc, .asf, .amc, .c3d, .aoa, .mcd.'],u'3d模型查看工具 Autodesk官方出品'],

    # Excel_to_lua
    Excel_to_lua:[['Excel_to_lua'],u'Excel 转 lua'],

    # puttygen
    puttygen:[['puttygen is a RSA and DSA key generation utility','miyue','miyao','disable ssh use rsa key login'],u'生成RSA、DSA公钥私钥的密钥工具'],

    # QRcodeGen
    QRcodeGen:[['QRcodeGen','erweima'],u'生成二维码图片'],

    # QRcodeGen
    ChangeFileExt:[['ChangeFileExt','changefiletypeextension'],u'批量修改文件后缀，例如JPG改jpg'],

    # PVRTexTool
    PVRTexTool:[['PVRTexTool convert(encode/compress) images textures(png/jpg) to gpu texture format like pvr(etc/ast)','Mali Texture Compression Tool'],u'贴图压缩工具，PNG压缩成ETC、PVR等格式'],

    #PVRShaderEditor
    PVRShaderEditor:[['PVRShaderEditor is shader code editor,support code highlight,error check'],u'Shader代码编辑器，具有错误检查、代码高亮功能'],

    # FilePathNotOnlyEnglish
    FilePathNotOnlyEnglish:[['FilePathNotOnlyEnglish check chinese filename or other not english language character'],u'检测文件名或路径是否包含中文或其他非英文字符'],

    # TextAnalysisTool
    TextAnalysisTool:[['TextAnalysisTool.NET','android logcat search by tag'],u'看log神器，根据指定内容过滤'],

    # GetMyIPLocation
    GetMyIPLocation:[['get my compute ip address and gps location'],u'获取自己的外网IP以及所在地区位置'],

    # GetIPLocation
    GetIPLocation:[['get ip address/domain gps location'],u'获取IP/域名所在地区位置'],

    # mysql_to_lua
    mysql_to_lua:[['mysql_to_lua'],u'导出Mysql表数据为lua脚本'],

    #GBK_to_UTF8
    GBK_to_UTF8:[['GBK_to_UTF8 convert(encode) from gbk encoding to utf8'],u'转换文本文件编码GBK-->UTF8'],

    # # UpStr
    # UpStr:[['UpStr Converts characters(words)(string) to uppercase'],u'转换英文字符为全大写'],

    # # LowerStr
    # LowerStr:[['LowerStr Converts characters(words)(string) to lowercase'],u'转换英文字符为全小写'],
}

toolSets_old=toolSets
toolSets={}
# 反转,一个关键词 对应多个工具
for tmpTool,tmpToolInfo in toolSets_old.items():
    for tmpOneKeyword in tmpToolInfo[0]:
        tmpOneKeyword=tmpOneKeyword.lower()#使用小写字母作为关键词检索
        if (tmpOneKeyword in toolSets)==False:
            toolSets[tmpOneKeyword]=[]
        toolSets[tmpOneKeyword].append(tmpTool)

# print(toolSets)


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

    # 提取关键字对应的Tool,去重
    tmpTools_for_Search=[]
    for tmpOneKeyword in tmpKeyword_ContainsSearch:
        tmpTools=toolSets[tmpOneKeyword]
        for tmpTool in tmpTools:
            if tmpTool not in tmpTools_for_Search:
                tmpTools_for_Search.append(tmpTool)

    # print(tmpTools_for_Search)

    # 输出结果
    if len(tmpTools_for_Search)>0:
        print('\n----------------------------------------')
        for tmpIndex in range(len(tmpTools_for_Search)):
            tmpOneTool=tmpTools_for_Search[tmpIndex]
            print(str(tmpIndex)+":"+tmpOneTool.__name__+" -"+toolSets_old[tmpOneTool][1])
        print('----------------------------------------\n')

    #从toolset.json中 搜索
    tmpToolInfos_for_Search=[]
    toolsetjsonPath=os.getcwd()+"/Tools/toolset.json"
    toolsetjsonfile =open(toolsetjsonPath,encoding='utf-8') #打开json文件
    res=toolsetjsonfile.read()  #读文件
    toolsetArray=json.loads(res)
    # print(toolsetArray)#把json串变成python的数据类型：字典
    for tmpOneToolInfo in toolsetArray:
        # print(tmpOneToolInfo)
        tmpOneToolsInfo_KeywordArray=tmpOneToolInfo["keyword"]
        # print(tmpOneToolsInfo_KeywordArray)
        for tmpOneKeyword in tmpOneToolsInfo_KeywordArray:
            # print(tmpOneKeyword)
            if varKeyword in tmpOneKeyword.lower():
                # print("keyword find")
                tmpToolInfos_for_Search.append(tmpOneToolInfo)
                break

    if len(tmpToolInfos_for_Search)>0:
        print('\n----------------------------------------')
        for tmpIndex in range(len(tmpToolInfos_for_Search)):
            tmpOneToolInfo=tmpToolInfos_for_Search[tmpIndex]
            print(str(10+tmpIndex)+":"+tmpOneToolInfo["name"]+" -"+tmpOneToolInfo["desc"])
        print('----------------------------------------\n')


    if len(tmpTools_for_Search)==0 and len(tmpToolInfos_for_Search)==0:
        print("not found\n")
        return

    global _Show_Choose_Tips
    if _Show_Choose_Tips:
        print(u'\n直接按回车，可以返回Search')
        _Show_Choose_Tips=False
        
    tmpIndex=input("Choose:").replace('\r','').replace('\n','').replace(' ','')
    tmpIndexStr=str(tmpIndex).strip()
    
    if tmpIndexStr=="":
        sayHello()
    else:
        tmpIndex=int(tmpIndexStr)
        if tmpIndex>=10:
            tmpRealIndex=tmpIndex-10
            if tmpRealIndex>(len(tmpToolInfos_for_Search)-1):
                searchKeyword(varKeyword)
                return
            else:
                tmpOneToolInfo=tmpToolInfos_for_Search[tmpRealIndex]
                toolset.run(tmpOneToolInfo)
        else:
            if tmpIndex>(len(tmpTools_for_Search)-1):
                searchKeyword(varKeyword)
                return
            print("-------"+tmpTools_for_Search[tmpIndex].__name__+"-------")

            try:
                tmpTools_for_Search[tmpIndex].run()
            except:
                print("Unexpected error:", sys.exc_info())
                tmpTools_for_Search[tmpIndex].run()
        return
        
            
        



#统计现有linux命令
linuxcommands=Helper.list_all_file_name_in_one_dir(os.getcwd()+"/Tools/linuxcommand/usr/bin",".exe",True)
# print(linuxcommands)

# 运行Linux命令
def RunLinuxCmd(varKeyword):
    # tmpLinuxCommand=""
    tmpLinuxCommand=varKeyword[2:]
    tmpParts=tmpLinuxCommand.partition(' ')
    tmpLinuxCommand=str(tmpParts[0])

    print(u"识别为linux命令 "+tmpLinuxCommand+"\n")
    # 查找是否有这个命令对应的exe,Tools\linuxcommand\usr\bin这个目录里面
    if tmpLinuxCommand in linuxcommands:
        tmpBatPath=os.getcwd()+"/Tools/RunLinuxCmd.bat"
        os.system("start "+tmpBatPath+" "+varKeyword[2:])
    else:
        varSimilarStrList=Helper.GetSimilarStrsFromList(linuxcommands,tmpLinuxCommand)
        if len(varSimilarStrList)>0:
            print(u"错误，以下可用\n")
            print(varSimilarStrList)
        else:
            print(u"没有找到这个命令\n")

    
    

def sayHello():
    tmpKeyword=input("[Search]$")
    tmpKeyword=tmpKeyword.rstrip('\r')

    if tmpKeyword.startswith('::'):
        RunLinuxCmd(tmpKeyword)
    elif tmpKeyword.startswith(':'):
        print(u"识别为控制台命令\n")

        tmpBatPath=os.getcwd()+"/Tools/RunSystemCmd.bat"
        os.system("start "+tmpBatPath+" "+tmpKeyword[1:])
    else:
        searchKeyword(tmpKeyword)
    print('\n\n')
        
    sayHello()

if __name__=="__main__":
    print(u'tips:\n比如我想查找打图集工具，关键词 texturepacker。\n那么输入 texture 或者 pack 或者 tex ，只要输入关键词部分字母 即可查找。\n\n冒号+命令=Win命令，   :ping www.baidu.com  识别为ping命令\n2个冒号+命令=linux命令， ::ssh-keygen 识别为linux的ssh-keygen命令\n')
    
    sayHello()

    