---
title: 「折腾」Windows 下修改文件（夹）的时间为最新
date: 2022-06-27 13:35:34
tags:
 - 折腾
 - Windows
categories:
 - 电脑网络
id: 604
alias: 20120782141
---

习惯用「按时间分组或排序」来管理文件，然后需要让确认过的文件或文件夹时间直接变成最新；

<!--more-->

本质是直接调用 PowerShell 命令；

以下内容保存为 `.bat` 后缀的文件，然后将要修改的文件或文件夹拖到图标上触发；

会同时修改「创建时间」和「最后修改时间」；

中间注释掉的那行是作用是，如果执行项目是文件夹，则对内部项目也执行时间修改；

```bat
@echo off

for %%i in (%*) do (
    echo %~n1
    echo %%i

    @REM powershell.exe -command "if (Test-Path -LiteralPath '%%i' -PathType Container){ls '%%i\*' | foreach-object { $_.LastWriteTime = Get-Date; $_.CreationTime = Get-Date}}"

    powershell.exe -command "Get-ItemProperty -LiteralPath '%%i' | foreach-object {$_.LastWriteTime = Get-Date; $_.CreationTime = Get-Date}"

    echo "-----"
)

@REM pause
```
