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

ESLint - Pluggable JavaScript linter - ESLint 中文：

[http://eslint.cn/](http://eslint.cn/ "ESLint - Pluggable JavaScript linter - ESLint 中文")

**虽然不太清楚，使用 VSCode 插件版仍然需要在项目下或全局安装`eslint`的样子？**

### 安装 ESLint

```bash
# 安装 cnpm
npm install -g cnpm --registry=https://registry.npmmirror.com
```

使用 `cnpm 沉冰浮水` 仍然搜索不到匹配，/哭；

**全局安装：**

```bash
# 全局安装
cnpm install -g eslint
# 查看版本号
cnpm ls eslint
# 不知道为什么输出为空，加 -g 参数则直接卡住
# 也没找到正确能用的方法

# 下边命令可以得到全局 node_modules 的地址
cnpm root -g
```

**当前项目内：**

```bash
# 当前项目内
cnpm install eslint --save-dev
# 查看版本号
cnpm ls eslint
```

### 初始化

```bash
cnpm init @eslint/config
# eslint --init
# 所在目录如果没有 package.json 可能会报错，`npm init` 创建；

# 选项一 - 如何使用 ESLint
? How would you like to use ESLint? …
  To check syntax only
▸ To check syntax and find problems
  To check syntax, find problems, and enforce code style
# 注：如果选择了第 3 项，后续选项会不一样


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

# 选项六 - ESLint Config 文件保存为何种格式
? What format do you want your config file to be in? …
▸ JavaScript
  YAML
  JSON

# 选项七 - 根据选择可能需要安装额外的项目，比如 vue
The config that you ve selected requires the following dependencies:

eslint-plugin-vue@latest

# 选项七 - 是否直接安装上边列出的项目
? Would you like to install them now? ‣ No / Yes

# 选项八 - 如果上一步选择了安装，会询问使用的包管理器
? Which package manager do you want to use? …
  npm
  yarn
▸ pnpm

# ------------

# 如果上边「选项一」选择了「To check syntax, find problems, and enforce code style」，会多出以下选项
? How would you like to define a style for your project? …
  Use a popular style guide
▸ Answer questions about your style

# 分支二 - 询问具体的代码风格，包括缩进、引号、分号等
✔ How would you like to define a style for your project? · prompt
✔ What style of indentation do you use? · 4
✔ What quotes do you use for strings? · double
✔ What line endings do you use? · unix
✔ Do you require semicolons? · No / Yes

# 分支一 - 选择 google 等厂商的代码风格
✔ How would you like to define a style for your project? · guide
✔ Which style guide do you want to follow? · google
```

选项一：

- 仅检查语法；
- 检查语法并查找问题；
- 在前者基础上强制代码样式；

默认为第 2 项，实际建议第 3 项；

之后根据实际需要用；

额外注意：

- 配置文件建议使用 JS 格式，因为 JSON 不支持注释；
- 本文是以 cnpm 为基础，包管理器选项里没有，可以换 pnpm；
- 或者不选择自动安装，手动执行`cnpm install`；


### 使用（CLI）

```bash
# 检查指定文件
eslint vite.config.js
# 检查目录
eslint src/**/*.vue src/**/*.js
# 指定后缀 + 自动修复
eslint . --ext .js,.mjs --fix
# 排除指定文件中定义的路径
eslint . --ext .js,.mjs --fix --ignore-path .gitignore
```

Command Line Interface - ESLint 中文：

[http://eslint.cn/docs/user-guide/command-line-interface](http://eslint.cn/docs/user-guide/command-line-interface "Command Line Interface - ESLint 中文")

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

所以保险起见还是自己执行`cnpm init @eslint/config`吧；

插件有不少配置项，可以在「设置」中搜索`eslint`查看：

```json
{
  "eslint.validate": [
    "typescript",
    "javascript",
    "javascriptreact",
    "vue"
  ],
  // 这里甚至并不能用「cnpm」 - -!
  "eslint.packageManager": "pnpm"
}
```

### 检查规则

使用 `@eslint/config` 初始化，然后再修改具体细节，下边为一份参考：

```js
/* // global module // 好像新版不需要设置这个了？ */
module.exports = {
    'env': {
        'browser': true,
        'es2021': true,
    },
    'extends': 'eslint:recommended',
    'parserOptions': {
        'ecmaVersion': 'latest',
    },
    // 全局变量声明
    'globals': {
        'module': 'readonly',
        'require': 'readonly',
    },
    // 规则定义
    'rules': {
        /* 相对通用的规则 */
        'indent': [
            'error',
            4,
        ],
        'linebreak-style': [
            'error',
            'unix',
        ],
        'quotes': [
            'error',
            'single',
        ],
        'semi': [
            'error',
            'never',
        ],
        'spaced-comment': [
            'error',
            'always',
        ],

        /* 以下按需配置 */

        // 允许 require 语法赋值
        '@typescript-eslint/no-var-requires': 0,

        // generator 函数中 * 号前后的空格
        'generator-star-spacing': 0,

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
            { 'requireForBlockBody': true },
        ],

        // 变量声明后未使用
        // args: "none" 表示不检查函数参数是否被使用
        'no-unused-vars': [
            1,
            { 'args': 'none' },
        ],

        // 函数圆括号之前的空格
        // anonymous: "never" 表示匿名函数不允许空格
        // named: "never" 表示命名函数不允许空格
        'space-before-function-paren': [
            1,
            { 'anonymous': 'never', 'named': 'never' },
        ],

        // 禁止不规则的空白
        'no-irregular-whitespace': [
            2,
            { 'skipStrings': true, 'skipRegExps': true },
        ],

        // // 正式环境禁止 debugger
        // 'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    },
}

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
