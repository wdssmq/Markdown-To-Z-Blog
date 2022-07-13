---
title: 【坑货笔记】零宽空白 &#8203; 是什么鬼！
date: 2022-04-02 11:14:47
tags:
- Unicode
- HTML
- 笔记
categories:
- 电脑网络
id: 2923
alias: 20190818266
---

这大概是在本站后台正式使用 MarkDown 编辑器写的第一篇文章。。

<!--more-->

2022-04-02：然后再次修改时已经换了写作方式：[https://github.com/wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。#md2zb")

其实上一篇 [【教程】Z-Blog 插件运作机制简述](https://www.wdssmq.com/post/20190817262.html "【教程】Z-Blog 插件运作机制简述") 也是用的 MD 编辑器但是是在桌面版的 Typora 中写好复制过来发布的；

------------

而本次遇到的问题是在写就前文本时插入了代码，直接 Typora 渲染结果中复制到 php 文件中运行是没有问题的，但是使用 Typora 的导出功能导出为 HTML，再从 HTML 复制时就会报以下错误：

> Parse error: syntax error, unexpected '$articles' (T_VARIABLE) in *.php on line 15

探究之下发现，在导出结果中，代码部分的空行会包含一个`&#8203;`字符，直接 Google 搜索框里都会变成空白→_→，需要把搜索词改成 8203；

相关说明整理如下：

> 零宽空格（zero-width space, ZWSP）是一种不可打印的 Unicode 字符，用于可能需要换行处 —— 维基百科
>
> Unicode 编码：`U+200B`
>
> HTML 实体编码：`&#8203;` ← 事实上这里如果不用代码语法写的话渲染成 HTML 就会看不见；
>
> URL 编码（UrlEncode）：`%E2%80%8B` ← 当零宽空白出现在网址中时；
>

而在文本编辑器中，即使设置了显示全部字符也不会有东西出现，但是把编码转换成 ANSI 就会出现一个?，算是实际排查时的一个有效方案；

<!--2923-->
