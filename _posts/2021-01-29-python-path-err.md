---
title: 【折腾】Python + GitHub Actions 更新 Z-Blog 的探索
tags:
- 折腾
- VSCode
- Python
- GitHub
- Z-Blog
categories:
- 未分类
---

起因是看到了这个项目：

> zhaoolee/WordPressXMLRPCTools: 用 Hexo 的方式管理 WordPress
> https://github.com/zhaoolee/WordPressXMLRPCTools

想着给 Z-Blog 也弄个，然而 ZB 的`XML-RPC`接口是残缺的，然后即将发布的 1.7 版本将自带 API。就走 API 来做了，，然而问题是 1.7 什么时候发布？

折腾过程中明明也解决了各种问题，然而做不到每一个点都整理记录，也是略惆怅。。

<!--more-->

------------

因为最近又重装了系统，Python 什么的要重新安装。。

【【重装前也有折腾一个 Python 项目，将图片变成素描风什么的，对于我来说是没啥用的功能，而且实际弄出来和演示效果差的有点多】】

【【姑且也有份折腾笔记，正好可以用现在这个工具发布出来】】

虽然在微软商店可以方便的下载 Python，但是使用起来并不太方便 - -。

这里是一些探索，Docker For Windows 同理。

简单说，在 Git bash 或 VSCode 终端里执行 Python 时会提示`Permission denied`，所以需要加`winpty`才行，还有个「应用执行别名」的选项可以按需设置。

```shell
python -V
# bash: /c/Users/****/AppData/Local/Microsoft/WindowsApps/python: Permission denied

winpty python -V
# Python 3.7.9
```

**好吧，，建议直接单独安装 Python。。。商店版基本只能在 cmd 下使用，，pip 啥的各种麻烦。**

----------

另外，关于 VSCode 中无法安装 autopep8 用于代码格式化。

提示类似这样：

> C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe: can't open file 'c:Userswdssm.vscodeextensionsms-python.python-2021.1.502429796pythonFilespyvsc-run-isolated.py': [Errno 2] No such file or directory

解决：在 cmd 中执行：

```bat
C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe C:\Users\wdssm\.vscode\extensions\ms-python.python-2021.1.502429796\pythonFiles\pyvsc-run-isolated.py pip install -U autopep8

C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe C:\Users\wdssm\.vscode\extensions\ms-python.python-2021.1.502429796\pythonFiles\pyvsc-run-isolated.py pip install -U pylint --user
```

需要按实际修改路径。

---------

↓这个东西在本地不知道怎么用，GitHub Actions 经过 30 多次尝试终于成功了。

```shell
pip install pipenv
pip install -p Pipfile.lock
```

-----------

Github Actions 里获取文件真实修改时间的探索：

[GIT 获取文件最初创建及最新修改日期 · Issue #69 · Dream4ever/Knowledge-Base](https://github.com/Dream4ever/Knowledge-Base/issues/69 "GIT 获取文件最初创建及最新修改日期 · Issue #69 · Dream4ever/Knowledge-Base")

```shell
_cache_logs="_cache_logs.json"
          echo  "{" > ${_cache_logs};
          git ls-tree -r --name-only HEAD | while read filename; do
          if [ "${filename##*.}"x = "md"x ];then
          echo "\"$(git log -1 --pretty=format:"%at" -- $filename)\": \"$filename\",";
          echo "\"$(git log -1 --pretty=format:"%at" -- $filename)\": \"$filename\"," >> ${_cache_logs};
          fi
          done
          echo  "\"0\":\"README.md\"" >> ${_cache_logs};
          echo  "}" >> ${_cache_logs};
#
```


另一些探索：

```shell
# _test="aaa"
export _test="aaa"
python test.py
# import os
# print(os.environ["_test"])
```

> bash: ${var}: ambiguous redirect
