---
title: 【折腾】基于Node的QQ机器人项目
tags:
- QQ,折腾,Node
categories:
- 电脑网络
id: 470
alias: 20210101974
---

> [【折腾】在Docker中运行酷Q机器人](https://www.wdssmq.com/post/20181129356.html "【折腾】在Docker中运行酷Q机器人")

请先安装好git和Node.js。。

参考：[【折腾】VSCode远程开发配置（Remote Development）](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）")

[AD]<a class="mz-ShortUrl" data-alias="VultrVPS" href="https://www.wdssmq.com/go/VultrVPS" target="_blank" rel="noopener noreferrer" title="验证码略反人类">VultrVPS - 验证码略反人类</a>

<!--more-->

### 安装配置ondebot

```bash
cd ~
# 这是我自己的魔改fork
git clone https://github.com/wdssmq/onebot.git
cd ~/onebot

cp config.sample.js config.js
node main 12123222
```

之后请参照使用说明登录：

如何完成滑动验证码并取得ticket：[https://github.com/takayama-lily/onebot/issues/28](https://github.com/takayama-lily/onebot/issues/28 "如何完成滑动验证码并取得ticket · Issue #28 · takayama-lily/onebot")

首次登录成功后只需要使用`node main 12123222`登录；

也可以在config.js中设置autoLogin；

### 使用pm2持久化运行

PM2 是 node 进程管理工具，可以利用它来简化很多 node应用管理的繁琐任务，如性能监控、自动重启、负载均衡等，而且使用非常简单。

```bash
# 全局安装
npm install -g pm2
cd ~/onebot

# 我设置了autoLogin，否则需要在main.js后加上你要登录的QQ号
pm2 start main.js -n onebot
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
