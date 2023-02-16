---
title: 「备忘」那些需要全局安装的 node 包
date: 2023-01-02 12:06:26
tags:
 - Node.js
 - 备份
 - 折腾
categories:
 - 列表纪事
id: 646
alias: 20230103270
---

「备忘」那些需要全局安装的 node 包

<!--more-->

### 安装 cnpm

```bash
npm install -g cnpm --registry=https://registry.npmmirror.com
# 习惯了 cnpm
```

### 具体项目

```bash
cnpm i -g @lint-md/core @lint-md/cli
# lint-md/lint-md: 检查中文 markdown 编写格式规范的命令行工具，基于 AST，方便集成 CI，写博客 / 文档必备。支持 API 调用！
# https://github.com/lint-md/lint-md

cnpm i -g browser-sync
# Browsersync - Time-saving synchronised browser testing
# https://browsersync.io/

cnpm i -g eslint
# 「折腾」ESLint 安装与使用_电脑网络_沉冰浮水
# https://www.wdssmq.com/post/20190917021.html
```
