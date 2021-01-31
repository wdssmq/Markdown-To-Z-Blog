---
title: 【折腾】VSCode中运行Python提示没有权限
tags:
- 折腾
- VSCode
- Python
categories:
- 未分类
---

虽然在微软商店可以方便的下载 Python，但是使用起来并不太方便 - -。

这里是一些探索，Docker For Windows 同理。

<!--more-->

简单说，在 Git bash 或 VSCode 终端里执行 Python 时会提示`Permission denied`，所以需要加`winpty`才行，还有个「应用执行别名」的选项可以按需设置。

```shell
python -V
# bash: /c/Users/****/AppData/Local/Microsoft/WindowsApps/python: Permission denied

winpty python -V
# Python 3.7.9
```
----------

好吧，，建议直接单独安装Python。。。商店版需要在 cmd 下使用。。

另外，关于VSCode中无法安装 autopep8 用于代码格式化。

提示类似这样：

> C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe: can't open file 'c:Userswdssm.vscodeextensionsms-python.python-2021.1.502429796pythonFilespyvsc-run-isolated.py': [Errno 2] No such file or directory

解决：在cmd中执行：

```bat
C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe C:\Users\wdssm\.vscode\extensions\ms-python.python-2021.1.502429796\pythonFiles\pyvsc-run-isolated.py pip install -U autopep8

C:\Users\wdssm\AppData\Local\Programs\Python\Python37\python.exe C:\Users\wdssm\.vscode\extensions\ms-python.python-2021.1.502429796\pythonFiles\pyvsc-run-isolated.py pip install -U pylint --user
```

需要按实际修改路径。

-------

↓这个东西在本地不知道怎么用，GitHub Actions 经过 30 多次尝试终于成功了。

```shell
pip install pipenv
pip install -p Pipfile.lock
```

最后，折腾过程中明明也解决了各种问题，然而又好像没有什么值得专门记录的。。
