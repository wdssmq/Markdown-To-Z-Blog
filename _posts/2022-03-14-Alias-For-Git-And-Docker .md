---
title: 「折腾」git 及 docker 命令快捷输入
date: 2022-03-14 00:02:09
tags:
- 折腾
- Git
- Docker
categories:
- 电脑网络
id: 2804
alias: 20171130103
---

本来是想折腾「WSL2 + Docker 安装堡塔面板」的，然而很多命令需要频繁输入，所以决定先弄个快捷输入；

<!--more-->

Docker 部分其实是搜狗输入法的快捷输入短语 /doge；

附带了一条快捷安装`cnpm`的规则；

```ini
cnpm,3=npm install -g cnpm --registry=https://registry.npmmirror.com
; -----
dks,3=sudo service docker start
dks,4=sudo service docker stop
; -----
dkia,3=sudo docker image ls
dkrmi,3=sudo docker rmi
dkrmi,4=sudo docker rmi -f
; -----
dkst,3=sudo docker start
dkst,4=sudo docker stop
; -----
dkps,3=sudo docker ps -a
dkrm,3=sudo docker rm --force
dkrm,4=sudo docker rm
```

Git 命令，则可以设置在`~/.gitconfig`内：

使用时可以直接 `git br` 或 `git co`；

```ini
[core]
    fileMode = false
[alias]
    # status
    s   = status
    ss  = status --short --branch

    # stash
    sh  = stash
    shp = stash pop
    shl = stash list
    shs = stash save
    sha = stash apply
    shd = stash drop

    # branch
    br  = branch
    bra = branch -a
    brv = branch -a -v
    brm = branch -m
    brh = branch -h
    co  = checkout
    cob = checkout -b
    sw  = switch
    swc = switch -c

    # tag
    tgn = tag -n
    tgr = ls-remote --tags origin
    tgp = push origin --tags

    # remote
    rea = remote add
    res = remote set-url
    rev = remote -v
    ren = remote rename
    rem = remote remove
    re  = remote

    # fetch
    fe  = fetch
    fea = fetch --all
    fep = fetch -p
    # fo  = fetch origin
    # fop = fetch origin -p

    # merge
    mr  = merge
    mnc = merge --no-commit
    # msq = merge --squash

    # commit
    ci  = commit
    cim = commit -m

    # push
    pus = push origin
    put = push origin --tags

    # reset
    res = reset --soft HEAD^
    rem = reset --mixed HEAD^
    resc = reset --soft
    remc = reset --mixed

```

本文会以实际需要慢慢补充条目，你也可以参考下边文章：

git 快捷命令 - 掘金

`https://juejin.cn/post/6844904036785717262`

------------------

待研究：

sudo docker ps -a -q

sudo docker service ls -q

sudo docker service rm

----------------

```bash
sudo docker rm --force baota
sudo docker run --name baota \
  --net=net_web \
  -p 80:80 -p 443:443 -p 8888:8888 -p 888:888 \
  -v ~/wwwroot2:/www/wwwroot \
  --privileged=true --shm-size=1g \
  --restart always  \
  -d pch18/baota
# \n

```
