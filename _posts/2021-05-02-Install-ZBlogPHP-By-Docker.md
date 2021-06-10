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

## 2021-05-02

到网站能正常打开研究了大半天，所以 PHPMyAdmin 和数据库文件映射之类的暂时还没弄；

<!--more-->

## Docker 安装 MysQL + PHPMyAdmin

> [Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD](http://www.andrewchen.tw/2017/05/05/20170505_NOTE_DOCKER_MYSQL/ "Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD")

网络设置仍然不是很懂，只能说这样确实成功了；

```bash
# docker pull mysql/mysql-server

cd /root
MYSQL_DIR=/root/MySQL
if [ ! -d $MYSQL_DIR ]; then
  mkdir -p $MYSQL_DIR
fi

# 删除创建的容器
docker rm --force MySQL
docker run --name MySQL \
  --net=host \
  -e MYSQL_ROOT_HOST=172.%.%.% \
  -e MYSQL_ROOT_PASSWORD=shujukumima \
  --restart on-failure \
  -d mysql/mysql-server:5.7

# 安装验证
docker exec -it MySQL mysql -u root -p

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
if [ ! -d $ZBP_DIR ]; then
  mkdir -p $ZBP_DIR
fi
# 删除创建的容器
docker rm --force zbp
docker run --name zbp \
  -v $ZBP_DIR:/app \
  -e ZC_DB_HOST=172.18.0.1 \
  -e ZC_DB_NAME=zblog_docker \
  -e ZC_DB_USER=root \
  -e ZC_DB_PWDD=shujukumima \
  -e ZC_BLOG_USER=admin \
  -e ZC_BLOG_PWDD=shezhimima \
  -p 8081:80 \
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

```bash
docker network ls

docker network inspect bridge
docker network inspect host

docker network create -d bridge test-net
docker network inspect test-net

```


<!--1476-->
