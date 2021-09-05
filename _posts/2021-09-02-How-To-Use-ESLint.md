---
title: 「折腾」ESLint 安装与使用
tags:
- JavaScript
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

**虽然不太清楚，使用 VSCode 插件版仍然需要在项目下或全局安装 Npm 包的样子？**

### 安装 ESLint

```bash
# 淘宝镜像
npm install -g cnpm --registry=https://registry.npm.taobao.org
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

# 下边命令可以得到全局node_modules的地址
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
eslint --init

# 选项一
# ? How would you like to use ESLint? ...
#   To check syntax only
# > To check syntax and find problems
#   To check syntax, find problems, and enforce code style

# 选项二
# ? What type of modules does your project use? ...
# > JavaScript modules (import/export)
#   CommonJS (require/exports)
#   None of these

# 选项三
# ? Which framework does your project use? ...
# > React
#   Vue.js
#   None of these

# 选项四
# ? Does your project use TypeScript? » No / Yes

# 选项五
# ? Where does your code run? ...  (Press <space> to select, <a> to toggle all, <i> to invert selection)
# √ Browser
# √ Node

# 选项六
# ? What format do you want your config file to be in? ...
#   JavaScript
#   YAML
# > JSON

# 选项七 因为选择了 vue
# The config that you've selected requires the following dependencies:

# eslint-plugin-vue@latest
# ? Would you like to install them now with npm? » No / Yes
```

选项一：
- 仅检查语法；
- 检查语法并查找问题；
- 在前者基础上强制代码样式；

建议选择：检查语法并查找问题；「默认选项」

选项二至选项六请按实际需要；

选项七根据实际选择会不一样，另外默认的`npm instll XXX`可能会比较慢，可以选择 No 然后自己换用`cnpm`；

### 使用（CLI）

```bash
# 检查指定文件
eslint vite.config.js
# 检查目录
eslint src/**/*.vue src/**/*.js
```

Command Line Interface - ESLint 中文：

[http://eslint.cn/docs/user-guide/command-line-interface](http://eslint.cn/docs/user-guide/command-line-interface "Command Line Interface - ESLint 中文")

### VSCode 插件版

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

所以保险起见还是自己执行`eslint --init`吧；

### 检查规则

下边是目前决定使用的规则，以后会慢慢补充；

```json
  "rules": {
    "spaced-comment": [2, "always"],
    "semi": [2, "always"],
    "quotes": [2, "double"],
    "no-unused-vars": [1, { "args": "none" }]
  }
```

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
