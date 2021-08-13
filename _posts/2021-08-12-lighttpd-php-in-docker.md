---
title: 「折腾」Docker 化部署 lighttpd 并安装 Z-BlogPHP
tags:
- Docker
- Z-BlogPHP
- 折腾
categories:
- 电脑网络
id: 802
alias: 20210804429
---

### 写在前边

> 在自己可控的前提下，探究「正确」的步骤。——沉冰浮水

起因是有位同学想在路由器里安装 Z-BlogPHP，环境是 lighttpd，然后伪静态没能正确生效；

<!--more-->

IIS、Apache、Nginx 姑且都用过，lighttpd 也仅仅是知道其存在而已。

### Docker 镜像资源

本想用另一个 ssh-nginx 镜像项目修改下实现，好像没成功，所以 Fork 了一个现成；

wdssmq/alpine-lighttpd-php: Lighttpd and PHP running on Alpine Linux in a Docker image：

[https://github.com/wdssmq/alpine-lighttpd-php](https://github.com/wdssmq/alpine-lighttpd-php "wdssmq/alpine-lighttpd-php: Lighttpd and PHP running on Alpine Linux in a Docker image")

过程中遇到的一些小坑：

> `Call to undefined function simplexml_load_string()`
>
> 解：
>
> 本身有安装`php-xml`，需要额外安装`php-simplexml`；

另外还填加了`php-mysqli`，「lighttpd.conf」规则中定义的`mimetype`也不够；

### 构建并使用

数据库及`net_web`已经提前创建，参考「[【折腾】Docker 化安装 Z-BlogPHP\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20120817544.html "【折腾】Docker 化安装 Z-BlogPHP\_电脑网络\_沉冰浮水")」；

```bash
# 创建目录并拉取 Git
mkdir -p /root/Git/
cd /root/Git/
git clone git@github.com:wdssmq/alpine-lighttpd-php.git

# 构建镜像
cd /root/Git/alpine-lighttpd-php
docker build -t wdssmq/lighttpd-php .

# 部署容器
DIR_lighttpd='/home/www/lighttpd'
PORT_lighttpd=8033
mkdir -p $DIR_lighttpd
cd ${DIR_lighttpd}
docker rm --force lighttpd-php
docker run --name lighttpd-php \
 --net=net_web \
 -p ${PORT_lighttpd}:80 \
 -v $(pwd):/var/www \
 -d wdssmq/lighttpd-php

# 「调试」查看日志
docker logs lighttpd-php

# 「调试」进入容器内部
docker exec -it lighttpd-php /bin/sh
```

映射端口号为`8033`，可自行更改，之后下载 Z-BlogPHP 程序到`'/home/www/lighttpd'`目录中即可；

具体命令行见：「[下载 Z-BlogPHP - node.md](https://github.com/wdssmq/alpine-lighttpd-php/blob/master/note.md#%E4%B8%8B%E8%BD%BD-z-blogphp "下载 Z-BlogPHP")」

### 关于伪静态

Z-BlogPHP 预置提供的伪静态规则如下；

```conf
# Rewrite rules - Z-BlogPHP
url.rewrite-if-not-file = (
  "^/(zb_install|zb_system|zb_users)/(.*)" => "$0",
  "^/(.*.php)" => "$0",
  "^/(.*)$" => "/index.php/$0"
)
```

虽然稍加研究便配置成功，并且预置在了上边的镜像构建中。然而怎么解释真心好难。

除了规则定义外，还需要先启用相应的功能「模块」，伪静态对应的模块是`mod_rewrite`；

然而事实是，lighttpd 能够解析执行 PHP 同样需要开启其相应的「模块」，模块名是`mod_fastcgi`;

就结果来说，以下几种形式都可以；

**写在一起：**

```conf
server.modules = (
  "mod_fastcgi",
  # "mod_xxxx", # 其他启用或未启用的模块，顺序理论上不重要
  "mod_rewrite"
)
```

**追加写法 1：**

```conf
# 显示定义一次
server.modules = (
  "mod_fastcgi", # 作为最后一项时能不能有「,」并不明确；
  # "mod_xxxxx", # 其他启用或未启用的模块，顺序理论上不重要
)

# 可能有其他定义或注释或并没有

# 追加并合并
server.modules += ("mod_rewrite")
```

**追加写法 2：**

```conf
# 追加并合并，在此之前可能已经定义过 server.modules，也可能没有；
server.modules += ("mod_fastcgi")

# 可能有其他定义或注释或并没有

# 追加并合并
server.modules += ("mod_rewrite")
```

所以最终「正确」的步骤只能是：

在 PHP 本身能够正确执行的前提下，并且已有定义中并末开启`mod_rewrite`模块，那么请尝试在**原有**「lighttpd.conf」文件的**最末尾**「另起一行」「**追加**」以下内容以开启伪静态：

```conf
# 启用 Rewrite 模块
server.modules += ("mod_rewrite")
# Rewrite rules - Z-BlogPHP
url.rewrite-if-not-file = (
  "^/(zb_install|zb_system|zb_users)/(.*)" => "$0",
  "^/(.*.php)" => "$0",
  "^/(.*)$" => "/index.php/$0"
)
```

如果仍然无法成功，作为「教程」，并不能预见你实际操作时会犯下的错误，以及实际环境中会影响结果的差异性，从数量意义上，可能性真的太多太多了；


### Git 又忘记设置用户信息了

```bash
git config --global user.name author #将用户名设为author
git config --global user.email author@corpmail.com #将用户邮箱设为author@corpmail.com
```

```bash
git config　user.name nickname #将用户名设为nickname
git config　user.email nickname@gmail.com #将用户邮箱设为nickname@gmail.com
```

<!-- 2021-08-12-Key-Values-Table-Of-Computer-Science -->
<!-- 「说点什么」计算机运作基础之「键值表」 -->
