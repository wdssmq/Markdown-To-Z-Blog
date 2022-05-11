---
title: 「折腾」Docker 化安装 Z-BlogPHP
tags:
- Docker
- Z-BlogPHP
- 折腾
categories:
- 电脑网络
id: 1476
alias: 20120817544
---

## 使用 Docker Compose 部署「推荐」

wdssmq/zbp-docker-compose: 使用 Docker Compose 快捷部署 Z-BlogPHP + MySQL；：

[https://github.com/wdssmq/zbp-docker-compose](https://github.com/wdssmq/zbp-docker-compose "wdssmq/zbp-docker-compose: 使用 Docker Compose 快捷部署 Z-BlogPHP + MySQL；")

<!--more-->

```bash
# 安装 Docker Compose
sudo curl -L https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-`uname -s`-`uname -m` \
 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

生成最新版 Docker Compose 安装命令：[https://demo.wdssmq.com/tools/GenShell/](https://demo.wdssmq.com/tools/GenShell/ "生成最新版 Docker Compose 安装命令")

## 创建一个网络用于容器互通

`docker network create -d bridge net_web`

后续创建的容器全部连接至该网络中，更多说明请见「[这个链接](https://www.wdssmq.com/post/20210820126.html "2021-08-07 17:58 笔记 | Docker 网络相关")」；


## Docker 安装 MysQL + PHPMyAdmin

> [Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD](http://www.andrewchen.tw/2017/05/05/20170505_NOTE_DOCKER_MYSQL/ "Docker 安裝 Mysql + Phpmyadmin | 愛吃東西的 RD")

~~网络设置仍然不是很懂，只能说这样确实成功了；~~

下边命令最初是在 CentOS 下测试，Ubuntu 可能要加 `sudo`；

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
docker run --name PHPMyAdmin \
  --network=net_web \
  -e PMA_HOST=MySQL \
  -e UPLOAD_LIMIT=4096K \
  -p 9100:80 \
  -d phpmyadmin/phpmyadmin

# 平时可以停用，需要的时候再开启
docker stop PHPMyAdmin
docker start PHPMyAdmin

# MySQL 安装验证
docker exec -it MySQL mysql -u root -p

# 进入容器内登录测试
# docker exec -it MySQL /bin/bash
# mysql -u root -p

# 命令行备份
if [ ! -d ~/backup ]; then
  mkdir ~/backup
fi
# 指定要备份的数据库
DB_NAME=zblog_docker
docker exec -it MySQL mysqldump \
  -u root -pshujukumima \
  $DB_NAME > ~/backup/db_$DB_NAME-$(date +%Y-%m-%d-%H-%M).sql
# ↑ 重要：-p 参数后要不带空格直接连着密码

# 导入数据库
DB_SQL=~/backup/db_www.wdssmq.com.sql
DB_NAME=zblog_docker2
docker exec -i MySQL mysql \
  -u root -pshujukumima \
  -D $DB_NAME < $DB_SQL

# 下边命令仅作参考
use mysql;
select host,user from user;
update user set host='%' where user='root';

```

====================


## Docker 安装 Z-BlogPHP

```bash
ZBP_DIR=~/wwwroot/zbp_folder
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

# 查看日志
docker logs zbp

# 进入容器内部
docker exec -it zbp /bin/bash

```

====================

## 构建 ZBP-Docker 镜像并发布到 docker hub

> zblogcn/zblogphp-tencent-openapp-docker：
>
> [https://github.com/zblogcn/zblogphp-tencent-openapp-docker](https://github.com/zblogcn/zblogphp-tencent-openapp-docker "zblogcn/zblogphp-tencent-openapp-docker")


```bash
cd ~/git
# 克隆项目并进入目录
git clone git@github.com:zblogcn/zblogphp-tencent-openapp-docker.git zbp-docker
cd zbp-docker

# Build
docker build -t wdssmq/zblogphp:22.05 .
# —— 指定 Tag
docker build -t wdssmq/zblogphp .
# —— 不指定 Tag，将默认为 :latest

# 查看镜像
docker image ls

# 登录 docker hub
# https://hub.docker.com/
# https://hub.docker.com/settings/security
# 推荐用 Access Tokens 作为下边登录的密码
docker login -u <用户名> -p <密码>

# 发布镜像
docker push wdssmq/zblogphp:22.05
docker push wdssmq/zblogphp:latest

```

=========================

## 其他

各种错误提示：

· Warning: Permanently added 'github.com,192.30.255.113' (RSA) to the list of known hosts.

解决：

执行`ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts`；

· Permission denied (publickey).

解决：

使用形如`git@github.com:zblogcn/zblogphp-tencent-openapp-docker.git`的地址进行连接但是没有配置「SSH Key」时会出现该提示；

见下方`ssh-keygen`生成命令，然后将生成的`*.pub`内容填加至：[https://github.com/settings/ssh/new](https://github.com/settings/ssh/new "Add new SSH keys")；

· ERROR: You're using an RSA key with SHA-1, which is no longer allowed. Please use a newer client or a different key type

解决：

RSA 算法已被认为不再安全（主要取决于密钥长度）；

更直接的方法是更换算法为 ecdsa 或 ed25519，两者之间后者更安全，当然如果你的环境较旧，出现了`unknown key type ed25519`的提示，那么就选前者；

```bash
ssh-keygen -t ed25519
# unknown key type ed25519
ssh-keygen -t ecdsa
```

· Docker 网络相关

更详细的说明见「[这个链接](https://www.wdssmq.com/post/20210820126.html "2021-08-07 17:58 笔记 | Docker 网络相关")」；

```bash
docker network ls

docker network inspect bridge
docker network inspect host

docker network create -d bridge net_web
docker network inspect net_web
```


<!--1476-->
