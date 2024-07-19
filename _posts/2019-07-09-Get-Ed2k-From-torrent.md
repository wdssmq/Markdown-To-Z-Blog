---
title: 「P2P」从 BitComet 生成的种子中获取 ed2k
date: 2019-07-09 15:52:23
tags:
- BT
- ed2k
- P2P
categories:
- 杂七杂八
id: 1832
alias: 20131014380
---

2019 年 07 月 09 日：

写了一个 PHP 的网页工具，上传种子文件即可提取 ed2k 链接（如果有的话）：


> BT 种子转磁力链\_BT 种子提取 ed2k
>
> [https://demo.wdssmq.com/Tools/bt2mag/](https://demo.wdssmq.com/Tools/bt2mag/ "BT 种子转磁力链\_BT 种子提取 ed2k")


核心库来自：

adriengibrat/torrent-rw: php5 class to read and write .torrent files：

[https://github.com/adriengibrat/torrent-rw](https://github.com/adriengibrat/torrent-rw "adriengibrat/torrent-rw: php5 class to read and write .torrent files")

\----------------------------

常见的的 ed2k 链接格式

`ed2k://|file|<文件名称>|<文件大小>|<文件哈希值>|h=<根哈希值>|/`

但是最后的根哈希值并不是必须的，，所以只要满足下边结构就能用。。

`ed2k://|file|<文件名称>|<文件大小>|<文件哈希值>|/`

然后如下图，用专门工具打开比特慧星生成的 `.torrent` 文件找到这三个值就可以拼凑出 ed2k（文件名其实可以随便写）。当然，至于有没有速度看运气；

![001.png](https://www.wdssmq.com/zb_users/upload/2013/10/2013101462780169.png "001.png")

相关文章：

[一些能用的 BT Tracker 服务器地址【不定时更新】\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20130323295.html "一些能用的 BT Tracker 服务器地址【不定时更新】\_电脑网络\_沉冰浮水") —— 内附上图软件的下载

<!--1832-->
