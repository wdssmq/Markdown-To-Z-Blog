---
title: 「折腾」关于 2021 年末仍然没有完备的图床方案这件事
tags:
- 折腾
- CDN
- 独立博客
categories:
- 电脑网络
id: 30
alias: 20211225085
---

早年没有「图床」概念时写博客都是把图片作为附件传博客程序里，而我的选择更是「尽量不发带图的东西」。。

<!--more-->

慢慢就变成了习惯，，后来再偶尔需要发图时就传到`sm.ms`这类公益图床；

> 使用 GitHub Actions + Markdown 更新 Z-Blog 博客：
[wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb")

图片和 .md 文件放在一起，日常编辑用 VSCode + [Markdown All in One 插件](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one "Markdown All in One - Visual Studio Marketplace")，然后用 Typora + PicGo 上传引入的图片；

且不说 Typora 现在收费了，最大的问题上传图片时不支持带有`#`号的路径。。。

前边「[「原神」关于满地图打素材却发现可以自动追踪这件事\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20130808670.html "「原神」关于满地图打素材却发现可以自动追踪这件事\_杂七杂八\_沉冰浮水")」一文中也有说过，jsDelivr 现在虽然恢复使用了，作为图床总有些担心，，// 虽然我已经在各种地方用作 CDN 了。。

总之现在决定研究下 Cloudflare Workers 给 GitHub 当 CDN 的方案；

> Cloudflare Workers 反代使用 GitHub 仓库搭建的图床 - 森见鹿的博客：
>
> [http://senjianlu.com/2021/12/cloudflare-workers-image/](http://senjianlu.com/2021/12/cloudflare-workers-image/ "Cloudflare Workers 反代使用 GitHub 仓库搭建的图床 - 森见鹿的博客")

图片地址对应：

`https://raw.githubusercontent.com/wdssmq/Markdown-To-Z-Blog/main/doc/001.orig.png`

`https://img.wdssmq.workers.dev/doc/001.orig.png`

实际配置步骤见：「[「折腾」Cloudflare Worker 反代 RSSHub\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100219897.html "「折腾」Cloudflare Worker 反代 RSSHub\_电脑网络\_沉冰浮水")」

```js
addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {

  // Cloudflare Workers 分配的域名
  // const cf_worker_host = "img.wdssmq.workers.dev";

  // 同时绑定自己的域名
  const cf_worker_host = new RegExp("img.wdssmq.workers.dev|img.wdssmq.com","g");

  // GitHub 仓库文件地址
  const github_host = "raw.githubusercontent.com/wdssmq/Markdown-To-Z-Blog/main";

  // 替换
  const url = request.url.replace(cf_worker_host, github_host);
  return fetch(url);
}
```

2022-06-17：

然后也终于实现了在 md 中直接写相对地址，然后发布时自动替换；

-----

wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb：

[https://github.com/wdssmq/Markdown-To-Z-Blog#图床](https://github.com/wdssmq/Markdown-To-Z-Blog#%E5%9B%BE%E5%BA%8A "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb")

-----

使用 GitHub Actions + Markdown 更新 Z-Blog 博客\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20210224498.html](https://www.wdssmq.com/post/20210224498.html "使用 GitHub Actions + Markdown 更新 Z-Blog 博客\_电脑网络\_沉冰浮水")
