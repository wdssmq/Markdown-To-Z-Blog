---
title: 「RPG Maker」RPG 游戏无法运行原因整理
tags:
- 游戏
- RPG
- 软件
categories:
- 电脑网络
id: 2934
alias: 20200105056
---

### dll 文件缺失

找不到 RGSS202E.dll

找不到 RGSS103G.dll

↑↑ 提示缺少 dll 文件的将 dll 文件放在游戏根目录下就行，和 Game.exe 同级；

<!--more-->

### RPGVXAce RTP is required to run this game

缺少运行库，下载相应版本——RPG Maker VX Ace，或直接使用- [RPG][运行库]RPGVXAce_RTP.zip -;

https://www.rpgmakerweb.com/download/additional/run-time-packages

### 下载地址

magnet:?xt=urn:btih:D18F8B7AB3F6F8F3FE1EE0C450E2B73FDB94DA16&dn=#[RPG 运行修复及修改器][20200105][0014cd6385f5]

magnet:?xt=urn:btih:85E99C455007B82A3F8607A66ABBA5DF8EFC10A8&dn=#[RPG 运行修复及修改器][20190831][0014cd6385f5]

上边磁如果下载不动可以加 QQ 群：

[lock]这里可能会放度盘/阿里云盘链接，如果有人需要的话[/lock]

-------------

↓↓目测无效

没有发现 RGSS-RTP Standard

如果运行游戏时电脑提示：“没有发现 RGSS-RTP Sdandard”，就请在文件夹里找到：Game.ini 这个文件，双击打开，在：“RTP1=Standard”这个地方，把 Standard 去掉，然后保存，再进行游戏


<!--2934-->
