---
title: 「折腾」基于 Node 的 QQ 机器人项目
date: 2021-01-01 11:19:13
tags:
- QQ
- 折腾
- Node.js
categories:
- 电脑网络
id: 470
alias: 20210101974
zhihu: https://zhuanlan.zhihu.com/p/353340704
csdn: https://blog.csdn.net/qq_15022221/article/details/114174661
---

> 2023-03-15
>
> 又又不能用了，不过有个 Fork 还有推进：[icqqjs/icqq](https://github.com/icqqjs/icqq "Tencent QQ Bot Library for Node.js")；
>
> 本来想自己实现 OneBot 接口，算是第一个 TS 项目，就略艰难，然后就发现也已经有了：[lc-cn/onebots](https://github.com/lc-cn/onebots "基于 icqq 的多例 oneBot 管理应用")；


> 2021-01-01
>
> 酷 Q 不能用了。更换了 Node 项目。
>
> [【折腾】在 Docker 中运行酷 Q 机器人](https://www.wdssmq.com/post/20181129356.html "【折腾】在 Docker 中运行酷 Q 机器人")

请先安装好 git 和 Node.js。。

参考：[【折腾】VSCode 远程开发配置（Remote Development）](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）")

「AD：[ShortSth:DesiVPS,VultrVPS][/ShortSth]」

<!--more-->

### 安装及配置

```bash
# 全局安装
# npm install -g onebots
cnpm install -g onebots

# 创建目录
RUN_DIR=~/node/onebots
mkdir -p $RUN_DIR
cd $RUN_DIR

# 初始化
onebots -c config.yaml

# 修改配置后再次执行
onebots -c config.yaml
```

> 具体配置，如何后台运行，然后和 Z-BlogPHP 的互通啥的目前没还没搞定……

### 使用 pm2 持久化运行

PM2 是 node 进程管理工具，可以利用它来简化很多 node 应用管理的繁琐任务，如性能监控、自动重启、负载均衡等，而且使用非常简单。

```bash
# 全局安装
npm install -g pm2

# 开启持久化运行
RUN_DIR=~/node/onebots
cd $RUN_DIR
# pm2 delete all


# 这里目前没搞定，，，
# pm2 start ecosystem.config.js
# pm2 logs onebots

# 开机自启
pm2 save
pm2 startup

# 理论上可以监听文件改变然后自动重启，，不过排除没搞定
# --watch --ignore-watch="node_modules data"
```

管理命令

```bash
# 列出全部进程
pm2 list

# 查看进程信息
pm2 describe onebot
pm2 logs onebot

# 停止进程
# pm2 stop app_name|app_id
pm2 stop onebot
pm2 stop all

# 删除
# pm2 delete app_name|app_id
pm2 delete onebot
pm2 delete all

# 开机自启
pm2 save
pm2 startup

# centos 7 查看自启项
# systemctl list-unit-files
systemctl list-unit-files | grep enabled
# pm2-root.service                              enabled
```

<!--470-->
