---
title: 「过往」“狗日的”腾讯
date: 2026-05-09 21:49:20
tags:
 - 过往
 - 小事
categories:
 - 杂七杂八
id: 744
alias: 20221005708
---

翻旧文件时发现的脚本命令，当年一不小心就会被安装腾讯管家，应对方法是直接在对应路径创建空文件夹，然后把权限设置为拒绝访问……

<!--more-->

虽然已经忘记为什么有个 20191015 文件夹了「- -」


```bat
set path1="c:\Program Files (x86)\Tencent\QQPCMgr"
set path2="c:\20191015"
REM Takeown /F %path% /r /d y
REM cacls %path% /t /e /g Administrators:F
REM rd /s %path%
md %path1%
md %path2%
echo y|cacls %path1% /d everyone>nul
echo y|cacls %path2% /d everyone>nul
pause

```
