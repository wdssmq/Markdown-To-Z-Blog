---
title: 合并了 Typecho 文章到 Z-Blog
tags:
- PHP,折腾,Typecho,Z-Blog
categories:
- 电脑网络
id: 3098
alias: 20200905897
---

### 几句话就能概括的标题

使用的方案是按照 MovableType 语法给 Typecho 弄了个“主题”，150 条数据在一页显示后另存，再使用相应插件导入到 z-blog；

> 适用于 Z-Blog 的 MovableType 语法规范\_电脑网络\_沉冰浮水
>
> <a href="https://www.wdssmq.com/post/20170502785.html" target="_blank" title="适用于Z-Blog的MovableType语法规范_电脑网络_沉冰浮水">https://www.wdssmq.com/post/20170502785.html</a>
>
> MT 数据格式导入【PHP】 - Z-Blog 应用中心
>
> <a href="https://app.zblogcn.com/?id=928" target="_blank" title="MT数据格式导入【PHP】 - Z-Blog 应用中心">https://app.zblogcn.com/?id=928</a>

### 关于符号链接（symlinks）

然后推荐一个叫`HardLinkShellExt`的东西，算是对`mklink`命令的封装。

前边的主题打算放进插件里发布，而开发调试要在 Typecho 的目录里，直接复制的话会显得很蛋疼。。

目测符号连接和目录连接都可以，Web 环境用的 EasyPHP。

|          | 文件 | 目录 | 相对地址 | 绝对地址 | PHP 可访问 | Git |
| -------- | ---- | ---- | -------- | -------- | ---------- | --- |
| 符号连接 | √    | √    | √        | √        | √          | ×   |
| 目录连接 | ×    | √    | ×        | √        | √          | √   |
| 硬连接   | √    | ×    | ○        | ○        | √          | √   |

大概是这个感觉，另外 OneDrive 同步时也可以用。

**注：Git 通过开启相应的设置也是可以支持符号连接的：**

- [【备忘】msysGit 安装及使用](https://www.wdssmq.com/post/20140804123.html "【备忘】msysGit安装及使用") ←差不多最后一步有个「symlinks」相关的选项。
- 然后在 `.git/config` 中开启「core.symlinks」

### 最后备忘一条 SQL

```sql
SELECT * FROM `zbp_post` WHERE `log_Alias` IN (SELECT `log_Alias` FROM `zbp_post` GROUP BY `log_Alias` HAVING COUNT(`log_Alias`)>1)
```
<!--3098-->
