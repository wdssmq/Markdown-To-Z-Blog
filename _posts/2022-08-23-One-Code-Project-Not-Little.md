---
title: 「言说」写了份有点「大」的代码
date: 2022-08-23 12:10:33
tags:
 - 言说
 - 说点什么
 - 杂七杂八
categories:
 - 杂七杂八
id: 34
alias: 20190704011
---

发现自己一直都不怎么喜欢写很复杂的功能，作品大都是「小代码」，原始意义上的那个小；

<!--more-->

比如前不久折腾的这个东西：[「小代码」跨文件按行统计文本「Python」\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20120901104.html "「小代码」跨文件按行统计文本「Python」\_电脑网络\_沉冰浮水")

然后最近 feedly 叒改版了，虽然目测只是根元素 `#box` 换成了 `#root`，导致对应的「GM_脚本」也要修改；

之前有用 rollup.js 弄了一套开发「GM_脚本」的体系，实现了多个 js 文件构建拼接成一份最终代码，只是需要另外弄个 web 服务用来安装到浏览器扩展，修改编译后要再安装一次来更新，然后手动刷新浏览器页面……

[「折腾」使用 rollup.js 模块化编写 GM 脚本\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20120627834.html "「折腾」使用 rollup.js 模块化编写 GM 脚本\_电脑网络\_沉冰浮水")

自带 web 服务并且支持热更新的轮子其实是有的。比如 vite-plugin-monkey，也有实际上应用到某些项目中，然而已经习惯了以纯文本方式引入 `Userscript Header`；

然后我自己也不需要在「GM_脚本」中引入大段的 CSS 或者 Vue 什么的；

```js
// 所见既所得.jpg
const gm_banner = `
// ==UserScript==
// @name         New Userscript
// @namespace    https://www.wdssmq.com/
// @version      0.1
// @author       沉冰浮水
// @description  try to take over the world!
// @license      MIT
// @noframes
// @run-at       document-end
// @match        <$URL$>
// @grant        none
// ==/UserScript==

/* jshint esversion: 6 */
/* eslint-disable */
`;

const gm_name = "empty_def";

export { gm_banner, gm_name };
```

一开始有找到 `rollup-plugin-dev` `rollup-plugin-livereload` 这两个插件，然而两者都有跨域问题（CORS）；「- CSP 和 CORS 目测是两个东西，可以自行了解 -」

前者可以修改后允许跨域，后者则因为又依赖于上游包，就挺麻烦的；

--------------

总之各种纠结之后自己缝合了一个轮子出来 ——

wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」：

[https://github.com/wdssmq/rollup-plugin-monkey](https://github.com/wdssmq/rollup-plugin-monkey "wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」")

- **目前代码在 v1 分支；**
- README 好麻烦，pnpm 安装也有些问题要解决 Orz；
- 要不要发布到 npm 啊，git 安装也不是不能用；
- 所以我为了讲这一部分的内容水了一篇文章；

--------------

> Disable Content-Security-Policy：
>
> `https://microsoftedge.microsoft.com/addons/detail/disable-contentsecurity/ecmfamimnofkleckfamjbphegacljmbp`
