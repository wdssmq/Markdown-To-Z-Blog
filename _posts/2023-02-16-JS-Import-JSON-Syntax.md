---
title: 「Node.js」import 引入 JSON 文件的问题 - rollup && eslint
date: 2023-02-09 17:53:01
tags:
 - Node.js
 - JavaScript
 - rollup
 - eslint
categories:
 - 电脑网络
id: 2010
alias: 20140110775
---

rollup 2.x 版本是可以直接这么写的：

<!--more-->

```js
// rollup.config.js
import pkg from "./package.json";
```

升级 3.15 后报错；

> [!] TypeError: Module "./package.json" needs an import assertion of type "json"

修改后 eslint 又会报错：

```js
// rollup.config.js
import pkg from "./package.json" assert { type: "json" };
// Parsing error: Unexpected token assert ← eslint
```

进一步解决：

```bash
cnpm i -D eslint @babel/core @babel/eslint-parser @babel/plugin-syntax-import-assertions
```

```js
// .eslintrc.js
"parser": "@babel/eslint-parser",
"parserOptions": {
    "requireConfigFile": false,
    "babelOptions": {
        "plugins": [
            '@babel/plugin-syntax-import-assertions'
        ],
    },
    "ecmaVersion": "latest",
    "sourceType": "module",
},
```

就挺麻烦的 - -

· · · · · ·

「折腾」ESLint 安装与使用\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20190917021.html](https://www.wdssmq.com/post/20190917021.html "「折腾」ESLint 安装与使用\_电脑网络\_沉冰浮水")

Support of `assert {type: "json"}` · Discussion #15305 · eslint/eslint：

[https://github.com/eslint/eslint/discussions/15305#discussioncomment-2508948](https://github.com/eslint/eslint/discussions/15305#discussioncomment-2508948 "Discussion #15305 · eslint/eslint")
