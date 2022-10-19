---
title: Docker 内 php-nginx 的伪静态相关
date: 2021-09-30 16:50:42
tags:
- Docker
- PHP
- Nginx
categories:
- 电脑网络
id: 592
alias: 20190813019
---

### 目标

基于`webdevops/php-nginx`构建的 Docker 镜像，默认支持伪静态的，然而忘记是哪个文件了，所以专门记录一下过程；

**注：目前只是把文件路径梳理了出来，具体怎么合理优雅的进行自定义要再研究 Orz；**

<!--more-->

### 命令备忘

```sh
# 进入容器内
docker exec -it zbp_ForAPP /bin/bash

# 在容器内执行
find /|grep nginx.conf
```
主文件路径是：`/etc/nginx/nginx.conf`，然而又引用了各种外部文件；

比如：`include /etc/nginx/modules-enabled/*.conf;`，实际对应文件在：`/usr/share/nginx/modules-available/`；←不过这里都是一些`*.so`文件的引用；

然后是：`include /etc/nginx/conf.d/*.conf;`和`include /etc/nginx/sites-enabled/*;`；

不过后者默认为空，前者涉及到的主要文件都在`/opt/docker/etc/nginx`内；

以下为了查询需要的路径：

```sh
# 进入容器内部
docker exec -it zbp_ForAPP /bin/bash
cd /etc/nginx/conf.d
ls
# 10-docker.conf

readlink *
# /opt/docker/etc/nginx/main.conf

cd /opt/docker/etc/nginx
ls
# conf.d       main.conf  ssl                vhost.common.d  vhost.ssl.conf
# global.conf  php.conf   vhost.common.conf  vhost.conf
```

```shell
# 在容器外
# 复制文件
NGINX_DIR=/home/www/zbp_ForAPP/nginx
docker cp zbp_ForAPP:/etc/nginx/nginx.conf "${NGINX_DIR}/"
docker cp zbp_ForAPP:/opt/docker/etc/nginx "${NGINX_DIR}/"
# docker cp zbp_ForAPP:/usr/share/nginx/modules-available "${NGINX_DIR}/"
```

### 结果

以容器内路径来说，有下边文件：

`/opt/docker/etc/nginx/vhost.common.d/10-location-root.conf`

内容：

```conf
location / {
    try_files $uri $uri/ /index.php?$query_string;
}
```

等同于一般意义上的伪静态；大概。。
