---
title: 「折腾」Docker 部署 Gitea 时的一些记录
date: 2023-02-09 17:53:35
tags:
 - Docker
 - Git
 - 折腾
categories:
 - 电脑网络
id: 1108
alias: 20220721836
---

使用 Docker 部署 Gitea 服务，使用指定的 http 和 ssh 端口映射，暂不考虑 https；

<!--more-->

部分`docker-compose.yml`配置如下，详细配置请参考[官方文档](https://docs.gitea.io/zh-cn/install-with-docker/)或[这个地址](https://github.com/wdssmq/zbp-docker-compose/issues/5)：

```yaml
version: '3'
services:
    gitea:
        image: gitea/gitea:1.18.1
        restart: always
        # …………
        # …………
        volumes:
            - ./gitea-data:/data
        ports:
            - "3000:3000"
            - "222:22"
        depends_on:
            - MySQL
        networks:
            - net_web
```

· 首次执行使用`sudo docker-compose up`命令；

· 浏览器访问`http://域名:3000/`会进入安装页；

· 和外部访问相关的有下边几个配置，请将其中的`localhost`替换为实际的域名或者 IP 地址；

----

注：「服务器域名」不带协议头和端口号，「基础 URL」则是完整的 URL 地址；

![001.png](001.png "001.png")

----

· 先`ctrl + c`停止容器，在挂载目录中找到配置文件进行修改；

----

> 关于年抛域名忘记关自动续费这种事……

`./gitea-data/gitea/conf/app.ini`：

```ini
[server]
APP_DATA_PATH    = /data/gitea
DOMAIN           = getrss2021.xyz
SSH_DOMAIN       = getrss2021.xyz
HTTP_PORT        = 3000
ROOT_URL         = http://getrss2021.xyz:3000/
DISABLE_SSH      = false
SSH_PORT         = 22
SSH_LISTEN_PORT  = 22
LFS_START_SERVER = true
LFS_JWT_SECRET   = e8mhNN3XZ0VlrDpNN-yNNIZzPooW9P9NNQENN5cVXRs
OFFLINE_MODE     = false
```
----

· 将其中的`SSH_PORT = 22`修改为`SSH_PORT = 222`；

· `sudo docker-compose up -d`正式启动容器；

· 程序将会给出`ssh://git@域名:222/用户名/仓库名.git`格式的地址供访问；

----------------

如果访问地址和配置不一致时，会出现下边的错误：

> Your ROOT_URL in app.ini is http://localhost:3000/ but you are visiting http://getrss2021.xyz:3000/
> You should set ROOT_URL correctly, otherwise the web may not work correctly.

<!-- 无法读取此仓库下的 Git 数据。 联系此实例的管理员或删除此仓库。 -->
