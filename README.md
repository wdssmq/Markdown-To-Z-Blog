# Markdown-To-Z-Blog

同步*.md 内容到 Z-Blog

---start---

## 目录( 2021 年 02 月 07 日更新)

[【折腾】麦沃硬盘盒报毒的应对方案](https://zbp17.wdssmq.com/post/16.html "【折腾】麦沃硬盘盒报毒的应对方案")

[【言说】不知道发没发的《黑豹》评论](https://zbp17.wdssmq.com/post/15.html "【言说】不知道发没发的《黑豹》评论")

[【折腾】VSCode 远程开发配置（Remote Development）](https://zbp17.wdssmq.com/post/14.html "【折腾】VSCode 远程开发配置（Remote Development）")

[关于 Z-BlogPHP 1.7 缩略图的一些记录](https://zbp17.wdssmq.com/post/13.html "关于 Z-BlogPHP 1.7 缩略图的一些记录")

[合并了 Typecho 文章到 Z-Blog](https://zbp17.wdssmq.com/post/12.html "合并了 Typecho 文章到 Z-Blog")

[【备忘】Z-BlogPHP 常用接口或函数](https://zbp17.wdssmq.com/post/11.html "【备忘】Z-BlogPHP 常用接口或函数")

[【折腾】GM_脚本修改 bilibili 番剧链接为我的追番](https://zbp17.wdssmq.com/post/4.html "【折腾】GM_脚本修改 bilibili 番剧链接为我的追番")

[【折腾】Linux(CentOS)安装 Python](https://zbp17.wdssmq.com/post/5.html "【折腾】Linux(CentOS)安装 Python")

[【言说】相对擅长写代码，然而也只有写代码](https://zbp17.wdssmq.com/post/8.html "【言说】相对擅长写代码，然而也只有写代码")

[【笔记】LNMP 部署/续期 SSL 证书](https://zbp17.wdssmq.com/post/10.html "【笔记】LNMP 部署/续期 SSL 证书")

[【言说】停不下的写作和代码](https://zbp17.wdssmq.com/post/9.html "【言说】停不下的写作和代码")

[使用 GitHub Actions + Markdown 更新 Z-Blog 博客](https://zbp17.wdssmq.com/post/7.html "使用 GitHub Actions + Markdown 更新 Z-Blog 博客")

[【折腾】pip 安装各种依赖遇到的坑](https://zbp17.wdssmq.com/post/6.html "【折腾】pip 安装各种依赖遇到的坑")

[欢迎使用 Z-BlogPHP！](https://zbp17.wdssmq.com/post/1.html "欢迎使用 Z-BlogPHP！")

[【折腾】Python + GitHub Actions 更新 Z-Blog 的探索](https://zbp17.wdssmq.com/post/3.html "【折腾】Python + GitHub Actions 更新 Z-Blog 的探索")

---end---

zhaoolee/WordPressXMLRPCTools: 用 Hexo 的方式管理 WordPress
[https://github.com/zhaoolee/WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools "zhaoolee/WordPressXMLRPCTools: 用Hexo的方式管理WordPress")

## 命令（本地测试）

```shell
pip install markdown
pip install requests
pip install python-frontmatter
```

创建 config.json 并按如下示例填写内容：

```json
{
    "API_USR": "zblog_usr",
    "API_PWD": "zblog_pwd",
    "API_URL": "http://zblog.site/zb_system/api.php"
}
```

运行：

`python api.py`

## 文章书写

### 存放路径

支持两种形式，需要配图的文章可以创建一个文件夹存放。

- _posts/*.md
- _posts/*/doc.md

### 内容格式

- 可以直接复制`_posts/1970-01-01-empty.md`；
- 对于 VSCode ，可以使用快捷命令`ctrl + shift + b`；【2021-02-05】
  - **注：会同时创建文件夹和单文件两种形式，按需改名使用即可；**
  - **注：未改名的会被`.gitignore`排除；**

```md
---
title: 文章标题
tags:
- 标签一
- 标签二
categories:
- 分类名
---

正文段落一

<!--more-->

正文段落二

```
