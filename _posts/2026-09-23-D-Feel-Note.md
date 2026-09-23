---
title: 「折腾」水水的不想月报
date: 2026-09-23 07:56:51
tags:
 - 折腾
 - 代码
 - coding
categories:
 - 电脑网络
id: 116
alias: 20140225001
---

### 周期性的熬夜和心流

上星期也是达成了 git 满勤（9.13 ~ 9.19）。。

；之前一次是 1.4 ~ 1.10。。

这篇文章主要也是想水一下这段时期的成果。。

<!--more-->

> AI 额度就不够了……
>
> 这里是一条广告：[ShortSth:硅基流动][/ShortSth]

今天 9.23，这一周期的集中代码时间差不多就是上月 23 号开始的。。

；就已经开始「不想」写了，跳过一部分；

；总之一个经验就是合并分支后别用 VSCode 带的「推送/同步」功能，直接命令行，前者在「非快进式合并」下会触发 rebase，导致已经解决的冲突要现来一遍；

### Z-BlogPHP 主仓库

1.8 在 `dev/zbp18` 分支；

1.7 和 1.8 都有发测试打包：[Releases · zblogcn/zblogphp](https://github.com/zblogcn/zblogphp/releases "Releases · zblogcn/zblogphp")；

共有改进是加了 `zb_install/cli.php` 可以命令行完成安装。。；就「不想」写单独的使用文档

1.8 的初期设想是，在看起来和用起来没啥区别的前提下完成后台的模板化作为第一版，然而塞的东西有点多拖了进度。。

> zblogcn/zblogphp: Z-BlogPHP 博客程序
>
> [https://github.com/zblogcn/zblogphp](https://github.com/zblogcn/zblogphp "zblogcn/zblogphp: Z-BlogPHP博客程序")

### Z-BlogPHP 应用的自动打包流程（github + cnb.cool）

`cnb.cool` 是腾讯新出的 git 托管平台，虽然有条件还是建议 github；

示例仓库：[wdssmq/zbp\_UEditor](https://github.com/wdssmq/zbp_UEditor "wdssmq/zbp\_UEditor: UEditor For Z-BlogPHP")，参考`.github/workflows/release.yml`；

或者基于文档按需配置 ——

> wdssmq/zbp-app-pack: 一个用于将 Z-BlogPHP 应用（插件或主题）打包为 `.zba` 安装包的 GitHub Action。
>
> [https://github.com/wdssmq/zbp-app-pack](https://github.com/wdssmq/zbp-app-pack "wdssmq/zbp-app-pack: 一个用于将 Z-BlogPHP 应用（插件或主题）打包为 `.zba` 安装包的 GitHub Action。")

`cnb.cool` 版 ——

> zbp-app-pack
>
> [https://docs.cnb.cool/zh/plugin/public/open-source/php/zbp-app-pack.html](https://docs.cnb.cool/zh/plugin/public/open-source/php/zbp-app-pack.html "zbp-app-pack")

### AI 指令整合

自用 / 仅作参考

> wdssmq/ai-tools: 可复用的 GitHub Copilot / VS Code AI 工作流指令库。
>
> [https://github.com/wdssmq/ai-tools](https://github.com/wdssmq/ai-tools "wdssmq/ai-tools: 可复用的 GitHub Copilot / VS Code AI 工作流指令库。")


### Z-BlogPHP 本地部署、开发工具

基本功能：

- 将 git 目录的 Z-BlogPHP 部署到另外的目录；等同于 release 打包再解压，会清空原目录；
- cli 完成部署目录的打包；
- 为部署目录批量安装指定的插件应用；线上或本地的`.zba`文件，基于 Z-BlogPHP 仓库内的`utils/zba_toolkit.php`；
- 同步插件文件夹到部署目录，带 watch 模式；依赖 rsync 和 watchexec，win 系统可用；

> wdssmq/zbp-tools: 用于 Z-BlogPHP 开发调整的辅助脚本
>
> [https://github.com/wdssmq/zbp-tools](https://github.com/wdssmq/zbp-tools "wdssmq/zbp-tools: 用于 Z-BlogPHP 开发调整的辅助脚本")


### 其他

应用生态的各种探索，就很多东西并不是我自己的 coding 能力能决定和解决的……

> wdssmq/Z-Blog-We: 你可以向本仓库提交你的 RSS 或 Z-Blog 应用（插件/主题）；
>
> [https://github.com/wdssmq/Z-Blog-We](https://github.com/wdssmq/Z-Blog-We "wdssmq/Z-Blog-We: 你可以向本仓库提交你的 RSS 或 Z-Blog 应用（插件/主题）；")


> wdssmq/astro-zbp-we: 收集值得关注的博客、主题与插件，让每一次发现都能顺手收藏。
>
> [https://github.com/wdssmq/astro-zbp-we](https://github.com/wdssmq/astro-zbp-we "wdssmq/astro-zbp-we: 收集值得关注的博客、主题与插件，让每一次发现都能顺手收藏。")

