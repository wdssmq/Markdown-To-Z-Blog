---
title: 【折腾】Docker 空间占用问题及 Nginx
tags:
- Docker,Nginx,折腾
categories:
- 电脑网络
id: 357
alias: 20210210927
---

### Docker 空间占用

**注：关于清理空间部分目前并没有总结出实际可用的方案，下边只是一些探索记录。**

Docker 的 df 命令

```bash
docker system df

# 下边是结果
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              2                   2                   380MB               0B (0%)
Containers          2                   2                   0B                  0B
Local Volumes       21                  0                   446.7MB             446.7MB (100%)
Build Cache         0                   0                   0B                  0B
```

然而感觉并不大，上`df -hl`

```bash
df -hl

# 结果如下
Filesystem      Size  Used Avail Use% Mounted on
udev            463M     0  463M   0% /dev
tmpfs            99M   11M   88M  11% /run
/dev/vda1        25G   25G     0 100% /
tmpfs           493M     0  493M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           493M     0  493M   0% /sys/fs/cgroup
tmpfs            99M     0   99M   0% /run/user/0
overlay          25G   25G     0 100% /var/lib/docker/overlay2/0c44aacce0a523f8d96af3c6c20e02ef3331961dab7e676299bb8c366626f125/merged
shm              64M     0   64M   0% /var/lib/docker/containers/efa1960dd0e4c2d5fb8d2ba756b781e0d9392a148620334b70fd0c7b06737653/mounts/shm
overlay          25G   25G     0 100% /var/lib/docker/overlay2/0ccf53346b8e4227b82530273532608b186fbf54545818340c9c8f062a63dde8/merged
shm              64M     0   64M   0% /var/lib/docker/containers/1ca6b4a758efaed43d715bde4f9b3f435682c4cfd7441b52b69a9ad04b42fa16/mounts/shm
```

搜索到的清理命令是`docker system prune [-a]`，`-a`参数会清理的比较彻底，然而执行后并没能解决问题。。

### 安装 Nginx

直接运行`docker pull nignx`会报错，大概意思是需要账号密码啥的，执行`docker login`进行登录。

没有账号的去`https://hub.docker.com`注册。

手动指定 tag 可能成功率高些【玄学】：`docker pull nginx:latest`。

```bash
# 运行测试（也可以不测）
docker run --rm --name "nginx" -p 80:80 nginx

# 实际部署
# docker rm --force nginx #删除已创建的容器

# 创建文件夹
mkdir -p /root/nginx/{conf,conf.d,html,log}

# 创建/root/nginx/conf.d/default.conf并配置所需内容

docker run -d --name nginx -p 80:80 \
          -v /root/nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf \
          -v /root/nginx/log:/var/log/nginx \
          -v /root/nginx/html:/usr/share/nginx/html \
          nginx
```

### 关于 nginx.conf 和 default.conf

网上找到的教程提到要自己创建 nginx.conf 然后映射进容器，然而会报错：

> "server" directive is not allowed here in /etc/nginx/nginx.conf

【/root/nginx/log/error.log 会记录错误日志】

经过实际查验容器内的文件发现需要自己映射的文件应该是`-v /root/nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf`

以下为排查过程，同时也是 Docker 比较重要的使用姿势。

```bash
# docker rm --force nginx #删除已创建的容器

# 创建并进入容器内的命令行
docker run -it --name "nginx" -p 80:80 nginx /bin/bash

# 对于运行中的容器，可通过其ID进入
docker ps
docker exec -it 10ff26ba7281 /bin/bash

# 可以使用ls,cd等命令浏览容器内的文件
# exit退出查看

# 容器内部
find ./ -name "nginx.conf"
# 得到结果并留存
# ./etc/nginx/nginx.conf
exit #退出容器

# 退出容器后
# docker cp 容器id:容器内文件路径 目标路径
docker cp 10ff26ba7281:/etc/nginx/nginx.conf /root/nginx/conf/nginx.conf

# 实际排查后发现应该使用conf.d/default.conf进行映射
docker cp 10ff26ba7281:/etc/nginx/conf.d/default.conf /root/nginx/conf.d/default.conf
```

### 其他

> Get https://registry-1.docker.io/v2/****: unauthorized: incorrect username or password

```shell
cd /var/lib/docker/overlay2/
du -sh *
```

<!--357-->
