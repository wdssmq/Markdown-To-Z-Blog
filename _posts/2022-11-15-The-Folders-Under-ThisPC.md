---
title: 「折腾」Win11 更新后，「此电脑」内的用户文件夹不见了这件事
date: 2022-11-15 13:13:35
tags:
 - 折腾
 - Win11
 - Windows
categories:
 - 电脑网络
id: 862
alias: 20220522481
---

果然录视频越来越熟练了，，所以是不是可以不用配图了 - -

<!--more-->

- 快捷键「Win + R」;
- 运行「regedit」；
- 定位到以下路径：
    - `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace`
- 每一个对应项下有一个名为「`HideIfEnabled`」的属性，将该属性删除即可；
- 重启「Windows 资源浏览器」；


```conf
{088e3905-0323-4b02-9826-5d99428e115f}  -  下载
{24ad3ad4-a569-4530-98e1-ab02f9417aa8}  -  图片
{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}  -  音乐
{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}  -  桌面
{d3162b92-9365-467a-956b-92703aca08af}  -  文档
{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}  -  视频
```

<iframe src="//player.bilibili.com/player.html?aid=517691728&bvid=BV16g411q79T&cid=892205601&page=1" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

然而剩下的几个对应的啥？

```conf
{1CF1260C-4DD0-4ebb-811F-33C572699FDE}
{374DE290-123F-4565-9164-39C4925E467B}
{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}
{A0953C92-50DC-43bf-BE83-3742FED03C9C}
{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}
```


> 升级到 WIN11 后，此电脑中的文件夹消失了 - Microsoft Community
>
> `https://answers.microsoft.com/zh-hans/windows/forum/all/%E5%8D%87%E7%BA%A7%E5%88%B0win11%E5%90%8E%E6%AD%A4/da396a3b-ed81-4236-9f74-fee441c721ec`

下边这篇直接给了 reg  文本，执行后效果一样：

> Windows 11 恢復此電腦中 6 個文件夾的方法 - 零度解說
>
> `https://www.freedidi.com/6837.html`


<!--
```ini
Windows Registry Editor Version 5.00
; Created by: 零度解說

; Desktop
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}]
"HideIfEnabled"=-

; Documents
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}]
"HideIfEnabled"=-

; Downloads
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}]
"HideIfEnabled"=-

; Music
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}]
"HideIfEnabled"=-

; Pictures
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}]
"HideIfEnabled"=-

; Videos
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}]
"HideIfEnabled"=-
```
-->
