---
title: 「小事」Python 的 Docker 镜像更新了一波
tags:
- 小事
- Python
- Docker
categories:
- 杂七杂八
---

### 零

一直忘记设置 aText 开机自启.jpg

### 一

这篇文章是使用 VSCode 写就后使用 API 发布到 Z-BlogPHP 的，具体实现见下边项目；

<!--more-->

> wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb：
>
> [https://github.com/wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb")

前几天写另一篇文章时，发现 API 发布失败了；「[说说 base64 编码\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/2019112672.html "说说 base64 编码\_电脑网络\_沉冰浮水")」

Actions 日志内报错：`Python 3.7 was not found on your system...`；

API 发布是用 Python 实现然后使用 VaultVulp/action-pipenv 这个动作库调用触发；

「- 话说「Github Actions」的中文翻译是啥？ -」

Python 版本要求及依赖写在「Pipfile」文件内。

```conf
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[scripts]
build = "python api.py"

[packages]
markdown = "3.3.4"
requests = "2.26.0"
python-frontmatter = "1.0.0"

[requires]
python_version = "3.9"
```

一开始用的是`python_version = "3.7"`，因为能用就没动，然后现在不能用了，理论上应该可以直接`python_version = "3.*"`吧；

### 二

当时是 8 月 18 号，然后今天是 20 号……

这几天又又发现 B 站相关的 RSS 没有新推送，因为各种 RSSHub 实例总是挂掉，所以同样用 GitHub Actions 搞了个「多实例反代」——

> wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询：
>
> [https://github.com/wdssmq/proxy_rsshub](https://github.com/wdssmq/proxy_rsshub "wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询")

「- 其实对于这个项目，yml 比 json 更适合作为配置项吧 -」

然后今天终于看了一眼记录，果然是挂掉了，然后才意识到这边的「Pipfile」也要改；「[Actions · wdssmq/proxy\_rsshub](https://github.com/wdssmq/proxy_rsshub/actions "Actions · wdssmq/proxy\_rsshub")」

### 三

这次问题的溯源；

VaultVulp/action-pipenv 本质是将工作区文件映射进 Docker 容器中进行处理，而使用的镜像是现场构建的，其 Dockerfile 定义中，默认使用了`python:3`的大版本号；

```conf
ARG PYTHON_IMAGE_VERSION=3
FROM python:$PYTHON_IMAGE_VERSION
……
```

而就在 18 号那天，对应的依赖镜像更新了一波——「[python Tags | Docker Hub](https://hub.docker.com/_/python?tab=tags "python Tags | Docker Hub")」；

「- 话说这个「官方镜像」是指「DockerHub 官方」还是「Python 官方」 -」

「- 严格来说并没能得到什么经验教训的感觉.jpg -」
