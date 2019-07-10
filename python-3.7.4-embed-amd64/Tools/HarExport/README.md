# HarExport

提取Har资源，用来提取H5网页游戏素材资源。

har 是firefox等浏览器用来保存网络访问数据的json文件。

所有访问的网络请求，以request response保存。

图片等文件以Base64保存。

这里的代码功能就是从base64数据还原文件。

首先需要安装 <font color=red>python3</font>

<font color=red>1.保存har文件</font>

![avatar](./image/1.png)

打开游戏页面

F12 打开开发者工具，切换到 <font color=red>网络</font> 一栏

确保选择 <font color=red>所有</font>

玩一段时间游戏

在 HAR 这里点击，选择 <font color=red>所有文件另存为HAR</font>，弹出提示框保存即可。


<font color=red>2.提取图片素材</font>

在当前目录打开命令行，执行命令
    
    python HarExport.py

提示输入har 文件路径，把har 文件拖到 CMD 窗口，回车即可

![avatar](./image/2.png)

文件提取按照url分段 存到指定文件夹。

比如这张图片

    "url": "https://res1.t5game.5jli.com/t5game_res/img/bg.jpg?v=1558085555",

就存储在

![avatar](./image/3.png)



