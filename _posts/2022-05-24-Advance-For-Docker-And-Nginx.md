---
title: 「折腾」Docker + Nginx 内映射子目录站点及自定义规则
tags:
- 折腾
- Docker
- Nginx
categories:
- 电脑网络
id: 2869
alias: 20181028361
---

因为计划外的原因重装了系统，WSL2 虽然有备份，但是备份文件太大了还是决定从头安装；

<!--more-->

另外之前的 Z-BlogPHP In Docker 是用的`docker run`部署的，改为`docker-compose`好像要方便一些；

因为有写一些「GM_脚本」，通过 web 服务访问才能让浏览器插件识别并安装，但是单独为其开个服务好像没必要，所以就选择作为 Z-Blog 的子目录实现；

`http://127.0.0.1:8081/userscript` ← 这样；

同时需要为该路径开启「目录浏览」功能（autoindex）；

在预定要挂载进 Docker 内的站点目录按如下路径放置文件并写入内容：

```conf
# zbp_folder/vhost.d/5-GM_JS.conf

# 屏蔽 vhost.d/ 本身的访问
location /vhost.d/ {
    return 404;
}

# 针对 userscript/ 配置所需要选项
location /userscript/ {
    autoindex on;
    autoindex_localtime on;
    add_header Cache-Control no-store;
}
```

以下为挂载示意：

`docker run`部署：

```bash
ZBP_DIR=~/wwwroot/zbp_folder
ZBP_PORT=8081
VHOST_DIR=$ZBP_DIR/vhost.d
sudo docker run --name zbp \
  --net=net_web \
  -v $ZBP_DIR:/app \
  -v ~/Git/userscript:/app/userscript \
  -v $VHOST_DIR/5-GM_JS.conf:/opt/docker/etc/nginx/vhost.common.d/5-GM_JS.conf \
  -e XXXXX \
  -p $ZBP_PORT:80 \
  --restart on-failure \
  -d wdssmq/zblogphp
```

`docker-compose`部署：

```yml
volumes:
    - ./www/zbp_folder:/app
    - ~/Git/userscript:/app/userscript
    - ./www/zbp_folder/vhost.d/5-GM_JS.conf:/opt/docker/etc/nginx/vhost.common.d/5-GM_JS.conf
```

· 相关推荐：

「折腾」压缩 wsl2 磁盘占用_电脑网络_沉冰浮水
https://www.wdssmq.com/post/20100428905.html

「折腾」Docker 化安装 Z-BlogPHP_电脑网络_沉冰浮水
https://www.wdssmq.com/post/20120817544.html

「折腾」使用 rollup.js 模块化编写 GM 脚本_电脑网络_沉冰浮水
https://www.wdssmq.com/post/20120627834.html

Docker 内 php-nginx 的伪静态相关_电脑网络_沉冰浮水
https://www.wdssmq.com/post/20190813019.html
