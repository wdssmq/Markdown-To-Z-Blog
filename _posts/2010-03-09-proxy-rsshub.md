---
title: 【折腾】GitHub Actions 反代 RSSHub + 多实例轮询
tags:
- GitHub
- RSSHub
- Python
- 折腾
categories:
- 电脑网络
id: 142
alias: 20100309739
zhihu: https://zhuanlan.zhihu.com/p/367656502
csdn: https://blog.csdn.net/qq_15022221/article/details/116125459
---

## 软件名称

wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询


## 应用平台

* GitHub Workflows / GitHub Actions
* Python


## 推荐类型

【开发者自荐】


## 一句简介

定时抓取 RSSHub 站点内容并缓存在 GitHub 库中，RSSHub 实例故障或被源站屏蔽时也不需要更换阅读器中的地址；


## 应用简介

- 核心功能为 Python 实现，使用 GitHub Actions 定时触发；
- 需要编辑`config.json`添加订阅规则，执行时依次向所设置的 RSSHub 站点请求相应规则；
- 抓取成为后会保存在 xml 文件夹中，对应的链接地址自动更新至`README.md`中；
  - 将匹配如下模式并自动替换——`---start---(.|\n)*?---end---`；
- `proxy_rsshub/.github/workflows/index.yml` 内可设置执行间隔；【【对于 RSS 来说 6 小时已经很合理了吧】】


## 官方网站 && 应用商店地址

wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询：

[https://github.com/wdssmq/proxy_rsshub](https://github.com/wdssmq/proxy_rsshub "wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询")
