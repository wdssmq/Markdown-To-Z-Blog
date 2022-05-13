---
title: 【折腾】基于 Node 的 QQ 机器人项目
tags:
- QQ,折腾,Node
categories:
- 电脑网络
id: 470
alias: 20210101974
zhihu: https://zhuanlan.zhihu.com/p/353340704
csdn: https://blog.csdn.net/qq_15022221/article/details/114174661
---

> 酷 Q 不能用了。更换了 Node 项目。
>
> [【折腾】在 Docker 中运行酷 Q 机器人](https://www.wdssmq.com/post/20181129356.html "【折腾】在 Docker 中运行酷 Q 机器人")

请先安装好 git 和 Node.js。。

参考：[【折腾】VSCode 远程开发配置（Remote Development）](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）")

「AD：[ShortSth:DesiVPS,VultrVPS][/ShortSth]」

<!--more-->

### 安装配置 ondebot

```bash
cd ~
if [ ! -d node ]; then
  mkdir -p node
fi

cd ~/node
if [ ! -d onebot ]; then
  git clone git@github.com:takayama-lily/node-onebot.git onebot
fi

cd ~/node/onebot
if [ ! -e config.js ]; then
  cp config.sample.js config.js
fi

# 修改 config.js 加入配置项；

node main 12123222
```

之后请参照引导揭示登录；

可能需要的参考：

如何完成滑动验证码并取得 ticket：[https://github.com/takayama-lily/onebot/issues/28](https://github.com/takayama-lily/onebot/issues/28 "如何完成滑动验证码并取得ticket · Issue #28 · takayama-lily/onebot")

首次登录成功后只需要使用`node main 12123222`登录；

### 使用 pm2 持久化运行

PM2 是 node 进程管理工具，可以利用它来简化很多 node 应用管理的繁琐任务，如性能监控、自动重启、负载均衡等，而且使用非常简单。

```bash
# 全局安装
npm install -g pm2

# 开启持久化运行
cd ~/node/onebot
# pm2 delete all

pm2 start main.js -n onebot -- 12123222
pm2 logs onebot

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
