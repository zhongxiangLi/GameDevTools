首先需要修改 python37._pth 文件，去掉 import site 的注释

```
python37.zip
.

# Uncomment to run site.main() automatically
import site #去掉这行前面的 # 注释

```


使用Python命令不同

安装版Python在任意文件夹均可执行，绿色版Python 只能在Python.exe 所在文件夹执行命令

安装版Python使用

```
python +命令
```

绿色版

```
python -m +命令
```


pip使用的不同

安装版

```
pip +命令
```

绿色版
```
python -m pip +命令
```

比如安装pyside2,需要在绿色版的文件夹右键打开命令行，然后执行下面命令

```
python -m pip install pyside2
```

