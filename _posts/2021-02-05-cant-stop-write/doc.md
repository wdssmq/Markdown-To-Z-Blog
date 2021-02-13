---
title: 【言说】停不下的写作和代码
tags:
- 言说
- 碎碎念
- 折腾
categories:
- 杂七杂八
id: 393
alias: 20210205073
---

### 再一次的安利

新的一天也在折腾新的写博工具，，

wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。：

[https://github.com/wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。")

所以文章分类的部分要怎么改进呢？？？

以及如何引用另一篇文章- -

<!--more-->

### 新功能

今天最主要的成果是为 m2z 工具配置了 VSCode 下的 tasks.json，功能是通过自动执行指定的`shell`命令，从而实现新建空白文章，快捷键`ctrl + shift + b`，更多说明见项目的 README 。

不太重要的附注：

- 该说因为 VSCode 是微软家的，所以换行要用`\r\n`，其实直接`\n`也能用，就是输出效果不太好看；
- 写完才发现，`${_date}-new-post`部分也可以作为一个整体变量的 - -；
- 忘记加判断是否已存在了- -，好像对使用不是很有影响；

```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "copy",
      "type": "shell",
      "command": [
        "\r\n",
        "cd _posts \r\n",
        "_date=`date +%Y-%m-%d` \r\n",
        "_empty=1970-01-01-empty.md \r\n",
        "cp ${_empty} ${_date}-new-post.md \r\n",
        "mkdir ${_date}-new-post \r\n",
        "cp ${_empty} ${_date}-new-post/doc.md"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

### 未能解决的部分

`.vscode/settings.json` 和 `*.code-workspace` 都可以用来实现一些选项的设置，包含在编辑器列表中隐藏部分路径文件，现在想在前者隐藏尽可能多的项目以方便「单纯使用」，然后在后者对其覆盖用来维护项目本身。

### 感慨

- 打算写点儿新东西；
- 发现工具还是不顺手；
- 改进工具；
- 把改进的过程记录下来写在文章里；
- 我原来想写啥来着？

### 契机

今天周五，所以新一期的周刊↓

科技爱好者周刊（第 145 期）：大家不出门，经济怎么办？ - 阮一峰的网络日志：

[http://www.ruanyifeng.com/blog/2021/02/weekly-issue-145.html](http://www.ruanyifeng.com/blog/2021/02/weekly-issue-145.html "科技爱好者周刊（第 145 期）：大家不出门，经济怎么办？ - 阮一峰的网络日志")

然后我的投稿没有入选，不知道下一期还有没有机会——

\[自荐\]使用 GitHub Actions + Markdown 更新 Z-Blog 博客。 · Issue #1634 · ruanyf/weekly：

[https://github.com/ruanyf/weekly/issues/1634](https://github.com/ruanyf/weekly/issues/1634 "\[自荐\]使用 GitHub Actions + Markdown 更新 Z-Blog 博客。 · Issue #1634 · ruanyf/weekly")

而这个项目其实是抄自 144 期的一个用于 WordPress 的项目。【【所以才不采用么？- -】】

### 一张封面图

然后在「往期回顾」中看到一张比较在意是什么东西的封面图就点进去看了，就是下边这期——

科技爱好者周刊：第 94 期 - 阮一峰的网络日志：

[http://www.ruanyifeng.com/blog/2020/02/weekly-issue-94.html](http://www.ruanyifeng.com/blog/2020/02/weekly-issue-94.html "科技爱好者周刊：第 94 期 - 阮一峰的网络日志")

关于封面图是啥可以自己去看，重要的是在这一期有下边的内容：

![001](https://i.loli.net/2021/02/05/gn1zQcLuZEeJ9Xw.png "001")

而我正好在昨天写了一篇：

[【言说】相对擅长写代码，然而也只有写代码](https://zbp17.wdssmq.com/post/8.html "【言说】相对擅长写代码，然而也只有写代码")

然而也没有然而。。。。

### 另一个项目

然后顺便投稿了略早之前的一个项目——

\[自荐\]一键复制网页标题及链接 · Issue #1636 · ruanyf/weekly：

[https://github.com/ruanyf/weekly/issues/1636](https://github.com/ruanyf/weekly/issues/1636 "\[自荐\]一键复制网页标题及链接 · Issue #1636 · ruanyf/weekly")

使用效果如下：

```conf
New Issue · ruanyf/weekly
https://github.com/ruanyf/weekly/issues/new
----
<p>New Issue · ruanyf/weekly</p><p><a href="https://github.com/ruanyf/weekly/issues/new" target="_blank" title="New Issue · ruanyf/weekly">https://github.com/ruanyf/weekly/issues/new</a></p>
----
[New Issue · ruanyf/weekly](https://github.com/ruanyf/weekly/issues/new "New Issue · ruanyf/weekly")
----
New Issue · ruanyf/weekly

[https://github.com/ruanyf/weekly/issues/new](https://github.com/ruanyf/weekly/issues/new "New Issue · ruanyf/weekly")
```

### 结尾

写完这篇文章的同时感觉自己对「玄学」也有了些意料之外的理解，以后有动力再写吧。。

[https://seo.chinaz.com/zbp17.wdssmq.com](https://seo.chinaz.com/zbp17.wdssmq.com "站长工具 - zbp17.wdssmq.com的SEO综合查询")
