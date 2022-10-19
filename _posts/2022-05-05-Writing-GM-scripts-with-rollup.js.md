---
title: 「折腾」使用 rollup.js 模块化编写 GM 脚本
date: 2022-05-05 14:06:07
tags:
- JavaScript
- GM_脚本
- 折腾
categories:
- 电脑网络
id: 1309
alias: 20120627834
---

五月份了，又可以领大会员 B 币了，不过 B 站又改了些东西，导致我之前写的提醒脚本也要相应的修改；

「- 很多说明要详细到什么程度也是好难把握 -」

<!--more-->

> 脚本获取及说明见：
>
> [「GM 脚本」大会员 B 币领取提醒\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20141219446.html "「GM 脚本」大会员 B 币领取提醒\_电脑网络\_沉冰浮水")

-----------

2022-09-12：

> **弄了个 rollup 插件出来：**
>
> wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」：
>
> [https://github.com/wdssmq/rollup-plugin-monkey](https://github.com/wdssmq/rollup-plugin-monkey "wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」")
>
> **视频演示：**
>
>「小代码」rollup.js 开发「GM\_脚本」演示\_哔哩哔哩\_bilibili：
>
> [https://www.bilibili.com/video/BV1qe4y1d7ZM](https://www.bilibili.com/video/BV1qe4y1d7ZM "「小代码」rollup.js 开发「GM\_脚本」演示\_哔哩哔哩\_bilibili")

-----------

一直以来，针对同一个网站的功能脚本会塞进一个文件里，比如之前 B 站的脚本有 330 行，维护修改是真的痛苦；

「果然还是拆成小文件然后自动拼接会比较方便吧！」 ← 虽然这么想，但是咸鱼星人什么的。。

好在前不久终于开始填这个坑了，使用的方案就是「`rollup.js`」；

`rollup.js`本身的教程可参考文末推荐，事实上终于决定水出本文也是因为阮一峰碰巧在这个时机写了介绍；

-----

如果你也想用来构建「GM_脚本」则可以参考下我的使用姿势；

- GM_脚本的应用环境是浏览器，所以对应的输出格式是`format: 'iife'`；
- GM_脚本开头需要加入`==UserScript== …… ==/UserScript==`注释，可以作为`banner`由`rollup.js`拼接进来；
- 配置定义文件`rollup.config.js`支持从外部引入内容作为参数，所以`banner`定义值可以写在一个单独的文件里，比如`src/__info.js`，同样作为脚本命名的`name`也可以由该文件提供；
- 所以不同脚本项目可以使用同样的`rollup.config.js`内容，而只需要修改`src/__info.js`中的定义；
- 我弄了份`empty\_def`作为初始项目，除了`src/__info.js`外还有`src/_base.js`，封装了各种「初始常量或函数」；「- 就是风格不太统一的感觉 -」
- `src/main.js`中可以使用`import _bcoin from './_bcoin';`单纯拼接不同文件进来，虽然会得到一行黄字：`Import of non-existent exports`，不过我们就是要这样用；

userscript/empty\_def：[https://github.com/wdssmq/userscript/tree/master/empty_def](https://github.com/wdssmq/userscript/tree/master/empty_def "userscript/empty\_def at master · wdssmq/userscript")

userscript/bilibili：[https://github.com/wdssmq/userscript/tree/master/bilibili](https://github.com/wdssmq/userscript/tree/master/bilibili "userscript/bilibili at master · wdssmq/userscript")「历史原因，导出文件还是`later.user.js`，要不要改呢」

最新 B 币领取提醒：[https://github.com/wdssmq/userscript/blob/master/bilibili/src/_bcoin.js](https://github.com/wdssmq/userscript/blob/master/bilibili/src/_bcoin.js "userscript/\_bcoin.js at master · wdssmq/userscript")「只是提醒，并不能自动领」

-----

> 打包工具 rollup.js 入门教程 - 阮一峰的网络日志：
>
> [http://www.ruanyifeng.com/blog/2022/05/rollup.html](http://www.ruanyifeng.com/blog/2022/05/rollup.html "打包工具 rollup.js 入门教程 - 阮一峰的网络日志")

> Module 的语法 - ES6 教程 - 网道：
>
> [https://wangdoc.com/es6/module.html](https://wangdoc.com/es6/module.html "Module 的语法 - ES6 教程 - 网道")

