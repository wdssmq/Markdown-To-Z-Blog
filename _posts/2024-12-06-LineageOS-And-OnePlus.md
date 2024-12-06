---
title: LineageOS 的各种问题
date: 2024-12-06 16:22:15
tags:
 - 安卓
 - 手机
 - LineageOS
categories:
 - 电脑网络
id: 792
alias: 20230421460
---

收了台旧的一加手机，前机主刷了 LineageOS，整体还算不错，橙色也很 OK，就是有几个小问题，系统和软件上的。。

<!--more-->

### 一

一个较早就发现的问题是，拍照或录像时，明明是横屏，但拍出来的照片或视频却是竖屏的。。。

照片经常是发现不对就删掉重拍，视频就比较麻烦，所以有试着用软件旋转，最后发现，视频本身是对的，但是 metadata 属性被设置成了 90 度，播放器就会以竖屏播放。。。。

使用 ffmpeg 可以将其实改回来， PowerShell 脚本如下：

```powershell
# 删除已经存在的 *.new.mp4 文件
Remove-Item -Path .\*.new.mp4 -ErrorAction SilentlyContinue

# 遍历当前目录中的所有 MP4 文件
Get-ChildItem -Path . -Filter *.mp4 | ForEach-Object {
    $inputFile = $_.FullName
    $outputFile = [System.IO.Path]::ChangeExtension($inputFile, ".new.mp4")

    # 使用 ffmpeg 进行视频旋转
    # 因为我的视频本身是横屏，但是 metadata 中的旋转角度是 90，所以这里需要将旋转角度设置为 0；
    # 实际按需要修改为对应的旋转角度 0, 90, 180, 270
    ffmpeg -i $inputFile -c copy -metadata:s:v:0 rotate=0 $outputFile

    ## 以下是另一种旋转视频的方法，和 metadata 的区别是后者会真实旋转视频；
    ## transpose=1 顺时针旋转 90 度
    ## transpose=2 逆时针旋转 90 度
    ## -c copy 表示直接复制视频和音频流，不进行重新编码

    # ffmpeg -i $inputFile -vf "transpose=2" -c copy $outputFile
}

```

### 二

然后又到年底了，手机积分换话费的贴子刷到了好几个，然而，我这边发不出去短信。。。

提示「未选择用于发送短信的首选 SIM 卡」

这个错误提示搜索不到啥内容，然后切换到英文拿到了英文的提示：「No preferred SIM selected for sending SMS messages」

目测是一个陈年 Bug，有一个配置选项是「每次都询问」，然而实际发短信时并不会弹出这个询问，直接报错，然后看起来我的手机上默认就是这个状态。。

然后我这儿的后续问题是，我一开始不知道要在哪儿去指定这个「首选 SIM 卡」，在短信应用里找不到，然后这个选项的实际位置在：「设置」→「网络和互联网」→「 SIM 卡」 ，选择一张卡为其指定「短信偏好设置」。。

默认的「每次都询问」有问题，所以必须指定一张卡先，实际发短信时则可以切换实际要用的卡。。
