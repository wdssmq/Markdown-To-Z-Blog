---
title: 【备忘】msysGit 安装及使用
tags:
- Git,备忘,折腾
categories:
- 电脑网络
id: 2327
alias: 20140804123
zhihu: https://zhuanlan.zhihu.com/p/401916212
---

### 安装包下载

在 Windows 中使用 Git 需要安装 msysGit：

[https://gitforwindows.org/](https://gitforwindows.org/ "https://gitforwindows.org/")

~~msysGit 自带 UI 界面，满足基本的使用需求~~，或者在其基础上使用 TortoiseGit 或者 GitHub

<!--more-->

TortoiseGit 下载地址（语言包需另外下载）：

[https://tortoisegit.org/download/](https://tortoisegit.org/download/ "https://tortoisegit.org/download/")

### 其他

两篇关于 Git 的教程：

图解 Git：[http://marklodato.github.io/visual-git-guide/index-zh-cn.html](http://marklodato.github.io/visual-git-guide/index-zh-cn.html "http://marklodato.github.io/visual-git-guide/index-zh-cn.html")

Git 简易使用指南：[http://www.bootcss.com/p/git-guide/](http://www.bootcss.com/p/git-guide/ "http://www.bootcss.com/p/git-guide/")

其实还是建议使用 msysGit + TortoiseGit 的，后者可以实时监测文件改动，操作步骤要少很多，此外汉化也比较完全，，虽然我还是看不懂好多操作到底是干啥的。。可以自行搜索下其使用教程或者等我（？）另外写一篇。。。

### 安装步骤

**2021 年 1 月 11 日：最新版安装流程已经有较大改动，1、4 两步的提示着重看下，其他默认就好。**

1、图 1~图 5 为安装过程，其中第 1 步和第 4 步时需要如图选择，其他默认

![图1](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553653705.png "msysgit-001.png")

图 1 ↑ **Git Gui Here 可以不选**

![图2](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553655129.png "msysgit-002.png")

图 2 ↑

![图3](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553656753.png "msysgit-003.png")

图 3 ↑

![图4](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553658033.png "msysgit-004.png")

图 4 ↑ **换行符现在感觉选第二个比较好**

![图5](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553659565.png "msysgit-005.png")

图 5 ↑

**建议使用 TortoiseGit 或 VSCode 内置功能，下边的内容可以跳过了！**

2、安装后桌面好像只有个命令行的快捷方式？没关系，直接在桌面或任意文件夹右键，点击 Git UI Here（图 6）

![图6](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553660453.png "msysgit-006.png")

图 6 ↑

3、创建新版本库，选择你的开发路径（图 7）。

![图7](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553661361.png "msysgit-007.png")

图 7 ↑

4、见到如图 8 界面并且自动扫描目录下的文件，下次可直接在 test 文件夹中 右键>>Git UI Here 进入该界面或者在“版本库”菜单中创建个快捷方式到桌面。

![](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553662813.png "msysgit-008.png")

图 8 ↑

5、第一次运行程序需在 编辑>>选项 中设置用户信息、文件编码什么的，第三个框是如何处理项目中的新建文件（未进行版本控制的），选择 Yes 时项目文件中的新建文件会被纳入到版本库中，选 no 则只监测已有文件的编辑修改而无视新文件。默认是 ask，有新文件时询问。

![图9](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553664861.png "msysgit-009.png")

图 9 ↑

6、每次使用 Gui 打开一个版本库均会自动扫描项目文件的改动，或者在窗口开启时修改过文件后“重新扫描”；之后可以执行“缓存改动”操作将修改临时备份一下（TortoiseGit 会实时自动扫描和缓存）；“提交”操作则为正式备份（版本控制理解为一种备份机制也没有不对吧。），但是每次提交都必须填写描述，注明你做了哪些修改；“签名”操作会自动在描述中追加你在「图 5」中填写的用户信息，可选。（图 10）

![图10](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553666081.png "msysgit-010.png")

图 10 ↑

7、在“版本库”菜单中找到“图示 master 分支的历史”，点击后可以查看、对比历次的提交（图 11、图 12）

![图11](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553668157.png "msysgit-011.png")

图 11 ↑

![图12](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553671349.png "msysgit-012.png")

图 12 ↑

8、图 13~16 演示了恢复项目到第一次提交，这个“gitk”窗口没有汉化，所以其他选项是啥意思完全不清楚。。

![图13](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553673785.png "msysgit-013.png")

图 13 ↑

![图14](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553676209.png "msysgit-014.png")

图 14 ↑

![图15](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553679653.png "msysgit-015.png")

图 15 ↑

![图16](https://www.wdssmq.com/zb_users/upload/2014/8/2014080553681153.png "msysgit-016.png")

图 16 ↑

9、「图 16」为测试文件夹第一次提交时的内容，再 Reset 一次就可以变回「图 13」，并且新添加的文件不会丢失。但是在第一次 Reset 之后如果在 gitk 界面执行了 Reload 等操作后，当前 master 之后的三次提交将丢失（图 17），要避免这种情况的话可以创建一个新分支——Create New Brace，然后 CheckOut 过去。

![图17](https://www.wdssmq.com/zb_users/upload/2014/8/2014080562848421.png "msysgit-017.png")

图 17 ↑

<!--2327-->
