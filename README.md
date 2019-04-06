# GameDevTools
游戏开发日常用到的工具集

将GameDevTools.bat 创建快捷方式 放到桌面就可以快速打开

# 搜索工具

比如我想查找打图集工具，关键词 texturepacker。
那么输入 texture 或者 pack 或者 tex ，只要输入关键词部分字母 即可查找。

输入工具序号，即可使用工具

# 新增工具
在GameDevTools.py 注册新的工具 与 关键字

```
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
}
```

# 更新日志

```
2019/4/6 新增SimpleDownload 单文件下载器，省的打开迅雷或者浏览器,关键词 ['http download','xunlei','xuanfeng','kuaiche','idm']

2019/4/6 新增GIMP 免费开源的图片编辑工具，替代Photoshop,关键词 ['gimp','png','image editor','jpg','photoshop','texture','ps']

2019/4/6 新增WinMerge 对比代码工具，也可以对比文件夹 文件，替代beyond compare,关键词 ['diff','beyond compare','winmerge']

2019/4/6 新增TextureMerger 打图集工具 提取自Egret,关键词 ['png','jpg','texturepacker','texturemerger']

2019/4/6 新增luac,关键词 ['luac','lua']

2019/4/6 新增lua,关键词 ['lua','LUA']

2019/4/6 新增PNG无损压缩工具 PNGoo_Win,关键词 ['png','compress','png compress','image','image compress','yasuo']

2019/4/4 新增文本编辑器 Notepad,关键词 ['txt','exe','edit','note','notepad','text']

2019/4/3 新增屏幕录制gif工具 ILCEcap,关键词 ['gif','screen','capture','rec','url','licecap','cap']
```
