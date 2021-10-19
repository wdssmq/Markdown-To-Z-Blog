---
title: 「Docker」Nginx 反代探究
tags:
- Docker
- Nginx
- 折腾
categories:
- 电脑网络
---

### 日常跑题的开场

略早之前偶然间看到了`RSSerpent/RSSerpent`这个项目，定位和 RSSHub 一样，使用 Python，不像 RSSHub 每份「规则/路由」都要在代码文件内引入，RSSerpent 选取了「插件/化可拆装」的引入方案；

<!--more-->

虽然作者在国庆期间终于补了波插件开发文档，在翻过了「环境配置」这座大山后也确实写出了两条规则；（其中一条是给官方路由的 Pr）

然而明明在开发调试时可以抓取内容并输出 RSS，可是实际部署出来并不能用的样子-_-!；

毕竟是新项目，慢慢等完善吧；

其实另一方面，RSSHub 对我来说还算够用，最大的问题也并不是规则，而是实例的可用性——比如实例整个挂掉，或者某条规则在该实例上不再可用——即使自建也无法避免；

（昨天发现`rss.shab.fun`证书过期了，刚看了下到是很快续上了；）

虽然每天都有看，但是某条订阅好久没更新了这种情况，对人的敏感性要求太高了；

> 果然目前最好的方案是这个：
>
> [「折腾」GitHub Actions 反代 RSSHub + 多实例轮询\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100309739.html "「折腾」GitHub Actions 反代 RSSHub + 多实例轮询\_电脑网络\_沉冰浮水")
>
> 不过之前还是被意料之外的原因波及了：
>
> [「小事」Python 的 Docker 镜像更新了一波\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20210820542.html "「小事」Python 的 Docker 镜像更新了一波\_杂七杂八\_沉冰浮水")

（果然每次都会变成碎碎念.jpg）

### 正文

这篇文章的起因是搞了下边东西；

wdssmq/proxy\_nginx: Nginx Docker 化镜像，适合用于反代；：

[https://github.com/wdssmq/proxy_nginx](https://github.com/wdssmq/proxy_nginx "wdssmq/proxy\_nginx: Nginx Docker 化镜像，适合用于反代；")

↑ 虽然是个代码库，但是弄完感觉更像是水了篇使用教程，顺便带了个 Git 库；

`README.md`里写了不少笔记，Docker 化部署 Nginx 环境，外加如何将`/etc/nginx/*`各种相关的配置以映射的的方式实现自定义，还研究了怎么配置 SSL 证书；

> 前边已经水过的一篇：
>
> [Docker 内 php-nginx 的伪静态相关\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20190813019.html "Docker 内 php-nginx 的伪静态相关\_电脑网络\_沉冰浮水")

然后发现把「Nginx 配置反向代理」塞进去感觉会很长；「- 虽然拆出到这里也很长.jpg -」

----

需求描述：

已经使用 Docker 部署了一个 RSSHub 实例，跑在默认的`1200`端口上，想另外部署一个单独的 Nginx 容器进行反代；

镜像基于`webdevops/php-nginx:7.4`，并且提取了`/etc/nginx`用于自定义映射；

预置文件比较多，还有很多已经废弃却没删除的，梳理过包含关系后得出总结如下：

`nginx/conf.d/`文件内用于放置需要全局引入的文件，或者说写在端口监听外部；

`nginx/vhost.common.d/*.conf`则分别在`80`和`443`各自的`server {}`内部引入；

> 其实主要是想实现多个 RSSHub 实例反代的，好像设计上并不支持我预想的用法；

按路径分别写入下边配置：

```conf
; nginx/conf.d/5-proxy.conf
upstream rss1200 {
    server getrss2021.xyz:1200;
}
```

```conf
; nginx/vhost.common.d/5-proxy.conf
location /rss/ {
    proxy_set_header Host $host/rss;
    proxy_pass http://rss1200/;
}
```

容器相互是隔离的，需要确保`*:1200`是能访问到的地址，或者将容器加入同一网络内使用容器名用于寻址；

之后映射进 Docker 容器或重启已有容器即可；

所以现在用`https://getrss2021.xyz/rss/`就可以访问到我搭建的 RSSHub 实例；

**结语：**

其实就当前示例来说，也可以不使用 upstream 模块，然而把所以「可以」都写成过程果然也不太现实；
