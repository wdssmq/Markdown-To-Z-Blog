---
title: 「GM_脚本」GM_setClipboard 方法示例
tags:
- GM_脚本
- JavaScript
- 浏览器脚本
categories:
- 电脑网络
id: 619
alias: 20211108343
---

浏览器脚本的初衷是可以针对那些非自己管理的站点实现所需的额外功能，然后即使是自己的网站，有些仅限自己使用的功能同样用脚本可能比较好；

<!--more-->

`GM_setClipboard`函数用于向剪贴板写入文本内容，也就是实现「复制」效果；

GM\_setClipboard - 国内版 Bing：

[https://cn.bing.com/search?q=GM_setClipboard](https://cn.bing.com/search?q=GM_setClipboard "GM\_setClipboard - 国内版 Bing")

`GM_`开头的函数需要使用`@grant`标记声明才可以使用：

```js
// @grant    GM_setClipboard
```

下边一份完整的功能代码：

```js
// ==UserScript==
// @name         「Z-Blog」- 复制已输入的 Tags
// @namespace    https://www.wdssmq.com/
// @description  在 Z-BlogPHP 的「文章编辑」页面，添加一个按钮，可以将已输入的 Tags 复制到剪贴板。
// @version      0.1
// @author       沉冰浮水
// ----------------------------
// @link   https://afdian.net/@wdssmq
// @link   https://github.com/wdssmq/userscript
// @link   https://greasyfork.org/zh-CN/users/6865-wdssmq
// ----------------------------
// @include      http://zbp.wdssmq.tk/zb_system/admin/edit.php?act=ArticleEdt
// @grant        GM_setClipboard
// ==/UserScript==
/* jshint esversion:6 */

(function () {
  "use strict";
  // 上边 @grant 属性如果不为 none 时，好像不能使用 window 而要用 unsafeWindow
  let $ = typeof window.$ == "function" ? window.$ : unsafeWindow.jQuery;
  // 添加按钮
  $("#showtags").after(
    '<a class="js-copy-tags" href="javascript:;" title="一键复制"> [复制Tags]</a>'
  );
  // 绑定事件
  $(".js-copy-tags").click(function () {
    const strTags = $("#edtTag").val();
    GM_setClipboard(strTags);
  });
})();

```

> “佛系安利”第二弹：用「油猴子脚本」武装你的浏览器\_电脑网络\_沉冰浮水：
>
> [https://www.wdssmq.com/post/20180606584.html](https://www.wdssmq.com/post/20180606584.html "“佛系安利”第二弹：用「油猴子脚本」武装你的浏览器\_电脑网络\_沉冰浮水")
