---
title: 「Node.js」一个 export/import 问题
date: 2022-10-30 22:16:20
tags:
 - Node.js
 - JavaScript
 - 折腾
categories:
 - 电脑网络
id: 43
alias: 20100204145
---

### 前言

折腾，遇到问题，解决，水一篇，周而复始……

然而昨天久违的看了下百度统计，日 IP 已经掉到 20 了……

<!--more-->

话说之前也遇到个类似的问题：

> [「大坑」关于 module 模式下如何正确引入 WebSocketServer\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220301064.html "「大坑」关于 module 模式下如何正确引入 WebSocketServer\_电脑网络\_沉冰浮水")

### 正文

> 以下为去 v2ex 提问时的原始内容；

项目本身使用 rollup 构建，然后功能上是一个 rollup-plugin，一开始只导出了一个函数 monkey，后边加了功能，结果就是拿到的东西不统一了。

虽然可以先判断一下，然而还是想弄清为什么会有这种差异……

```js
export { main as default, monkeyPath, monkeyRequire };
```

```js
// for test
import monkey, { monkeyPath, monkeyRequire } from "../../dist/index.mjs";

console.log("typeof monkey：", typeof monkey);
// typeof monkey： function
```

```js
// for prod
import monkey, { monkeyPath, monkeyRequire } from "rollup-plugin-monkey";

console.log("typeof monkey：", typeof monkey);
// typeof monkey： object
console.log("typeof monkey.default：", typeof monkey.default);
// typeof monkey.default： function
```

项目源码：
https://github.com/wdssmq/rollup-plugin-monkey

这里可以看到 dist/ 内容：
https://www.npmjs.com/package/rollup-plugin-monkey?activeTab=explore

最终项目使用的配置文件：
https://github.com/wdssmq/rollup-plugin-monkey/blob/main/test/gm/rollup.config.mjs

> v 友指出实际引用应该是 cjs，`exports["default"] = main`，会得到一个`object`类型的导出；

删除 prod 内对应的 cjs 后变成找不到文件了，是有 mjs 的，然后 pkg 内有如下配置：

```json
  "main": "dist/index.cjs",
  "module": "dist/index.mjs",
  "type": "module",
```

看来我理解有误，以为使用 module 语法就会使用对应字段的路径？

好像应该按下边的写，虽然并没有测试过 require：

```json
  "main": "dist/index.mjs",
  "exports": {
    "import": "./dist/index.mjs",
    "require": "./dist/index.cjs"
  },
  "type": "module",
```

### 补充

只导出 default 时的代码：

```js
// msj
export { main as default };

// cjs
exports["default"] = main;
```

有额外导出时的代码：

```js
// msj
export { main as default, monkeyPath, monkeyRequire };

// cjs
exports["default"] = main;
exports.monkeyPath = monkeyPath;
exports.monkeyRequire = monkeyRequire;
```

