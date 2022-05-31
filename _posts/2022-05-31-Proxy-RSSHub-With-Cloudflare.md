---
title: 「折腾」Cloudflare Worker 反代 RSSHub
tags:
- 折腾
- RSSHub
categories:
- 电脑网络
id: 1411
alias: 20100219897
---

之前试着拿来当图床：「[「折腾」关于 2021 年末仍然没有完备的图床方案这件事\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20211225085.html "「折腾」关于 2021 年末仍然没有完备的图床方案这件事\_电脑网络\_沉冰浮水")」

不过没多久不能直连了，，也是心塞；

<!--more-->

所以本方案需要自行解决阅读器到`workers.dev`的连接；

```js
addEventListener("fetch", event => {
    event.respondWith(handleRequest(event.request))
})

const proxyList = [
    "https://rss.shab.fun/",
    "https://rsshub.rssforever.com/",
    "https://rsshub.app/",
];

async function handleRequest(request) {
    // Cloudflare Workers 分配的域名
    cf_worker_host = "https://rsshub.wdssmq.workers.dev/";

    // 随机选择一个代理
    let proxy = proxyList[Math.floor(Math.random() * proxyList.length)];

    // 替换
    url = request.url.replace(cf_worker_host, proxy);

    return fetch(url);

    // return new Response(JSON.stringify({ proxy, url }), {
    //     headers: { "Content-Type": "application/json" },
    // });

}
```

其实更早有这个方案：「[【折腾】GitHub Actions 反代 RSSHub + 多实例轮询\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100309739.html "【折腾】GitHub Actions 反代 RSSHub + 多实例轮询\_电脑网络\_沉冰浮水")」

然而严格来说是违反 GitHub 的 TOS 的，虽然用了蛮久了已经；
