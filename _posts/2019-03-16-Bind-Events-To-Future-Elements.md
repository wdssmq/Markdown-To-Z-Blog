---
title: 「备忘」原生 JS 监听未来元素事件实例
date: 2019-03-16 11:24:59
tags:
- 备忘
- JavaScript
- 折腾
- 微博
categories:
- 电脑网络
id: 2899
alias: 20190316472
csdn: https://blog.csdn.net/qq_15022221/article/details/114182790
---

最近发现的一个社区化（？）或者说分布式的微博系统——Mastodon（官方中文译万象，网民又称长毛象），简单说就是任何人都可以使用其源码搭建一个微博站点并各自允许用户注册，不同站点的用户又可以相互发现和关注……

<!--more-->

> ↓↓↓
>
> 注册 - 长毛象中文站
>
> [https://acg.mn/invite/DXwRtTMG](https://acg.mn/invite/DXwRtTMG "注册 - 长毛象中文站")
>
> Mastodon - 搜索结果 - 知乎
>
> [https://www.zhihu.com/search?type=content&q=Mastodon](https://www.zhihu.com/search?type=content&q=Mastodon "Mastodon - 搜索结果 - 知乎")
>
> ↑↑↑

其实关于 Mastodon 的介绍就只有上边这些。详细请自行注册了解……

问题是关注了几个更新纸片人的机器人后，发现 NSFW 太烦人了，，这个到是找到了现成的脚本：

> ↓↓↓
>
> Mastodon NSFW Remover
>
> [https://greasyfork.org/zh-CN/scripts/29228-mastodon-nsfw-remover](https://greasyfork.org/zh-CN/scripts/29228-mastodon-nsfw-remover "Mastodon NSFW Remover")
>
> ↑↑↑

然而点击图片后加载大图实在略慢。。试着写了下边代码实现在鼠标划过图片时自动替换为大图（虽然感觉效果和效果有偏差，先发出来再调整）

```js
// 原生js未来元素事件监听的写法 - 笑场 - CSDN博客
// https://blog.csdn.net/xianglikai1/article/details/76100177

// JS获取元素属性和自定义属性 - 马优晨 - CSDN博客
// https://blog.csdn.net/qq_24147051/article/details/77976844
(function () {
  "use strict";
  function $n(e) {
    return document.querySelector(e);
  }
  function $na(e) {
    return document.querySelectorAll(e);
  }
  // 直觉应该用mouseenter，然而并不是
  $n(".app-holder").addEventListener("mouseover", function (e) {
    console.log(e.target);
    console.log(e.target.nodeName);
    console.log(e.target.className || "class为空");
    // 实际代码
    if (e.target.nodeName === "IMG") {
      let src = e.target.getAttribute("src");
      src = src.replace("small", "original");
      e.target.setAttribute("src", src);
      let srcset = e.target.getAttribute("srcset");
      srcset = srcset.replace("small", "original");
      e.target.setAttribute("srcset", srcset);
    }
  }, false);
})();
```

<!--2899-->
