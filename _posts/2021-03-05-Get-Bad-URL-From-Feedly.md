---
title: 【折腾】GM_脚本“取回” Feedly 内的订阅源地址
date: 2021-03-05 18:49:42
tags:
- GM_脚本
- RSS
- 折腾
categories:
- 电脑网络
id: 425
alias: 20210305305
zhihu: https://zhuanlan.zhihu.com/p/354923144
jianshu: https://www.jianshu.com/p/9343042e391d
csdn: https://blog.csdn.net/qq_15022221/article/details/114411325
---

### 虚拟桌面的快捷键仍然绝赞记不住 ing

相关文章：20210227485

Todo：[如何在 Hexo 的博文中引用自己的文章 | 晨星的个人博客](https://www.mls-tech.info/hexo/hexo-use-internal-link/ "如何在Hexo的博文中引用自己的文章 | 晨星的个人博客") ←←

以及，mdlint 插件要求英文和中文之间要有空格，所以也是略纠结；

<!--more-->

### 需求描述

Feedly 中查看已订阅项目时，地址栏显示是这样：

`https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Ffeed.wdssmq.com`

`https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fwww.wdssmq.com%2Ffeed.php`

「订阅源地址」部分是转码过的，虽然对于比较短的地址还是可以直接人肉识别出来，另外，在「`···`→`More settings`」中也是可以看到源地址回显的。。

<details markdown='1'><summary>吐槽：</summary>
【果然从博客建议之初就是「不想配图」星人，，，即使改用「Markdown + 免费图床」后也没能提升多少；

【Feedly 这个回显也是过了很久才半途加上的。。
</details>

但是，对于某些出问题的订阅源，会提示下边信息然后不给你查看源地址的选项：

```html
<div id="feedlyPageFX" class="container centered">
  <h2 class="Heading Heading--h2">
    Feed not found
    <div class="sub">Wrong feed URL or dead feed</div>
  </h2>
</div>
```

作为「GM_脚本」狂魔果然还是决定自己解决这个痛点顺便水一篇文章；

### 代码实现及讲解

- 需要这样“取回”订阅源的频度还是略低的，所以设置为点击触发就好；
- 因为 Feedly 使用的是前端渲染机制，上边提示对应的 html 在「源码查看」中其实并不存在，也就是属于「未来元素」，所以「监听事件」需要设置在会包含该「未来元素」的现存的元素节点上，本例中就是`body#box`；

```html
<body id="box" class="home">
…………
</body>
```

- 监听事件：点击、按下、弹起， 这里都可以，代码中选用了`mouseup`；
- 当有错误提示的元素被点击时，执行后续操作，主要有三步：
    - 从当前地址中拿到订阅源的部分；
    - 解码；
    - 输出到页面；
- ↑前两步顺序可以互换；
- 输出到页面时使用了[element.insertAdjacentHTML - Web API 接口参考 | MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/Element/insertAdjacentHTML "element.insertAdjacentHTML - Web API 接口参考 | MDN")，类似 JQuery 中的`.append()`方法；
- 具体输出到哪个元素中要也要分析和尝试，然后视情况使用上现有的样式类；

```js
(function () {
  "use strict";
  function $n(e) {
    return document.querySelector(e);
  }
  function $na(e) {
    return document.querySelectorAll(e);
  }
  function addEvent(element, evnt, funct) {
    return element.addEventListener(evnt, funct, false);
  }
  // 拿回订阅源地址
  // 绑定监听事件到 div#box 上
  addEvent($n("#box"), "mouseup", function (event) {
    // 输出触发事件的元素
    console.log(event.target);
    // 根据内容判断是否执行相应操作
    const elText = event.target.innerHTML;
    if (
      // elText.indexOf("Feed not found") > -1 ||
      elText.indexOf("Wrong feed URL") > -1 // 保证提示信息中的两行都能触发
    ) {
      // 内部再输出一次确定判断条件正确
      console.log(event.target);
      // 拿到解码后的订阅源地址
      const curUrl = ((url) => {
        return url.replace("https://feedly.com/i/subscription/feed/", "");
      })(decodeURIComponent(location.href));
      // 输出到页面中
      $n("#feedlyPageFX h2").insertAdjacentHTML(
        "beforeend",
        `<div class="sub">${curUrl}</div>`
      );
    }
  });
})();
```

### 结束

自用 Feedly 完整脚本地址见：

```js
// ----------------------------
// @raw    https://github.com/wdssmq/userscript/tree/master/feedly
// @raw    https://greasyfork.org/zh-CN/scripts/381793
// ----------------------------
// @link   https://afdian.net/@wdssmq
// @link   https://github.com/wdssmq/userscript
// @link   https://greasyfork.org/zh-CN/users/6865-wdssmq
// ----------------------------
```

另一篇相关文章：20100222433
