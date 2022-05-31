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

---------

步骤：

1、注册并登录：[https://workers.cloudflare.com/](https://workers.cloudflare.com/ "Cloudflare Workers®")；

2、「创建服务」 → 可自行决定「服务名称」 → 「启动器」随便选一个就好 → 「创建服务」；「新注册可能要先设置`子域`」

3、进入新建服务的内页 → 「快速编辑」；

4、复制下边代码填入项目内，`cf_worker_host`修改为你的服务地址 → 「保存并部署」；


```js
addEventListener("fetch", event => {
    event.respondWith(handleRequest(event.request))
})

// 如果有其他 RSSHub 地址也可以补充在这里
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
