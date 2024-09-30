---
title: 「备忘」使用符号链接映射软件配置文件夹
date: 2024-09-30 12:42:45
tags:
- Windows
- 备忘
- 重装系统
- Win10
categories:
 - 电脑网络
id: 670
alias: 20220826264
---

一些软件会把配置文件放在 `%USERPROFILE%\AppData\Local` 或 `%USERPROFILE%\AppData\Roaming`，其中一些需要备份一下在重装系统后恢复。。

<!--more-->

> 另：`%AppData%` 变量等同于 `%USERPROFILE%\AppData\Roaming`，而 `%LocalAppData%` 变量等同于 `%USERPROFILE%\AppData\Local`。。。

下边是我使用的方案：

- 1、在 `C:\config` 下存放真实的配置文件，`C:\config\Roaming` 和 `C:\config\Local` 分别对应 `%USERPROFILE%\AppData\Roaming` 和 `%USERPROFILE%\AppData\Local`；
- 2、并不是所有配置都需要备份，所以只映射需要的文件夹，比如 `C:\config\Local\Everything`、`C:\config\Roaming\Everything`；
- 3、重装系统前备份整个 C 盘到外置硬盘，重装系统后恢复 `C:\config`，再映射相应的文件夹；

再下边是自动化的 PowerShell 脚本：

- 1、保存脚本至 `C:\config\config.ps1`，按需调整 `$directoryList`；
- 2、在相应的软件安装前执行，「右键」→「使用 PowerShell 运行」，需要允许管理员权限；
- 3、首次运行会自动创建 `C:\config\Roaming` 和 `C:\config\Local` 及内部的空文件夹，然后创建符号链接；
- 4、如果软件已经安装，会提示：`The path $dir\$name is not a symbolic link.`，可以剪切**合并**至 `C:\config` 内相应文件夹，之后再次运行脚本；
- 5、恢复时只需将 `C:\config` 复制到新系统，再次运行脚本，同样应在软件安装前执行；

**注：如果遇到「禁止运行脚本」，使用 `set-executionpolicy remotesigned` 修改执行策略；**

```powershell
Set-Location "C:\config"

# 用于创建目录，两个参数，dir 和 name，判断 dir/name 是否存在，不存在则创建
function CreateDirectory($dir, $name) {
    # $pwd = Get-Location
    if (!(Test-Path "$dir\$name")) {
        # 直接创建目录
        New-Item -ItemType Directory -Path "$dir\$name"
    }
    else {
        Write-Output "The path $pwd\$dir\$name already exists"
    }
    # 输出换行
    Write-Output ""
}

# 用于创建符号链接到 $env:AppData 或 $env:LocalAppData
function CreateSymbolicLink($dir, $name) {
    $srcDir = "$pwd\$dir\$name"
    # $dir 判断 Roaming 或 Local，替换成 $env:AppData 或 $env:LocalAppData
    if ($dir -eq "Roaming") {
        $dir = $env:AppData
    }
    elseif ($dir -eq "Local") {
        $dir = $env:LocalAppData
    }
    if (!(Test-Path "$dir\$name")) {
        # 创建符号链接
        cmd /c mklink /d "$dir\$name" $srcDir
    }
    else {
        $item = Get-Item "$dir\$name"
        if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
            Write-Host "The path $dir\$name is a symbolic link."
        }
        else {
            Write-Output "+++++++++++++++++++++++++++++"
            Write-Host "The path $dir\$name is not a symbolic link."
            Write-Output "+++++++++++++++++++++++++++++"
        }
        # Write-Output "$dir\$name already exists"
    }
    # 输出换行
    Write-Output ""
}

# 判断管理员权限
If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")) {
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" $PSCommandArgs" -Verb RunAs
    Exit
}

# 获取需要创建的目录的列表
$directoryList = @("Everything", "qBittorrent", "Resilio Sync", "Resilio Sync Service")

# 循环遍历目录列表，检查目录是否存在，不存在则创建
foreach ($directory in $directoryList) {
    CreateDirectory "Roaming" $directory
    CreateSymbolicLink "Roaming" $directory
    CreateDirectory "Local" $directory
    CreateSymbolicLink "Local" $directory
    Write-Output "------------------------"
    Write-Output ""
}

# 输入任意键关闭窗口
Read-Host -Prompt "Press any key to continue..."

```
