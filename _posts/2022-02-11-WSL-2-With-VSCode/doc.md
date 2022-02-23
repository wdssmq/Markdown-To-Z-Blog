---
title: 「折腾」VSCode + wsl2 + Docker 探究
tags:
- VSCode
- Docker
- Linux
- 虚拟机
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

# 安装 Ubuntu-18.04
wsl --install -d Ubuntu-18.04

# 查看已安装
wsl -l -v
```

注：Debian 版本信息为 9.5 (stretch)，好像不符合 Docker 的要求；

下边是我的踩坑记录，虽然就结果上好像是可以用的？

**安装 WSL：**

- 「程序和功能」→「启用或关闭 Windows 功能」
- 勾选如下两项：
    - 「适用于 Linux 的 Windows 子系统」
    - 「虚拟机平台」
- 确定并重启系统；

**升级为 WSL 2：**

访问：`https://aka.ms/wsl2kernel`；

下载并安装对应内容中提供的「WSL2 Linux 内核更新包」；

遇到如下错误提示也意味着需要装这个更新包；

> WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel

**设置默认版本：**

```bash
wsl --set-default-version 2
# 设置 WSL 2 为默认；
```

决定下一步将要安装的 Linux 发行版默认使用的 WSL 版本；

我一开始没执行这一步，但是好像可以再改；

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
| \*  | Ubuntu-18.04 | Running | 1       |

**修改已安装 Linux 子系统：**

要在以前安装的 Linux 发行版上从 WSL 1 更新到 WSL 2，请使用命令 `wsl --set-version <distro name> 2`，将 `<distro name>` 替换为要更新的 Linux 发行版的名称。 例如，`wsl --set-version Ubuntu-20.04 2` 会将 Ubuntu 20.04 发行版设置为使用 WSL 2。

然而我第一次执行时提示如下：

```bash
wsl --set-version Ubuntu-18.04 2
# 正在进行转换，这可能需要几分钟时间...
# 有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
# WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel
```

所以需要安装上边说的「WSL2 Linux 内核更新包」，安装后再次执行转换：

```bash
wsl --set-version Ubuntu-18.04 2
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
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 官方源
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 向 sources.list 中添加 Docker 软件源
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 官方源
# echo \
#   "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
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
