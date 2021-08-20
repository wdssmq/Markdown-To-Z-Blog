---
title: 【备忘】再再次谈系统安装【2021】
tags:
- 操作系统
- win10
- 备忘
- 重装系统
categories:
- 电脑网络
id: 848
alias: 20120622915
csdn: https://blog.csdn.net/qq_15022221/article/details/119829771
zhihu: https://zhuanlan.zhihu.com/p/397429226
jianshu: https://www.jianshu.com/p/f46cbee91cd4
cnblogs: https://www.cnblogs.com/wdssmq/p/15113443.html
---

### 前言

> 重装系统这么简单的事为什么仍然有人不会.jpg

这是第三篇了，从什么时候起「备忘」的 Tag 也变成了「折腾」。。

「- -」「- -」「- -」


### 镜像下载

虽然`https://msdn.itellyou.cn/`上选择比较多，但是选择太多对于强迫症太不友好。。另外 2021 年如何下载 ed2k 资源是个问题；

> 下载 Windows 10：
>
> [https://www.microsoft.com/zh-cn/software-download/windows10](https://www.microsoft.com/zh-cn/software-download/windows10 "下载 Windows 10")

↑ 所以推荐使用微软官方提供的下载工具，可按需下载为 ISO 镜像文件或写入 U 盘；

![dl-001.png](https://i.loli.net/2021/04/25/XybWUKdgwszpSiN.png "dl-001.png")

↑ 在网页中找到如图区域并点击下载按钮

![dl-002.png](https://i.loli.net/2021/04/25/ATn79xNURHuFsdv.png "dl-002.png")

↑ 选择第二项

![dl-003.png](https://i.loli.net/2021/04/25/4bCBLUahmZTD87K.png "dl-003.png")

↑ 保持默认

![dl-004.png](https://i.loli.net/2021/04/25/jmhSaoqxLtMkFpD.png "dl-004.png")

↑ 有准备 U 盘的话可以写进 U 盘，这里按「传统」选择下载镜像

**注：选择 U 盘的话，U 盘内原有内容将被清空！**


「- -」「- -」「- -」


### 安装

1、解压镜像文件到硬盘上；

2、重启电脑进入「命令提示符」界面；

3、键入第 1 步解压的安装文件路径开启安装；

![install-00A.png](https://i.loli.net/2021/04/25/BWqaNIb7LucCJgw.png "install-00A.png")

↑ 解压方式 A

![install-00B.png](https://i.loli.net/2021/04/25/D4NVwqFmsh2OKB5.png "install-00B.png")

↑ 解压方式 B：双击镜像文件会以虚拟光驱方式载入 → 之后复制内部文件到`D:\win10\`文件夹内

![install-001.png](https://i.loli.net/2021/04/25/Ul9eCXZ1GYsRVLK.png "install-001.png")

↑ 「`开始`」 → 「`电源`」 → 按住「`shift`」键的同时点击「`重启`」按钮 → 「`疑难解答`」 → 「`高级选项`」 → 「`命令提示符`」

![install-002.png](https://i.loli.net/2021/04/25/kK9OaVRZSHF7sQT.png "install-002.png")

![install-003.png](https://i.loli.net/2021/04/25/pK92QomNMx6BhiI.png "install-003.png")

![install-004.png](https://i.loli.net/2021/04/25/LRup8aJNsXMQrB3.png "install-004.png")

→→ 「命令提示符」需要管理员密码，然后我平时用的 `PIN` 结果忘记密码了；

![install-005.png](https://i.loli.net/2021/04/25/t6jMyuKUwbZ1fYW.jpg "install-005.png")

↑ `D:\win10\sources\setup.exe` ← 这个命令我是存在 OneNote 里的。

「- -」「- -」「- -」


### 回顾

[【备忘】win7 下再硬盘安装 win7（桌面库和家庭组图标删除）\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100718425.html "【备忘】win7下再硬盘安装win7（桌面库和家庭组图标删除）\_电脑网络\_沉冰浮水")

[【备忘】win7 下硬盘安装 Win8（可双系统）\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100407697.html "【备忘】win7下硬盘安装Win8（可双系统）\_电脑网络\_沉冰浮水")

「- -」「- -」「- -」

<!--848-->
