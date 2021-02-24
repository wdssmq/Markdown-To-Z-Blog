---
title: 【折腾】pip 安装各种依赖遇到的坑
tags:
- Python
- 折腾
categories:
- 电脑网络
id: 696
alias: 20210224781
---

2021-02-03：

然后折腾了一个新项目：[wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。")

2021-01-11：

坐标石家庄某县城，，看到个 py 项目想折腾一下。。

<!--more-->

[科技爱好者周刊（第 141 期）：封闭系统的胜利 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2021/01/weekly-issue-141.html "科技爱好者周刊（第 141 期）：封闭系统的胜利 - 阮一峰的网络日志")

> [ArtLine](https://github.com/vijishmadhavan/ArtLine "https://github.com/vijishmadhavan/ArtLine")
> 一个深度学习项目，将照片转为线条素描画，这里有可以运行的 [Demo](https://github.com/jwenjian/artline-demo)（Flask 应用）。（[@jwenjian](https://github.com/ruanyf/weekly/issues/1571) 投稿）

插件需要安装 `torch-1.6.0` 这个东西，然后大小有 974MB，命令行直接超时了，然后晚上挂机下载了回来（都没想到找个镜像源下载）。

```bash
# pip3 install torch==1.6.0 -f https://download.pytorch.org/whl/torch_stable.html

pip3 install torch*
```

然而还有其他依赖项下载，一个只有 13MB 的文件都卡住不动。。。 `npm` 和 `docker` 都折腾过的我这时终于想起来可以找个镜像源：

```bash
pip3 install torch* -i https://pypi.tuna.tsinghua.edu.cn/simple
```

期间遇到的各种错误提示：

> ModuleNotFoundError: No module named 'fastai'
> ModuleNotFoundError: No module named 'matplotlib'
> ModuleNotFoundError: No module named 'PIL'
> ModuleNotFoundError: No module named 'torchvision'
> ModuleNotFoundError: No module named 'cv2'
> ERROR: Could not find a version that satisfies the requirement torchvision===0.7.0


'PIL'需要安装 `Pillow`；

'torchvision'则因为默认源和镜像源都没有这个版本所以要另外指定，比较慢但好在文件不大。

'cv2'对应 `opencv-python`;

```bash
# python -m pip install -U wheel
pip3 install torchvision==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
pip3 install fastai==1.0.61 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
```

发现这篇笔记已经很难线性起来了。。以及，到底是谁说 py 项目需要的依赖比 Node 少的？

> error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

[Microsoft Visual C++ 14.0 is required 解决方法 - 知乎](https://zhuanlan.zhihu.com/p/126669852 "Microsoft Visual C++ 14.0 is required解决方法 - 知乎")


--------------------------------

```bash
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# ↑↑好像不能这么用？？↑↑
python app.py
```

---

过程内找到的一个镜像站，虽然实际并没有用上：

[https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/win-64/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/win-64/ "清华大学开源软件镜像站 | Tsinghua Open Source Mirror")

----

```py
base = os.path.split(os.path.realpath(__file__))[0]
# 修改当前工作目录
os.chdir(base)
print("当前工作目录为 %s" % os.getcwd())

path = Path(".")
```

