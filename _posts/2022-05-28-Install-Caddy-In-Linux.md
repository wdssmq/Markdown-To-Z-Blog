---
title: 「折腾」Caddy 简易入门教程
tags:
- 折腾
- Linux
categories:
- 电脑网络
id: 876
alias: 20100604351
---

## 前言

有台真·垃圾 VPS，Docker 装不上，LNMP 啥的感觉也够呛，决定装个 Caddy，然后配合 hugo 或者 hexo 啥的玩下；

环境为 Ubuntu 18.04，使用 VSCode 远程连接；

<!--more-->

各种中文教程中的安装脚本链接都失效了，然后配置说明比 Z-BlogPHP 的文档还栏；

果然还是得看英文官方文档：[https://caddyserver.com/docs/](https://caddyserver.com/docs/ "Welcome — Caddy Documentation")；

`blog.wdssmq.com` ← 在写这篇教程时姑且能打开了，先用了 hugo 测试，能够自动给配置 ssl 这点挺厉害的；

「AD：[各种 VPS 推荐](https://www.wdssmq.com/tag/VPS/ "VPS\_沉冰浮水\_第1页")」


## 安装

```bash
curl -sS https://webinstall.dev/caddy | bash
```

> Install — Caddy Documentation
>
> [https://caddyserver.com/docs/install](https://caddyserver.com/docs/install 'Install — Caddy Documentation')

## Hello Caddy

```bash
cd ~
mkdir caddy
# code 为 VSCode 内编辑文件的命令；
code ~/caddy/Caddyfile
```

输入：

```conf
:8080
respond "Hello, world!"
```


```bash
# caddy 命令需要在同目录执行，除非指定 Caddyfile 路径；
cd ~/caddy
# Caddyfile 修改后使用 adppt 更新
caddy adapt
# 启动服务
caddy run
```

## 后台运行

```bash
# 后台运行
caddy start
# 重启，会自动执行 adapt
caddy reload
# 停止
caddy stop
```

## Caddyfile 配置

修改后需`caddy reload`；

在 Caddyfile 同目录下创建 index.html，修改配置文件内容：

```conf
:8080
file_server
# file_server browse # 不存在 index 文件时显示文件夹内的文件
```

--------------------

指定具体的 root 目录和域名等；

```conf
blog.wdssmq.com
root * /root/wwwroot/blog.wdssmq.com/public
encode zstd gzip
file_server
```

--------

开启多个服务监听；

`localhost`也可以换成具体的域名；

之后将 root file_server 等属性写进大括号内；

```conf
localhost {
	respond "Hello, world!"
}
localhost:2016 {
	respond "Goodbye, world!"
}
```

> file\_server (Caddyfile directive) — Caddy Documentation：
>
> [https://caddyserver.com/docs/caddyfile/directives/file_server](https://caddyserver.com/docs/caddyfile/directives/file_server "file\_server (Caddyfile directive) — Caddy Documentation")

> Caddyfile Tutorial — Caddy Documentation：
>
> [https://caddyserver.com/docs/caddyfile-tutorial](https://caddyserver.com/docs/caddyfile-tutorial "Caddyfile Tutorial — Caddy Documentation")
