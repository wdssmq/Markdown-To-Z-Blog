---
title: 「折腾」使用 Gource 为 Git 仓库生成动态视频
date: 2023-06-04 12:28:39
tags:
 - 折腾
 - Git
 - 电脑网络
categories:
 - 电脑网络
id: 74
alias: 20230426471
---

## 摘要

发现个工具 `acaudwell/Gource`，可以基于 Git 等版本控制系统的提交记录生成动态视频；

2021 年开始使用 Markdown 文件写博客，试着生成了一下视频；「`wdssmq/Markdown-To-Z-Blog`」

<!--more-->

完整记录有点长，只截取了 2023 年开始至今的部分（2023-01-02 - 2023-06-04），时长 `03:33`，`16.4G ppm` → `664MB mp4`；

换算下完整版本大概会有 15 分钟？文件大小的话。。emmm

到时可能试下 265 编码，，配 BGM 好像也很麻烦。。

## 下载

> 这边是在 Windows 下使用；

Gource - a software version control visualization tool：

[https://gource.io/](https://gource.io/ "Gource - a software version control visualization tool")

↑ 官网有这东西的 Win64 安装包/解压版，解压版需要自行添加环境变量；

Download FFmpeg：

[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html "Download FFmpeg")

↑ 然后好像还要准备 FFmpeg，上边页面中「`More downloading options`」>「`Get packages & executable files`」中下载 Windows 版本的 FFmpeg，解压后把 `bin` 文件夹路径添加到环境变量；

## 使用

```bash
# 查看帮助
gource -help

# 下边命令在 md2zb 项目路径下执行，使用的 shell 是 Git Bash

PPM_FILE=/d/md2zb.ppm
MP4_FILE=/d/md2zb.mp4
# 输出 ppm 文件
gource -f -1280x720 -s 4 -r 30 \
    --date-format "%Y-%m-%d %H:%M:%S" \
    --start-date '2023-01-02 12:24:00 +0800' \
    --stop-date '2023-06-04 15:48:42 +0800' \
    -o $PPM_FILE
# 生成视频
ffmpeg -y -r 30 -f image2pipe -vcodec ppm -i $PPM_FILE \
    -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 4 \
    -threads 0 -bf 0 $MP4_FILE
# ffmpeg 命令基于 Gource 示例修改， -r 30 是帧率，-crf 4 是画质，建议范围（1-17），较低的值表示更高的质量和更大的文件大小；
# 其他参数就不太懂了。。
```

Gource 可以指定某一起止区间的提交记录，对应参数格式为 `--start-date 'YYYY-MM-DD hh:mm:ss +tz' --stop-date 'YYYY-MM-DD hh:mm:ss +tz'`，其中 `+tz` 为时区，如 `+0800`；

下边命令用于获取指定提交的时间并应用格式化：

```bash
# git 获取指定提交的时间并应用格式化
git log 3426336e6b944188f2507ecbc518ae4df07098a7 -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S +0800'
git log 8b9ff137308a74cae7f6520b3f09d25a3a5aa785 -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S +0800'
# git log <commit_sha> -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S'

```

## Docker 使用

有一个 Docker 封装的 Gource 镜像：「[sandrokeil/docker-files/tree/master/gource](https://github.com/sandrokeil/docker-files/tree/master/gource "sandrokeil/docker-files/tree/master/gource")」

可以较快捷的使用，并且可以自动添加音乐文件；

## 参考

Controls · acaudwell/Gource Wiki

`https://github.com/acaudwell/Gource/wiki/Controls`

---

Videos · acaudwell/Gource Wiki

`https://github.com/acaudwell/Gource/wiki/Videos#windows`

---

Gource 版本可视化工具 使用手册 - Debug 客栈
`https://blog.debuginn.cn/linux-tools-gource/`

---

聊聊代码仓库可视化：gource 篇 - 知乎

`https://zhuanlan.zhihu.com/p/512355700`
