---
title: 【折腾】麦沃硬盘盒报毒的应对方案
tags:
- 硬盘,折腾,言说
categories:
- 电脑网络
id: 1652
alias: 20130726899
jianshu: https://www.jianshu.com/p/67b97eac7811
---


> 有很多方便的工具可以用，然而又时常感觉不够方便。。

最最主要的起因是，昨天写代码时笔记本再一次卡到只能强制关机。。虽然怀疑较大可能是 Docker 的原因，一边面想着接下来几天不开 Docker 试一下会不会再卡，一方面着手备份和下载镜像准备重装系统。

<!--more-->

理论上 C 盘需要备份的东西都有备份，但是恐惧使然还是备份下整个分区比较安心。。

[【说点什么】系统重装恐惧症\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20190130794.html "【说点什么】系统重装恐惧症_杂七杂八_沉冰浮水")

麦沃的硬盘盒会报毒很早就知道了，都是通过禁用掉只读分区来解决，然而今天虽然带了硬盘过来，但是却带错钥匙了，冬天因为静电的原因在家都尽量随身带着一小串钥匙（眼镜以外经常忘记放哪儿的东西又多了一样- -）出门换大串的，带有指甲刀 U 盘啥的，，←昨晚更新了镜像进去。。

结果是就算备份好了文件重装还是问题，何况还没确定真的要重装。。

所以的所以想趁此水一篇文章出来，然而的然而，**配图果然还是好麻烦**。。

最近听说 Typora 内置了 PicGo 的支持，结果 PicGo 会被 Windows 报不安全，配置连接也一直不成功，最后发现在 PicGo 开放的端口号和 Typora 默认的不符。。

一连串的问题最后变成了上边一连串的流水帐。。

### 原本预定的主要内容↓


在【分区盘符】上【右键】→`属性`→`硬件`，进入【虚拟 CD 分区】的`属性` ↓↓

![001](https://i.loli.net/2020/12/23/Ssw2pOMZkYHdhEm.png "001")

【点击】`改变设置` ↓↓

![002](https://i.loli.net/2020/12/23/Z41holzxPsiMu2X.png "002")

`驱动程序`→`禁用设备`→`确定` ↓↓

![003](https://i.loli.net/2020/12/23/mZMwRseUtHYpgAh.png)


报毒提示 ↓↓

![000](https://i.loli.net/2020/12/23/NFHJOoMrQGD4XY6.png "000")

### 其他

最近写了不少 md 文档，直接用 VSCode，主要是这两个↓

Z-BlogPHP 插件开发教程：[https://wdssmq.github.io/HelloZBlog/#/](https://wdssmq.github.io/HelloZBlog/#/ "Z-BlogPHP插件开发教程")

ZBlogPHP-Wiki：[https://wdssmq.github.io/ZBlogPHP-Wiki/#/](https://wdssmq.github.io/ZBlogPHP-Wiki/#/ "ZBlogPHP-Wiki")

因为是直接发布在 GitHub Pages，就算有配图直接放一起就行。

---

所以 Typora 的存在略尴尬，久违的用一次还可能提示更新，，PicGo 接口的话 VSCode 也有相应插件。。

---

本地创建一个文件夹，一个 md 文件+可能的图片若干，写好内容后复制发布在博客 ← 然而内容有修改的话要不要再同步回来是个问题。。

---

文章已经发布了才想起来，午饭时先操作了次分区备份，使用 DG 的分区备份为镜像文件（\*.pmf），然而预计要 2.5 小时。。需要再排除些文件，比如`%USERPROFILE%\AppData\Local\Docker\wsl\data`←装 Docker 的话这里的文件会很大，，目前 21G。

<!--1652-->
