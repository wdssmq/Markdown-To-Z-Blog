---
title: 【折腾】Docker 化安装 Z-BlogPHP
tags:
- Docker
- Z-BlogPHP
- 折腾
categories:
- 电脑网络
id: 1476
alias: 20120817543
---

## 创建一个网络用于容器互通

`docker network create -d bridge net_web`

后续创建的容器全部连接至该网络中，更多说明请见「[这个链接](https://www.wdssmq.com/post/20210804429.html "2021-08-07 17:58 笔记 | Docker 网络相关")」；

<!--more-->

## Docker 安装 MysQL + PHPMyAdmin

> [Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD](http://www.andrewchen.tw/2017/05/05/20170505_NOTE_DOCKER_MYSQL/ "Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD")

~~网络设置仍然不是很懂，只能说这样确实成功了；~~

```bash
# cd /root
# MYSQL_DIR=/root/MySQL
# if [ ! -d $MYSQL_DIR ]; then
#   mkdir -p $MYSQL_DIR
# fi

# 删除已创建的容器
docker rm --force MySQL
docker run --name MySQL \
  --net=net_web \
  -e MYSQL_ROOT_HOST=172.%.%.% \
  -e MYSQL_ROOT_PASSWORD=shujukumima \
  --restart on-failure \
  -d mysql/mysql-server:5.7

# PHPMyAdmin，映射端口为 9100
docker rm --force PHPMyAdmin
docker run --name PHPMyAdmin -d --network=net_web -e PMA_HOST=MySQL -p 9100:80 phpmyadmin/phpmyadmin

# 平时可以停用，需要的时候再开启
docker stop PHPMyAdmin
docker start PHPMyAdmin

# 安装验证
docker exec -it MySQL mysql -u root -p

# 备份，zbp_ForAPP 为数据库名
docker exec -it MySQL mysqldump -u root -p shujukumima zbp_ForAPP > /root/backup/db_zbp_ForAPP.sql

# 进入容器内登录测试
# docker exec -it MySQL /bin/bash
# mysql -u root -p

# 下边命令仅作参考
use mysql;
select host,user from user;
update user set host='%' where user='root';

```

====================


## Docker 安装 Z-BlogPHP

```bash
cd /root
ZBP_DIR=/root/zbp_folder
ZBP_PORT=8082
if [ ! -d $ZBP_DIR ]; then
  mkdir -p $ZBP_DIR
fi
# 删除创建的容器
docker rm --force zbp
docker run --name zbp \
  --net=net_web \
  -v $ZBP_DIR:/app \
  -e ZC_DB_HOST=MySQL \
  -e ZC_DB_NAME=zblog_docker \
  -e ZC_DB_USER=root \
  -e ZC_DB_PWDD=shujukumima \
  -e ZC_BLOG_USER=admin \
  -e ZC_BLOG_PWDD=shezhimima \
  -p $ZBP_PORT:80 \
  --restart on-failure \
  -d wdssmq/zblogphp

# 进入容器内部
docker exec -it zbp /bin/bash

```

====================

## 构建 ZBP-Docker 镜像并发布到 docker hub

> zblogcn/zblogphp-tencent-openapp-docker：
>
> [https://github.com/zblogcn/zblogphp-tencent-openapp-docker](https://github.com/zblogcn/zblogphp-tencent-openapp-docker "zblogcn/zblogphp-tencent-openapp-docker")


```bash
cd /root

# 克隆项目
git clone https://github.com/zblogcn/zblogphp-tencent-openapp-docker.git

# 周老师设置的项目名太长了
mv zblogphp-tencent-openapp-docker zbp-docker-tencent

# 登录 docker hub
# https://hub.docker.com/
# docker login -u <用户名> -p <密码>

# ---------------------------------------------

cd /root/zbp-docker-tencent
git pull

# Build + Push
docker build -t wdssmq/zblogphp .
# docker push wdssmq/zblogphp

```

=========================

## 其他

两个错误提示：

· Warning: Permanently added 'github.com,192.30.255.113' (RSA) to the list of known hosts.

解决：

执行`ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts`；

· Permission denied (publickey).

解决：

使用形如`git@github.com:zblogcn/zblogphp-tencent-openapp-docker.git`的地址进行连接但是没有配置「SSH Key」时会出现该提示；

可改用`https://github.com/zblogcn/zblogphp-tencent-openapp-docker.git`或者部署「SSH Key」连接；

· Docker 网络相关

更详细的说明见「[这个链接](https://www.wdssmq.com/post/20210804429.html "2021-08-07 17:58 笔记 | Docker 网络相关")」；

```bash
docker network ls

docker network inspect bridge
docker network inspect host

docker network create -d bridge net_web
docker network inspect net_web
```


<!--1476-->
