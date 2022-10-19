---
title: 「折腾」压缩 wsl2 磁盘占用
date: 2022-04-08 09:18:01
tags:
- Docker
- Ubuntu
- WSL2
- 折腾
categories:
- 电脑网络
id: 1427
alias: 20100428905
---

### 前文推荐

[「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220211184.html "「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水")

[「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140328160.html "「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水")

然而就结果上来说并没有解决 wsl2 内的 Docker 自启，换 zsh 后导致 npm 命令无法执行了；「后来发现不换 zsh 也行的。。囧」

<!--more-->

然后想着至少先备份下 wsl ——

```bash
wsl --export Ubuntu-18.04 "wsl-$(date +%Y-%m-%d).tar"
```

得到的文件有 29.1GB Orz，而前一次备份可以说正好是一个月前，大小是 5.88GB；

### 停用 wsl2

如果装了 Docker Desktop 也要先退出；

```bash
# 列表查看
wsl.exe --list --verbose
#   NAME                   STATE           VERSION
# * Ubuntu-18.04           Running         2

# 停用
wsl.exe --terminate Ubuntu-18.04
wsl.exe --list --verbose
#   NAME                   STATE           VERSION
# * Ubuntu-18.04           Stopped         2
```

### 文件路径

首先备忘几个文件夹路径：

- `%USERPROFILE%\AppData\Local\`
- `%USERPROFILE%\AppData\LocalLow\`
- `%USERPROFILE%\AppData\Roaming\`

wsl2 存放路径就在 `%USERPROFILE%\AppData\Local\Packages\` 内，不同 Linux 发行版对应不同的名称前缀，例如 Pengwin 是`WhitewaterFoundryLtd.Co`，Ubuntu 是`CanonicalGroupLimited`，Debian 是`TheDebianProject`；

我自己用的 Ubuntu-18.04，最终定位到如下路径：`%USERPROFILE%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx`

### 使用 diskpart 来压缩 wsl2 的虚拟磁盘

在命令行启动 diskpart 工具：

```bat
diskpart
```

会重新打开一个窗口，新窗口内执行：

```bash
# 实际路径请替换掉
select vdisk file="%USERPROFILE%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
# DiskPart 已成功选择虚拟磁盘文件。

# 执行压缩
compact vdisk
#  100 百分比已完成
# DiskPart 已成功压缩虚拟磁盘文件。
```

执行速度比 `wsl --export` 快不少，然后执行完发现，我没记压缩前的`ext4.vhdx`文件的大小，好像是 39G（？），执行后是 30G；

### 来源

清理 WSL2 的磁盘占用 - enrio - 博客园：

[https://www.cnblogs.com/enrio/p/14222648.html](https://www.cnblogs.com/enrio/p/14222648.html "清理 WSL2 的磁盘占用 - enrio - 博客园")

### 结语

之前在旧笔记本上用过 docker desktop，因为很卡所以印象不太好，所以这次一开始并没有选它；

姑且又安装了下：

```bash
wsl -l -v
#   NAME                   STATE           VERSION
# * Ubuntu-18.04           Running         2
#   docker-desktop         Running         2
#   docker-desktop-data    Running         2
```

也开启了如下选项，然后呢？？

> Resources
> WSL Integration
>
> Enable integration with additional distros:
>
> [√] Ubuntu-18.04
