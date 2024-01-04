---
title: 「折腾」GM_脚本 + CF Workers KV 半自动收集 B 用户投稿转为 RSS
date: 2024-01-04 11:03:24
tags:
 - GM_脚本
 - Cloudflare
 - 折腾
 - RSS
categories:
 - 电脑网络
id: 1239
alias: 20120519803
---

## 一

终于还是尝试了这种方式什么的。。。

<!--more-->

有借助 RSSHub 订阅 B 站用户投稿和番剧更新，几年来整体还算稳定，想着万一反爬变严了就干脆用 `GM_脚本` 直接从浏览器里抓取数据到远程存储的方式来实现，，然后 2023-12 开始终于发生了。。。

就结果来说，本文所述方案的代码已经基本完成了，但是终究是不能自动运行，然后定位上也和标准的 RSS 需求不太一样，，大概还是要研究下给 RSSHub 配置 cookie 。。。

## 二

关于功能定位，对于部分 up 主，会希望能把历史投稿也看一遍，然而总量上就会很多，采取了基于时间和条目序号分页的方案，以 m 天划分周期，当前周期内输出固定的 n 条数据这样，，具体看代码吧。。。


> wdssmq/later-url-cf: 使用 Cloudflare Workers KV 存储服务收集网址并以 RSS 输出；
>
> [https://github.com/wdssmq/later-url-cf](https://github.com/wdssmq/later-url-cf "wdssmq/later-url-cf: 使用 Cloudflare Workers KV 存储服务收集网址并以 RSS 输出；")


> userscript/packages/later-url at main · wdssmq/userscript
>
> [https://github.com/wdssmq/userscript/tree/main/packages/later-url#readme](https://github.com/wdssmq/userscript/tree/main/packages/later-url#readme "userscript/packages/later-url at main · wdssmq/userscript")


## 三

> Bilibili2RSS - 为你喜爱的任意 B 站「番剧」添加 RSS 更新通知\[Web\] - 小众软件
>
> [https://www.appinn.com/bilibili2rss/](https://www.appinn.com/bilibili2rss/ "Bilibili2RSS - 为你喜爱的任意 B 站「番剧」添加 RSS 更新通知\[Web\] - 小众软件")
>
> ↑ 当时的代码并没有保留……

2017 年的时候拿 PHP 写过一个订阅 B 站番剧更新的工具，后来知道 RSSHub 的存在；

RSSHub 最早也是需要针对特定番剧添加到一条订阅到阅读器，所以 PR 提交了一条「用户追番列表」的路由；

> 增加：用户追番列表 by wdssmq · Pull Request #2735 · DIYgod/RSSHub
>
> [https://github.com/DIYgod/RSSHub/pull/2735](https://github.com/DIYgod/RSSHub/pull/2735 "增加：用户追番列表 by wdssmq · Pull Request #2735 · DIYgod/RSSHub")
>
> ↑ 标记了「反爬严格」但是大概还能用？

`然后果然不太懂 Github 的 PR/ISSUE 搜索功能.jpg`

RSSHub 的问题是，官方站可能被针对性反爬，自建维护更新又比较麻烦，所以选用了对多个 RSSHub 实例进行反代的方式；


> wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询
>
> [https://github.com/wdssmq/proxy_rsshub](https://github.com/wdssmq/proxy_rsshub "wdssmq/proxy\_rsshub: 使用 GitHub Actions 反代 RSSHub + 多实例轮询")
>
> ↑ 这个可能不符合 GitHub Actions 的使用条款，所以用了一段时间后就停用了。。


> wdssmq/rsshub-cf: Cloudflare Worker 反代 RSSHub
>
> [https://github.com/wdssmq/rsshub-cf](https://github.com/wdssmq/rsshub-cf "wdssmq/rsshub-cf: Cloudflare Worker 反代 RSSHub")
>
> ↑ 本来这个方案相对靠谱，然而 B 站强化了一波反爬。。。
