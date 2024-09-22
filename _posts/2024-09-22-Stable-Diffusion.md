---
title: 「折腾」落后两年的 Stable Diffusion 搭建笔记
date: 2024-08-31 15:00:53
tags:
 - Python
 - AI_生图
categories:
 - 电脑网络
id: 685
alias: 20220812894
---

### 开场跑题是作者的定势

不管是电脑还是手机，好像我的设备都是略落后时代的，主力是 2016 年的华硕 R557L，姑且是原装 8GB 内存，电池很早就鼓包换掉了，硬盘先是换了全新的 1TB 机械，后来又换成了二手 500GB SSD；

<!--more-->

有收过一台 Surface Pro 4 作为备用，走的拍拍平台，，30 天保障期刚过就出屏幕闪烁问题，才知道是这代机子的通病，扯皮一通后没也给退，买了外接屏终究是不方便，后边用外甥的教育优惠买了官翻 Pro 7，旧机就扔给了外甥；

本想着苏菲当主力，华硕作为备用不需要太大硬盘，然而平板的散热实在捉急，又换回笔记本当主力，好在硬盘换固态后体验好了不少，1TB 外接使用；

其实更早已经淘汰的华硕 F81se 的硬盘有留着，加上 R557L 最早的那块，两块 500GB 机械想着利用起来，然后也时值小主机兴起；

先收了台 nuc4，不好说价格划不划算，卖家没出硬盘，另外收的，总共 550，又买了 mini dp 转 hdmi，自己的旧硬盘当数据盘，几年下来不好说发挥了啥作用，总之能开机；

所以这时候是一个「如果」，如果当时能接受它加两块 500GB 机械硬盘，一块塞进去一块外接，甚至两块都外接使用。。。

然而我想着能把两块到塞进去使用，然后再用上系统的软 RAID，为此收了台华硕 VC66，1200 块带内存和 256GB 系统盘，翻车，「不要怕，还在保」，，然而售后被拒。。

其实当时京东上微星也有款双 2.5 盘位的主机，1900 块，「如果当时能加 700 预算.jpg」

还有就是，最早那两块 500GB 硬盘并不支持组 RAID，不过不久后我哥换电脑把旧的给我了，联想 e450，换了块京东京造的 ssd，最终三块机械两块外接在 e450 上组阵列，剩下那块塞 nuc4 里，，，关键我还用的 RAID 1，BT 下载有啥用镜像的必要么？然而看完就删也更用不到 1TB 的 RAID 0。。。。。

最后的前不久，剁手了机械师的小主机，补贴加优惠后 2944.41，，其实也想过要买游戏本的话预算至少要加两千，然而仔细又仔细考虑，实在没有需求，，，甚至机械师这台目前除了 win11 不习惯外还还算满意，，，然而问题就是好像用不上。。。。

「- -」这一节马上就说完了.jpg「- -」

当前因为 Pro 4 买的便携屏姑且作为笔记本的外接屏使用，后边各种小主机管理时也是用它，然而把新的小主机当主力机的话双屏体验就没了。。所以买小主机时一并买了硬件采集卡，想着串流屏幕到笔记本上，然而实际效果还不用远程控制，，这已经是硬件方案了。。。正好昨天又了解到 Sunshine + MoonlightSetup，效果更是不太行。。

总之现在还是向日葵远程为主，，外接屏同时有 Type-C 接口，也支持触摸可以需要时切换使用。。。没有屏幕的设备远程使用也很麻烦，所以会有显卡欺骗器这种东西，VC66 也买了，然而问题是我为毛要买 DVI 接口的，现在只有 HDMI 和 DP 也用不上，虽然现在 C 口接显示器也是一样效果；

### 本文主题

> VSCode 中，ctrl + k O 可以在新窗口打开当前文件，好像现在这个窗口现在不是独立，工作区切换后也会关掉，说这个是因为我先在一个文件里记录了装 sd 的笔记，然后要换工作区整理成博文。。

因为我并没有按 ￥5000+ 的预算，所以是没有独显的，所以本文以此为前提。。另外本人姑且有 Git，Python 之类的基础知识，浏览器有代理。。。

1、使用的部署项目如下：

> AUTOMATIC1111/stable-diffusion-webui: Stable Diffusion web UI
>
> [https://github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui "AUTOMATIC1111/stable-diffusion-webui: Stable Diffusion web UI")

2、项目指定了 Python 3.10.6，直接 exe 安装：

- [https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe "Python 3.10.6")
- 好像是因为更高版本不支持 `torch` ← 这个东西在安装时也是比较费时；

3、克隆项目到本地：

```bash
git clone git@github.com:AUTOMATIC1111/stable-diffusion-webui.git _sd

```
4、修改脚本参数：

依赖安装及程序运行理论上都只需要运行 `webui-user.bat` 就好，然而这里先对其进行修改，另外后续步骤是我在处理各种错误后复盘整理而来，建议先手动解决后再执行；

↓↓ 在原始文件内添加 `--skip-torch-cuda-test --no-half` 参数，如果你在 GPU 可以不改 ↓↓

```bash
@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half

call webui.bat

```

**重要：无论是否修改都先不要执行，因为有各种报错需要手动处理**

5、下载并安装 `CLIP`：

> 脚本安装会下载不到，所以浏览器下载后安装，下边链接是脚本执行时出现的：
>
> `https://codeload.github.com/openai/CLIP/zip/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1`

下载后保存为 `clip.zip` 到项目根目录，然后执行：

```bash
# PowerShell，虽然不清楚用 venv 和全局命令有什么区别
.\venv\Scripts\python.exe -m pip install clip.zip --prefer-binary

```

6、下载 `openai/clip-vit-large-patch14`：

```bash
# 直接在根目录下执行
git clone https://www.modelscope.cn/AI-ModelScope/clip-vit-large-patch14.git openai/clip-vit-large-patch14

```

如果缺少这个会报下边错误：

> OSError: Can't load tokenizer for 'openai/clip-vit-large-patch14'. If you were trying to load it from `https://huggingface.co/models`, make sure you don't have a local directory with the same name. Otherwise, make sure 'openai/clip-vit-large-patch14' is the correct path to a directory containing all relevant files for a CLIPTokenizer tokenizer.

7、提前下载好一个模型：

好像可以到「[ModelScope](https://www.modelscope.cn/home "魔塔社区")」平台下载，我参考的教程推荐了「[chilloutmix\_NiPrunedFp32Fix](https://www.modelscope.cn/models/TheKernelZ/chilloutmix_NiPrunedFp32Fix/files "chilloutmix\_NiPrunedFp32Fix")」

```bash
# 这里使用平台的 CLI 工具下载，另外这个 CLI 好像本身好像就能执行模型调用？？
pip install modelscope

# 模型的下载 · 文档中心
# https://modelscope.cn/docs/%E6%A8%A1%E5%9E%8B%E7%9A%84%E4%B8%8B%E8%BD%BD

# 指定下载路径时好像不会额外创建子文件夹，把模型名再加一遍
modelscope download --model TheKernelZ/chilloutmix_NiPrunedFp32Fix --local_dir './local_dir/chilloutmix_NiPrunedFp32Fix'

# 下载后移动模型文件夹到 _sd\models\Stable-diffusion 内
# 或者直接指定下载路径：--local_dir './models/chilloutmix_NiPrunedFp32Fix

```

8、最后执行 `webui-user.bat`；

· 其他报错：

如果没有上边「第 4 步」的修改，执行时就会报下边错误 ——

> RuntimeError: Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check

> RuntimeError: "addmm_impl_cpu_" not implemented for 'Half'


### 另一个文生图工具

其实之前知道了一个开箱即用的工具，把一些东西进行了封装，基本上下载然后解压就行，只是窗口设计上不科学的地方实在略多，连运行计时都没有；

> 万象生图
>
> [https://support.qq.com/product/637894](https://support.qq.com/product/637894 "万象生图")

还有就是使用网盘提供下载，没会员的话实在是难受，，姑且提供了一个 Resilio Sync 分享：

> 正好发现它刚更新了程序，下载后会更新到分享里；
>
> BNYMP5JH5HMFMUPTX5TVSXDIGCNUQBOR3

### 发电赞助

> 沉冰浮水正在创作和 Z-BlogPHP 相关或无关的各种有用或没用的代码 | 爱发电
>
> [https://afdian.com/a/wdssmq](https://afdian.com/a/wdssmq "沉冰浮水正在创作和 Z-BlogPHP 相关或无关的各种有用或没用的代码 | 爱发电")
