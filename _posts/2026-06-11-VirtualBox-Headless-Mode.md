---
title: 「小坑」VirtualBox 虚拟机的 headless 启动方式
date: 2026-06-11 15:21:05
tags:
 - VirtualBox
 - 虚拟机
 - 备忘
categories:
 - 电脑网络
id: 833
alias: 20221015312
---

在虚拟机列表那里可在右菜单里选择「启动」-「启动时不用图形用户界面」;

<!--more-->

如果需要命令行或快捷方式启动，形式用下：

```ini
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "LinuxMint" --type headless

```

「- -」「- -」「- -」


坑的地方在于，如果你用右键菜单「创建桌面快捷方式」，路径是这样的：

```ini
"C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe" --comment "LinuxMint" --startvm "{a359ef4b-cead-41e9-ef46-g64cca247efn}"

```

后者参数直接加上「`--type headless`」好像是是无效的，因为一个是 `VBoxManage` 另一个是 `VirtualBoxVM`，而且 `startvm` 和 `--startvm` 也有区别，后边值用 `NAME` 和 `UUIID` 应该都可以。
