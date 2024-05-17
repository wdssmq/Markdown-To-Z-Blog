---
title: 「折腾」Docker 部署 Resilio Sync 和 RSSHub
date: 2019-06-17 15:50:31
tags:
- 折腾
- Docker
- Linux
categories:
- 电脑网络
id: 2916
alias: 20190617918
---

摘要：本文记录了使用 Docker 部署 Resilio Sync 和 RSSHub 的过程。

<!-- more -->

> Docker 需自行安装或者选购提供预装环境的空间：
>
> https://www.vultr.com/?ref=7663955
>
> 2024-03-13 补充 —— 你也可以通过下边链接查看推荐的其他 VPS 服务：
>
> [广告慎入\_沉冰浮水](https://www.wdssmq.com/category/%E5%B9%BF%E5%91%8A%E6%85%8E%E5%85%A5/ "广告慎入\_沉冰浮水")

Resilio Sync：

```bash
# 删除创建的容器
# docker rm --force Sync
docker pull resilio/sync
DATA_FOLDER=/root/Sync_Folder
WEBUI_PORT=8888
if [ ! -d $DATA_FOLDER ]; then
mkdir -p $DATA_FOLDER
fi
# 删除创建的容器
# docker rm --force Sync
docker run -d --name Sync \
           -p $WEBUI_PORT:8888 \
           -p 5555 \
           -v $DATA_FOLDER:/mnt/sync \
           --restart on-failure \
           resilio/sync

```

RSSHub：

2024-03-13 补充 —— 其实现在推荐使用 `docker-compose`，然后用 `ngingx_proxy_manager` 或者 `caddy` 反代一下；

<!-- Todo：后两者的说明文链接； -->

关于 cookie 设置部分，在 RSSHub 文档中：「部署」 → 「配置」 → 「部分 RSS 模块配置」一节中；

↑ 最近修改了 B 站密码，然后才想起来 cookie 也要改，哪怕是第二次配置了，「相应的内容在文档中的什么位置」这种事仍然很焦虑；

↑↑ 其实用的域名是年抛的 `.xyz`，也已经过期了，明明有个 `.fun` 域名，续费了 10 年，结果闲置了两三年什么的。。。

```yml
version: '3'

services:
    rsshub:
        # two ways to enable puppeteer:
        # * comment out marked lines, then use this image instead: diygod/rsshub:chromium-bundled
        # * (consumes more disk space and memory) leave everything unchanged
        # image: diygod/rsshub
        image: diygod/rsshub:chromium-bundled
        container_name: rsshub
        restart: unless-stopped
        ports:
            - '1200:1200'
        environment:
            NODE_ENV: production
            CACHE_TYPE: redis
            REDIS_URL: 'redis://redis:6379/'
            PUPPETEER_WS_ENDPOINT: 'ws://browserless:3000'  # marked
            BILIBILI_COOKIE_123456: SESSDATA=B 站的 cookie 字段设置;
        depends_on:
            - redis
            - browserless  # marked

    browserless:  # marked
        image: browserless/chrome  # marked
        container_name: browserless
        restart: unless-stopped  # marked
        ulimits:  # marked
          core:  # marked
            hard: 0  # marked
            soft: 0  # marked

    redis:
        image: redis:alpine
        container_name: redis
        restart: unless-stopped
        volumes:
            - redis-data:/data

volumes:
    redis-data:


# docker volume create redis-data

```

「- -」「- -」「- -」「- -」「- -」「- -」「- -」「- -」「- -」

以下为旧版命令参考：

```bash
cd /root
docker pull diygod/rsshub
if [ ! -d RSSHub ]; then
  git clone https://github.com/wdssmq/RSSHub.git
else
  cd /root/RSSHub
  git fetch --all
  git reset --hard origin/master
  git pull
fi
# 列出运行中的容器
docker container ls
# 删除创建的容器
# docker rm --force rsshub
# 后台创建容器并运行
cd /root/RSSHub/lib
docker run -d --name rsshub -p 1200:1200 -v `pwd`:/app/lib diygod/rsshub
#启停
docker stop rsshub
docker start rsshub

```

<!--2916-->
