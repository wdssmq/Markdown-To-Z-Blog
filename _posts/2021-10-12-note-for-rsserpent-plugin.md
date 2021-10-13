---
title: 「折腾」RSSerpent 插件笔记
tags:
- 折腾
- RSS
- Python
categories:
- 电脑网络
id: 14
alias: 20120817543
---

环境配置什么的果然是最麻烦的。。这篇笔记的主要作用还是把各种命令贴在一起供我自己复制使用；

<!--more-->

创建插件 - RSSerpent Docs：

[https://docs.rsserpent.com/latest/zh/contribution/plugin/](https://docs.rsserpent.com/latest/zh/contribution/plugin/ "创建插件 - RSSerpent Docs")


```bash
# 使用模板创建一个新插件
cookiecutter gh:rsserpent/template

# rsserpent-plugin-manhuagui
# 前缀部分需要手动输入

# 进入目录
cd rsserpent-plugin-manhuagui
# 进入 poetry 虚拟环境
poetry shell
# 运行
uvicorn rsserpent:app --host '0.0.0.0' --port 1202 --reload
```

提交前的规范化检查

```bash
# 进入 poetry 虚拟环境
poetry shell
# 需要首暂存修改
git add .
# 执行检查
pre-commit run --all-files
```
