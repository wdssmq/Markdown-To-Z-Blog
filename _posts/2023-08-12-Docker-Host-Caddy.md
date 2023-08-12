---
title: 「折腾」Docker 部署 Caddy
date: 2023-08-12 13:41:06
tags:
 - 折腾
 - Web
 - Docker
 - 备忘
categories:
 - 电脑网络
id: 64
alias: 20100717821
---

除了本站所在的机子外，还另外有两台半 VPS，那半台因为是 NAT 在写本文时仍然在吃灰，剩下两台姑且按侧重承担了些任务；

<!--more-->

所以上边涉及总共四家 IDC，这里会随机给出它们的推广链接：

> [ShortSth:主机云,DesiVPS,RackNerdVPS,iHostART][/ShortSth]

主博客用的 Z-BlogPHP，新文章是写 Markdown 发到 GitHub 再走 API 发布的，使用的 meta 结构和 hexo 基本一样，所以也可以简单用 hexo 生成一个静态站，虽然也可以托管 GitHub Pages 上，只是一来和常规更新方式不一样，二来又有额外的 VPS 可以用，就选择了自己搭建；

使用的域名是 `blog.wdssmq.com`，然后相应的两个 Git 仓库 [[md2zb]] [[hexo-blog]]，用的主题 [[maupassant]]，各自对应的链接见文章结尾；

将主仓库作为 submodule 添加到 hexo 仓库中，使用软连接映射文章目录到 `source/_posts`，这部分之前水过一篇了，链接见文章结尾；「- 另外写了个 bash 脚本定时运行实现自动拉取文章更新然后构建 `public/` -」

当时选择了 Caddy 作为 Web 服务器，还可以自动申请 SSL 证书，不过直接使用感觉有些微妙，服务挂掉后重启略麻烦，所以后来在另一台机子上试了本身就是 Docker 项目的 NginxProxyManager，然而 hexo 本身还是要有个静态 web 服务，再之前那台不能装 Docker 的机子也过期扔掉了，所以打算再试下 Docker 部署 Caddy；

> 吐槽：先是搜索到一篇知乎文章，结果 Caddyfile 报语法错误，发现是镜像太久了，又重新找到了官方镜像；
>
> caddyserver/caddy-docker:
>
> [https://github.com/caddyserver/caddy-docker](https://github.com/caddyserver/caddy-docker "caddyserver/caddy-docker: Source for the official Caddy v2 Docker Image")
>
> 使用说明（#Docker Compose）:
>
> [https://github.com/docker-library/docs/tree/master/caddy#docker-compose-example](https://github.com/docker-library/docs/tree/master/caddy#docker-compose-example "docs/caddy at master · docker-library/docs")

下边配置基于官方示例修改：

```yaml
version: "3.7"

services:
  caddy:
    container_name: caddy
    image: caddy:latest
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
      - "443:443/udp"
    volumes:
      - ./data/caddy/Caddyfile:/etc/caddy/Caddyfile
      - /root/Git/blog-hexo/public:/srv
      - caddy_data:/data
      - caddy_config:/config

volumes:
  caddy_data:
    external: true
  caddy_config:

  # 需要执行命令创建 caddy_data
  # docker volume create caddy_data

```

----

↑ `caddy_config` 内好像会有个 `autosave.json`，目测是由 `Caddyfile` 解析转换而来，会自动生成和更新，所以不用管它，甚至不指定挂载卷也行的感觉？

↑ `caddy_data` 里边存放申请到的证书之类的，理论上不需要自己管理或备份，但是如果删除容器后再启动又要重新申请也挺浪费的，所以指定一个由 Docker 管理的卷，然后`external: true` 则表示相对于当前 `docker-compose.yml` 内的「容器组」来说它是「外部的」，简单来说就是不会因为执行  `docker-compose down` 而被删除；

这部分算是我对「挂载卷」部分的理解；然后像 `Caddyfile` 和 `/srv` 这种直接指定一个具体的宿主机路径的，感觉可以用「挂载目录」来作描述上的区分，用户或其他非 Docker 程序可以更方便地直接访问和管理后者，同时又允许 Docker 容器使用；

----

之后只需要配置 `Caddyfile` 即可：

```caddyfile
blog.wdssmq.com {
	# 重定向错误的 tag 链接
	@tags {
		path_regexp tag /tags/(?P<n1>[^/]+)_(?P<n2>[^/]+)
	}
	redir @tags /tags/{re.tag.n1}-{re.tag.n2} permanent
	# root 目录
	root * /srv
	encode zstd gzip
	file_server
}

bbs.canihave.fun {
	reverse_proxy /* 172.17.0.1:8091 {
		# header_up Host {upstream_hostport}
		header_up X-Real-IP {remote}
	}
}

```

\----------------

「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20100604351.html](https://www.wdssmq.com/post/20100604351.html "「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水")

----

「折腾」Git Submodule 探究\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20100710361.html](https://www.wdssmq.com/post/20100710361.html "「折腾」Git Submodule 探究\_电脑网络\_沉冰浮水")

----

wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb：

[https://github.com/wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb")

----

wdssmq/blog-hexo：

[https://github.com/wdssmq/blog-hexo](https://github.com/wdssmq/blog-hexo "wdssmq/blog-hexo")

----

wdssmq/maupassant-hexo: A simple Hexo theme forked from icylogic.：

[https://github.com/wdssmq/maupassant-hexo](https://github.com/wdssmq/maupassant-hexo "wdssmq/maupassant-hexo: A simple Hexo theme forked from icylogic.")
