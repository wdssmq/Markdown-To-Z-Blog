---
title: 「折腾」VSCode + wsl2 + Debian 探究
tags:
- VSCode
- Linux
- 虚拟机
categories:
- 电脑网络
---

「- 会折腾这种东西的人应该知道下边几项怎么操作吧。。。 -」

**安装 WSL：**

- 「程序和功能」→「启用或关闭 Windows 功能」
- 勾选如下两项：
    - 「适用于 Linux 的 Windows 子系统」
    - 「虚拟机平台」
- 确定并重启系统；

<!--more-->

**设置默认版本：**

```bash
wsl --set-default-version 2
# 设置 WSL 2 为默认；
```

决定下一步将要安装的 Linux 发行版的 WSL 版本；

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

|     | NAME   | STATE   | VERSION |
| --- | ------ | ------- | ------- |
| \*  | Debian | Running | 1       |

**修改已安装 Linux 子系统：**

> `wsl --set-version Debian 2`

要在以前安装的 Linux 发行版上从 WSL 1 更新到 WSL 2，请使用命令 `wsl --set-version <distro name> 2`，将 `<distro name>` 替换为要更新的 Linux 发行版的名称。 例如，`wsl --set-version Ubuntu-20.04 2` 会将 Ubuntu 20.04 发行版设置为使用 WSL 2。

待续。。。

**参考：**

安装 WSL | Microsoft Docs：

[https://docs.microsoft.com/zh-cn/windows/wsl/install](https://docs.microsoft.com/zh-cn/windows/wsl/install "安装 WSL | Microsoft Docs")
