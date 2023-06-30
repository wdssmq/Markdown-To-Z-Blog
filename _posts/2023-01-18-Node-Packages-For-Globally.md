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

### 安装 cnpm / pnpm

```bash
# cnpm
npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm get registry

# pnpm
# npm install -g pnpm
curl -fsSL https://get.pnpm.io/install.sh | sh -
# 设置淘宝源
pnpm config set registry https://registry.npmmirror.com
pnpm get registry

```

### 具体项目

```bash
# lint-md
pnpm install -g @lint-md/core @lint-md/cli

# browser-sync
pnpm install -g browser-sync

# eslint
pnpm install -g eslint

# typescript && ts-node
pnpm install -g typescript ts-node

# rollup
pnpm install -g rollup

# hexo
pnpm install -g hexo-cli

# docsify
pnpm install -g docsify-cli

```

### 参考

「折腾」ESLint 安装与使用\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20190917021.html](https://www.wdssmq.com/post/20190917021.html "「折腾」ESLint 安装与使用\_电脑网络\_沉冰浮水")

lint-md/lint-md: :books: 检查中文 markdown 编写格式规范的命令行工具，基于 AST，方便集成 CI，写博客 / 文档必备。支持 API 调用！：

[https://github.com/lint-md/lint-md](https://github.com/lint-md/lint-md "lint-md/lint-md: :books: 检查中文 markdown 编写格式规范的命令行工具，基于 AST，方便集成 CI，写博客 / 文档必备。支持 API 调用！")
