---
title: 「Ubuntu 笔记」最终并没有用上的 Lubuntu
date: 2020-03-15 12:57:42
tags:
- Ubuntu
- 笔记
- Linux
- 折腾
categories:
- 电脑网络
id: 2936
alias: 20200315932
---

2023-03-04：

不算后续的后续，拍拍二手入了台 Surface Pro 4，结果翻车了（抖屏），又买了台官翻版 Surface Pro 7，华硕 F81se 彻底废弃了，华硕 X555LI 换了固态留在住处用……

<!--more-->

换固态前先后试装过 Deepin 和 Linux Mint，结果还是换回了 Win10；

Mint 留下的印象还蛮不错的，Deepin 虽然自带 wine 和安卓支持，但是输入法切换的快捷键修改后直接失效了就离谱……

再之后收了台 NUC4 当下载机，也用的 Win10，玩客云果然是不够用……


### 快捷键

`alt + 空格`调出当前窗口菜单，松开后再按相应的键：

`alt + 空格 d`：隐藏/显示装饰（标题栏）

`alt + 空格 n`：最小化

`alt + 空格 x`：最大化

----------------------------------

`ctrl + 空格`：激活输入法（修改后无效不知道延长回事）

`ctrl + alt + t`：命令行（终端）

### 终端命令行

```bash
# 安装 OR 更新五笔输入法

sudo apt-get install fcitx-table-wubi

# 查看硬盘空间

df -hl

```

### 启动项配置修改

\# 对应文件为/etc/default/grub

GRUB_CMDLINE_LINUX="acpi=off noapic nolapic locale=zh_CN irqpoll"

```bash
cd /etc/default

# 增加写权限
sudo chmod a+w grub

# 恢复权限
sudo chmod o-w grub
sudo chmod g-w grub

# 应用修改
sudo update-grub
```

------------

姑且算是《<a href="https://www.wdssmq.com/post/20191229296.html" target="_blank" title="足够轻量的代码编辑器？_杂七杂八_沉冰浮水">足够轻量的代码编辑器？</a>》一文的后续。。

前不久给主力笔记本换了块硬盘，旧硬盘装到旧笔记本上想着能应对一下基本的使用需求。。win7 + VSCode 还是勉强能用的，，但是勉强得过头了。最重要的是，临时离开系统进入休眠的话，，回来后根本无法正常唤醒 Orz

前文提到这次一开始是想装深度并且作为全盘安装，，但是并没能成功。win7 装好不久后碰巧知道了 Lubuntu 这个存在：

> Lubuntu 是 Ubuntu 快速、轻量级且节省能源的变体，它使用 LXDE（Lightweight X11 Desktop  Environment）桌面。它旨在面向低资源配置系统，并被主要设计用于上网本、移动设备和老旧个人电脑。

~~人生总有那么些不恰当的机缘~~，，结果就是划了分区装双系统，，经过几经折腾后也装上了。。

最新版也装不上，但是 LTS 可以，回头才发现深度根本没有 LTS。。

体验的话，确实很流畅，但是功能和习惯上，想说在有得选的情况下实在没什么理由为其坚持。。。。

最后的最后，又把硬盘拆出来配了个外壳当移动硬盘用。。。分区到是没动，，USB 启动应该还能进去系统？？？

<!--2936-->
