---
title: 「折腾」VSCode + wsl2 + Docker 探究
date: 2022-02-11 20:20:14
tags:
- VSCode
- Docker
- Linux
- WSL2
categories:
- 电脑网络
id: 31
alias: 20220211184
---

建议参考官方文档：

> 安装 WSL | Microsoft Docs：
>
> [https://docs.microsoft.com/zh-cn/windows/wsl/install](https://docs.microsoft.com/zh-cn/windows/wsl/install "安装 WSL | Microsoft Docs")

要点：

- `wsl --install`命令将启用所需的可选组件，下载最新的 Linux 内核，将 WSL 2 设置为默认值，并安装 Linux 发行版
- 可以使用 `wsl --install -d <Distribution Name>` 指定安装的 Linux 发行版，否则默认安装 Ubuntu；
- `wsl -l -o` 命令可以查询可用 Linux 发行版列表；

<!--more-->

```bash
# 查看可用列表
wsl -l -o

# 安装 Ubuntu-20.04
wsl --install -d Ubuntu-20.04

# 查看已安装
wsl -l -v

```

注：Debian 版本信息为 9.5 (stretch)，好像不符合 Docker 的要求；

下边是我的踩坑记录，相当于分步安装，可以只安装 wsl2 功能自身而不安装 Linux 发行版，之后可以从备份中恢复；

**安装 WSL：**

- 「程序和功能」→「启用或关闭 Windows 功能」
- 勾选如下两项：
    - 「适用于 Linux 的 Windows 子系统」
    - 「虚拟机平台」
- 确定并重启系统；

理论上也可以 PowerShell 中执行如下命令：

```powershell
# 需要管理员权限，执行后也要先重启再安装内核更新
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

```

**升级为 WSL 2：**

访问：`https://aka.ms/wsl2kernel`；

下载并安装对应内容中提供的「WSL2 Linux 内核更新包」；

遇到如下错误提示也意味着需要装这个更新包；

> WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel

**设置默认版本：**

决定下一步将要安装的 Linux 发行版默认使用的 WSL 版本；

我一开始没执行这一步，但是好像可以再改；

```bash
wsl --set-default-version 2
# 设置 WSL 2 为默认；

```


**安装 Linux 发行版：**

1. 直接通过「[Microsoft Store](https://aka.ms/wslstore "Microsoft Store")」安装；← 点击链接会打开「Microsoft Store」应用内的一个列表页，但是包含的项目好像不全；
2. 执行`wsl -l -o`；

```bash
wsl -l -o
# 以下是可安装的有效分发的列表。
# 请使用“wsl --install -d <分发>”安装。

# NAME            FRIENDLY NAME
# Ubuntu          Ubuntu
# Debian          Debian GNU/Linux
# kali-linux      Kali Linux Rolling
# openSUSE-42     openSUSE Leap 42
# SLES-12         SUSE Linux Enterprise Server v12
# Ubuntu-16.04    Ubuntu 16.04 LTS
# Ubuntu-18.04    Ubuntu 18.04 LTS
# Ubuntu-20.04    Ubuntu 20.04 LTS

```

**查看已安装 Linux 子系统：**

> `wsl -l -v`

|     | NAME         | STATE   | VERSION |
| --- | ------------ | ------- | ------- |
| \*  | Ubuntu-20.04 | Running | 1       |


**备份和恢复：**


```bash
# 从文件导入
mkdir -p /c/WSL
wsl --shutdown && wsl -l -v
echo $(date +%Y-%m-%d\ %H:%M)
wsl --import Ubuntu-20.04 "C:\WSL\Ubuntu-20.04" "D:\#bak\WSL\wsl-2023-02-06.tar"
echo $(date +%Y-%m-%d\ %H:%M)
# exit ← 把这一行也复制上，以保证上一行的时间能够输出

# 注：恢复后默认使用 root 连接，需要在额外修改用户；
cat /etc/wsl.conf
sudo su
sudo echo -e "[user]" >> /etc/wsl.conf
sudo echo -e "default = wdssmq" >> /etc/wsl.conf
su wdssmq
cat /etc/wsl.conf

# 备份打包
mkdir -p /c/WSL
wsl --shutdown && wsl -l -v
echo $(date '+%Y-%m-%d %H:%M')
wsl --export Ubuntu-20.04 "/c/WSL/wsl-$(date +%Y-%m-%d).tar"
echo $(date '+%Y-%m-%d %H:%M')
# exit ← 把这一行也复制上，以保证上一行的时间能够输出

```

其他：

 - wsl 内部可以用 `/mnt/c/xxx` 直接读写 Windows 下的内容；
 - Windows 可以使用 `\\wsl$\Ubuntu-20.04\home\wdssmq` 浏览 wsl 内文件；


**修改已安装 Linux 子系统：**

> **如果直接安装了 wsl2 则可以跳过这一步；**

要在以前安装的 Linux 发行版上从 WSL 1 更新到 WSL 2，请使用命令 `wsl --set-version <distro name> 2`，将 `<distro name>` 替换为要更新的 Linux 发行版的名称。 例如，`wsl --set-version Ubuntu-20.04 2` 会将 Ubuntu 20.04 发行版设置为使用 WSL 2。

然而我第一次执行时提示如下：

```bash
wsl --set-version Ubuntu-20.04 2
# 正在进行转换，这可能需要几分钟时间...
# 有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
# WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel

```

所以需要安装上边说的「WSL2 Linux 内核更新包」，安装后再次执行转换：

```bash
wsl --set-version Ubuntu-20.04 2
# 正在进行转换，这可能需要几分钟时间...
# 有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
# 转换完成。

```

**安装 Docker：**

Install Docker Engine on Ubuntu | Docker Documentation

`https://docs.docker.com/engine/install/ubuntu/`

WSL 上的 Docker 容器入门 | Microsoft Docs

`https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-containers`

```bash
# 升级、安装前置依赖：
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# GPG 更新
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 官方源
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
#   sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 向 sources.list 中添加 Docker 软件源
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 官方源
# echo \
#   "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
#   https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安装 Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo service docker start

# 查看 docker 运行状态
service docker status
# * Docker is running

```

**安装 Z-BlogPHP：**

[【折腾】Docker 化安装 Z-BlogPHP\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20120817544.html "【折腾】Docker 化安装 Z-BlogPHP\_电脑网络\_沉冰浮水")

↑ 上文是基于 CentOS 环境写的，Ubuntu 下使用需要在命令前加 `sudo`；「这东西果然好麻烦」

win10 内直接`127.0.0.1:[端口号]`即可访问 WSL 内的服务；

Win10 与 WSL2 间的网络和文件互访 - LOGI

`https://logi.im/script/achieving-access-to-files-and-resources-on-the-network-between-win10-and-wsl2.html`

**安装 Git：**

```bash
sudo apt install git
git --version
# git version 2.17.1

```

默认安装的版本较低，需要最新版可以参考下方：

如何在 Ubuntu 上安装最新版本的 Git - 知乎

`https://zhuanlan.zhihu.com/p/108991735`

**其他：**

WSL2 网络代理配置（apt 与 git） - 知乎

`https://zhuanlan.zhihu.com/p/108927713`


cmd 中执行 `ipconfig` 查看网络信息，然后在 wsl2 中执行`export https_proxy="socks5://$IP:$PORT"`；

实际用 `192.168.*.*` 好像成功了；

```shell
ipconfig

# 无线局域网适配器 WLAN:

# 192.168.123.236

# export https_proxy="socks5://192.168.123.236:10808"

# 以太网适配器 vEthernet (WSL):

# 172.26.160.1

# export https_proxy="socks5://172.26.160.1:10808"

```

-----

在 WSL 2 上设置 Node.js | Microsoft Docs

`https://docs.microsoft.com/zh-cn/windows/dev-environment/javascript/nodejs-on-wsl`

ubuntu18.04 安装 nodejs 最新版、指定版 12.x 14.x - 尽情山水 - 博客园

`https://www.cnblogs.com/forheart/p/13203249.html`

-----

【折腾】VSCode 远程开发配置（Remote Development）_电脑网络_沉冰浮水

`https://www.wdssmq.com/post/20201120519.html`
