---
title: 「代码片段」当网页元素可见时……
date: 2019-07-01 15:52:48
tags:
- 代码
- JavaScript
categories:
- 电脑网络
id: 2919
alias: 20190701815
---

当元素滚动到可视区域时执行指定操作，比如应用 `Animate.css` 动画效果

```javascript
// 原生 JS 选择器
function query(selector) {
  return Array.from(document.querySelectorAll(selector));
}
// 使用构造函数创建对象并指定回调函数
const observer = new IntersectionObserver(function (changes) {
  // 回调参数是数组，成员为 IntersectionObserverEntry 对象
  changes.forEach(function (change) {
    const container = change.target;
    // console.log(change.intersectionRatio);
    // 大于 0 时表示可见
    if (change.intersectionRatio > 0) {
      // console.log(container);
      container.classList.add("flip", "animated");
    } else {
      container.classList.remove("flip", "animated");
    }
  });
});
// observe 方法用于对指定一个元素开启监听
query(".section-top img").forEach(function (item) {
  // console.log(item);
  observer.observe(item);
});

```

「- -」「- -」「- -」「- -」

IntersectionObserver API 使用教程 - 阮一峰的网络日志

`http://www.ruanyifeng.com/blog/2016/11/intersectionobserver_api.html`

Animate.css

`https://daneden.github.io/animate.css/`

<!--2919-->
