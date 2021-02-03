---
title: 【折腾】GM脚本修改B站番剧链接为我的追番
tags:
- JavaScript,折腾,GM脚本,B站
categories:
- 未分类
---

### 需求描述

![图1](https://i.loli.net/2021/01/06/2rK5GdiCH7nXSaf.png)

在B顶部导航里有一个[番剧]链接，[主站]和[游戏中心]中心那个，指向链接是：

`https://www.bilibili.com/anime/` 【链接1】

然而我每次点这个链接是因为进去后有一个[我的追番]区域，然后点区域标题后边的[更多]会进入：

`https://space.bilibili.com/44744006/bangumi` 【链接2】

感觉很麻烦，所以决定直接把【链接1】替换为【链接2】

<!--more-->

### 开始

浏览器审查元素，该链接的html代码是：

`<a href="//www.bilibili.com/anime/" target="_blank" class="link">番剧</a>`

并没有特定的ID或类名供使用，但是可以使用【attribute（属性）】相关选择器中的【href属性值以"/anime/"结尾的a元素】。[^attribute选择器参考链接]

`$("a[href$='/anime/']").length`

在控制台运行上边代码↑，目的有三：

1、验证下B站有没有引入jQuery；
2、确定下选择器是不是对；
3、确定下会不会选到多个元素；

结果是[动态首页]输出`1`，然而B站首页输出`undefined`，虽然不知道为什么，但是先只说前者，因为网页版很少需要进首页；

理论上可以直接执行下边代码：

`$("a[href$='/anime/']").attr("href","https://space.bilibili.com/44744006/bangumi");`

↑其作用是，将【选定元素】的【href】这一属性的【值】设置为输入的内容，在本例就就是预定要修改的【链接2】，然而问题是这里写死了我的uid，，想要通用的话自动获取当前登录用户的uid比较好；

![图2](https://i.loli.net/2021/01/06/TjJnyFqIS5s1Ka4.png)

↑在控制台直接搜索自己的uid，发现三个结果；

`$("a.count-item[href^='//space']").length`

↑这次的选择器是这个，，以【XXX】开头，这里限定了[.count-item]选择器，不加的话结果有35个。。

虽然结果有三个，但是直接操作的话会对第一个生效：

`$("a.count-item[href^='//space']").attr("href")`

读取元素的属性值↑

完整代码↓

```js
// 番剧链接改为我的追番
(() => {
  // <a href="//www.bilibili.com/anime/" target="_blank" class="link">番剧</a>
  // $("a[href$='/anime/']").length
  // <- 1
  // $("a.count-item[href^='//space']").length
  // <- 3
  // $("a.count-item[href^='//space']").attr("href")
  // <- "//space.bilibili.com/44744006/fans/follow"
  // ---
  const uid = ((url) => {
    // console.log(url.match(/\d+/));
    return (url.match(/\d+/))[0];
  })($("a.count-item[href^='//space']").attr("href"));

  $("a[href$='/anime/']").attr(
    "href",
    `https://space.bilibili.com/${uid}/bangumi`
  );
})();
```

↓↓最后在浏览器插件中新建一个用户脚本，然后将代码贴进去；

![图3](https://i.loli.net/2021/01/06/mywjg9L7KCaN4pr.png)

[^attribute选择器参考链接]: https://www.w3school.com.cn/cssref/css_selectors.asp
