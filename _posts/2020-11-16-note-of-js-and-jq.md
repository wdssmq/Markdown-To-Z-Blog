---
title: 【备忘】JavaScript 及 jQuery 常用代码
date: 2021-01-04 21:30:29
tags:
- JavaScript
- JQuery
- 备忘
categories:
- 电脑网络
id: 3107
alias: 20201116687
---

JavaScript 或 jQuery 中各种常用的代码总结；

<!--more-->

移除 class，移除属性：

```js
// 移除class，移除属性
$("input").removeClass("hidden").removeAttr("disabled");
```

「- -」「- -」「- -」「- -」

jQuery 操作 Select：

```js
// https://www.cnblogs.com/shanyou/archive/2011/07/11/2103422.html
// 可直接使用val(）方法赋值
$('select').val(2);
```

「- -」「- -」「- -」「- -」

关于正则分组命名及回调替换：

```js
function fnReplace(html, post_id) {
  const fnRegxCB = function () {
    // console.log(arguments); // 输出全部参数，这个对象并不是数组
    // 转换成数组
    const arrArgs = Array.prototype.slice.call(arguments);
    // 命名分组被放在最后一项中，pop()方法会从原数组中删除最后一项并返回
    const data = arrArgs.pop();
    // 调试输出
    console.log(arrArgs, data);
    // 字符转数字
    post_id = parseInt(post_id);
    data.app_id = parseInt(data.app_id);
    // 取余+3，3<=hash<=9
    const hash = ((post_id + data.app_id) % 7) + 3;
    console.log(hash, post_id + data.app_id);
    return `<a href="${data.url}#${hash}-${post_id}" ${data.attrs}>${data.url}#${hash}-${post_id}</a>`;
  };
  return html.replace(
    /<a href="[^"]+" (?<attrs>[^>]+)>(?<url>https:\/\/app.zblogcn.com\/\?id=(?<app_id>\d+))[^<]*<\/a>/,
    fnRegxCB
  );
  // 不需要回调处理的话是这样↓
  // return html.replace(
  //   /<a href="[^"]+" (?<attrs>[^>]+)>(?<url>https:\/\/app.zblogcn.com\/\?id=(?<id>\d+))[^<]*<\/a>/,
  //   `<a href="$<url>#${post_id}" $<attrs>>$<url>#${post_id}</a>`
  // );
}
```

「- -」「- -」「- -」「- -」

obj 转网址参数：

```js
// obj转网址参数
const queryString = Object.keys(data)
  .map((key) => key + "=" + data[key])
  .join("&");
```

「- -」「- -」「- -」「- -」

obj 键值遍历：

```js
// obj键值遍历
Object.keys(req.headers).forEach(function (key) {
  console.log(key, req.headers[key]);
});
```

「- -」「- -」「- -」「- -」

解除图片防盗链：

```js
// 解除图片防盗链
(() => {
  function $na(e) {
    return document.querySelectorAll(e);
  }
  $na("a img").forEach((el) => {
    el.setAttribute("referrerPolicy", "no-referrer");
    console.log(el.getAttribute("src"));
  });
})();
```

「- -」「- -」「- -」「- -」

并不常用，只是备忘：

```js
(()=>{
 for (let index = 0; index <= 13; index++) {
   console.log(index,index % 7,Math.abs(index % 7 - 3));
 }
})();
```

<!--3107-->
