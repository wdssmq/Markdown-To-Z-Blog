---
title: 「折腾」VSCode + wsl2 + Debian 探究
tags:
- VSCode
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

下边是我的踩坑记录，虽然就结果上好像是可以用的？

**安装 WSL：**

- 「程序和功能」→「启用或关闭 Windows 功能」
- 勾选如下两项：
    - 「适用于 Linux 的 Windows 子系统」
    - 「虚拟机平台」
- 确定并重启系统；

**升级为 WSL 2：**

访问：`https://aka.ms/wsl2kernel`；

下载并对应内容中提供的「WSL2 Linux 内核更新包」；

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

|     | NAME   | STATE   | VERSION |
| --- | ------ | ------- | ------- |
| \*  | Debian | Running | 1       |

**修改已安装 Linux 子系统：**

要在以前安装的 Linux 发行版上从 WSL 1 更新到 WSL 2，请使用命令 `wsl --set-version <distro name> 2`，将 `<distro name>` 替换为要更新的 Linux 发行版的名称。 例如，`wsl --set-version Ubuntu-20.04 2` 会将 Ubuntu 20.04 发行版设置为使用 WSL 2。

然而我第一次执行时提示如下：

```bash
wsl --set-version Debian 2
# 正在进行转换，这可能需要几分钟时间...
# 有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
# WSL 2 需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel
```

所以需要安装上边说的「WSL2 Linux 内核更新包」，安装后再次执行转换：

```bash
wsl --set-version Debian 2
# 正在进行转换，这可能需要几分钟时间...
# 有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
# 转换完成。
```

待续。。。

