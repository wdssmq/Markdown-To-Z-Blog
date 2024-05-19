---
title: 「折腾」ESLint 安装与使用
date: 2021-09-02 13:37:25
tags:
- JavaScript
- eslint
- VSCode
- 折腾
categories:
- 电脑网络
id: 581
alias: 20190917021
---

### 写在前边

因为嫌麻烦，并没有实际用到过 ESLint；

最近改了一个别人写的东西，别的不说，单行注释双斜线后不加空格实在是逼死强迫症。

<!--more-->

### 资源网址

ESLint - Visual Studio Marketplace：

[https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint "ESLint - Visual Studio Marketplace")

Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter：

[https://eslint.org/](https://eslint.org/ "Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter")

**虽然不太清楚，使用 VSCode 插件版仍然需要在项目下或全局安装`eslint`的样子？**

### 安装 ESLint

```bash
# 安装 pnpm 并设置淘宝镜像
npm install -g pnpm
pnpm config set registry https://registry.npm.taobao.org

```

**全局安装：**

```bash
# 全局安装
pnpm install eslint -g
# 查看全局安装的版本号
pnpm ls eslint -g

```

**当前项目内：**

```bash
# 当前项目内
pnpm install eslint --save-dev
# 查看版本号
pnpm ls eslint

```

### 初始化

```bash
pnpm create @eslint/config
# eslint --init
# 所在目录如果没有 package.json 可能会报错，`npm init` 创建；

# 注：后续选项以实际为准

# 选项一 - 如何使用 ESLint
? How would you like to use ESLint? …
  To check syntax only
▸ To check syntax and find problems

# 选项二 - 模块引入方式
? What type of modules does your project use? …
▸ JavaScript modules (import/export)
  CommonJS (require/exports)
  None of these

# 选项三 - 项目使用的框架
? Which framework does your project use? …
  React
▸ Vue.js
  None of these

# 选项四 - 是否使用 TypeScript
? Does your project use TypeScript? ‣ No / Yes

# 选项五 - 项目使用的环境，可以都选或都不选
? Where does your code run? …  (Press <space> to select, <a> to toggle all, <i> to invert selection)
✔ Browser
✔ Node

# 选项六 - 根据选择可能需要安装额外的项目，比如 vue 的插件
The config that you ve selected requires the following dependencies:

eslint-plugin-vue@latest

# 选项七 - 是否直接安装上边列出的项目
? Would you like to install them now? ‣ No / Yes

# 选项八 - 如果上一步选择了安装，会询问使用的包管理器
? Which package manager do you want to use? …
  npm
  yarn
▸ pnpm

```

### 使用（CLI）

```bash
# 检查指定文件
eslint vite.config.js

# 可以使用 --fix 修复能够自动修复的问题

# 按路径匹配文件，某一对引号内的规则没能匹配到文件时会报错
eslint "src/**/*.vue" "src/**/*.{js,mjs,ts}" --fix

```

新版命令行废弃了很多参数，甚至官方文档也还没完全更新……

Command Line Interface Reference - ESLint - Pluggable JavaScript Linter：

[https://eslint.org/docs/latest/use/command-line-interface#site_top](https://eslint.org/docs/latest/use/command-line-interface#site_top "Command Line Interface Reference - ESLint - Pluggable JavaScript Linter")

### VSCode 插件版

**注：插件版本好像依赖于全局安装的`eslint`包？**

在「命令面板（Ctrl + Shift + P）」中输入`eslint`即可查看所拥有的命令：

- `ESLint: Create ESLint configuration` 创建配置文件；
- `ESLint: Fix all auto-fixable Problems` 修复能够自动修复的问题；
- `ESLint: Migrate Settings` 迁移设置，啥用暂不清楚；
- `ESLint: Show Output Channel` 查看日志输出，从信息看确实依赖于`node_modules\eslint\lib\api.js`；
- `ESLint: Restart ESLint Server` 重启插件服务；

因为 VSCode 默认终端是 Git Bash，所以自动触发创建命令时出现了下边错误：

```bash
node_modules\.bin\eslint.cmd --init
# bash: node_modules.bineslint.cmd: command not found

```

所以保险起见还是自己执行`pnpm create @eslint/config`吧；

插件有不少配置项，可以在「设置」中搜索`eslint`查看：

```json
{
  "eslint.validate": [
    "typescript",
    "javascript",
    "javascriptreact",
    "vue"
  ],
  "eslint.packageManager": "pnpm"
}

```

### 检查规则

使用 `@eslint/config` 初始化，然后再修改具体细节，下边为一份参考：

```js
// 此处为新版的 eslint.config.mjs
import globals from "globals";
import pluginJs from "@eslint/js";

export default [
  {
    languageOptions:
    {
      globals: {
        ...globals.browser,
        "$": "readonly",
        "module": "readonly",
        "jQuery": "readonly",
      },
    },
  },
  pluginJs.configs.recommended,
  {
    // 规则定义，按实际需要修改
    'rules': {
        // 缩进
        'indent': [
            'error',
            4,
            {
                'SwitchCase': 1,
            },
        ],
        // 换行符
        'linebreak-style': [
            'error',
            'unix',
        ],
        // 引号
        'quotes': [
            'error',
            'single',
        ],
        // 分号
        'semi': [
            'error',
            'never',
        ],
        // 单行注释的空格
        'spaced-comment': [
            'error',
            'always',
            {
                'line': {
                    // 继下述字符后再加空格
                    'markers': ['!', '#', '/'],
                },
            }
        ],

        /* ---------------- */

        // 对象或数组的拖尾逗号
        // always-multiline 表示只有在多行时才需要拖尾逗号
        'comma-dangle': [
            1,
            'always-multiline',
        ],

        // 箭头函数参数括号
        // as-needed 表示只有在需要时才添加括号
        'arrow-parens': [
            1,
            'as-needed',
            {
                // requireForBlockBody 表示在块体中需要括号
                'requireForBlockBody': true
            },
        ],

        // 变量声明后未使用
        // args: "none" 表示不检查函数参数是否被使用
        'no-unused-vars': [
            1,
            {
                'args': 'none'
            },
        ],

        // 函数圆括号之前的空格
        // 分别对匿名函数、异步箭头函数、命名函数设置
        'space-before-function-paren': [
            1,
            {
                'anonymous': 'never',
                'asyncArrow': 'always',
                'named': 'never'
            },
        ],

        // 禁止不规则的空白
        'no-irregular-whitespace': [
            2,
            {
                'skipStrings': true,
                'skipRegExps': true
            },
        ],

        // // 允许 require 语法赋值
        // '@typescript-eslint/no-var-requires': 0,

        // // generator 函数中 * 号前后的空格
        // 'generator-star-spacing': 0,

        // // 正式环境禁止 debugger
        // 'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    },
  },
];

```

List of available rules - ESLint 中文：

[http://eslint.cn/docs/rules/](http://eslint.cn/docs/rules/ "List of available rules - ESLint 中文")

### 错误排查

1、

> Environment key "es2021" is unknown

项目中已经安装 ESLint 但是版本太低，请删除「package-lock.json」文件后重新执行`cnpm install eslint --save-dev`或`cnpm install eslint@latest --save-dev`;

仍然有问题请删除 node_modules 后再试；

可在「本站（`www.wdssmq.com`）」搜索关键词：`快速删除 node_modules` 或 `快速删除` ；

2、

> Parsing error: Invalid ecmaVersion.

默认生成的配置文件中有一项是`"ecmaVersion": 12,`，改成 11 或 10，虽然并不清楚有啥用；

3、

> Do not access Object.prototype method 'hasOwnProperty' from target object.eslintno-prototype-builtins

出于安全并不建议直接用：`foo.hasOwnProperty("bar")`，而应该写成 `Object.prototype.hasOwnProperty.call(foo, "bar")`；

正则替换：

`([a-z0-9]+)\.hasOwnProperty\(([^\)]+)\)`

`Object.prototype.hasOwnProperty.call($1, $2)`

然后 VSCode 中 `forin` 的代码片段如下，看了已经修改过了：

```js
for (const key in object) {
  if (Object.hasOwnProperty.call(object, key)) {
    const element = object[key];

  }
}
```

4、

> The "marketId" property should be a constructor.eslintvue/require-prop-type-constructor

vue 中定义`props`对像时，多个类型声明应写为数组；

```js
export default {
    props: {
        myProp1: Number | String, // 错误
        myProp2: [Number, String] // 正确
    }
}
```

5、

> '__dirname' is not defined.eslintno-undef

错误提示出现在「vite.config.js」中；

解决：

.eslintrc.json 或其他格式的配置文件中，确保对应声明中存在`"node": true,`这一项；

```json
{
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  }
}
```

6、

> The template root requires exactly one element.eslintvue/no-multiple-template-root

报错代码如下，将`<template> ** </template>`改为`<template><div> ** </div></template>`可以消除这个错误，但是不太科学；

```html
<template>
  <Header class="header" />
  <router-view class="content" />
  <Footer class="footer" />
</template>
```

正确方法，修改「.eslintrc.json」文件

`"extends": ["eslint:recommended", "plugin:vue/essential"],`→`"extends": ["eslint:recommended", "plugin:vue/vue3-essential"],`；

<!-- 2023-07-01 14:44:19 -->
