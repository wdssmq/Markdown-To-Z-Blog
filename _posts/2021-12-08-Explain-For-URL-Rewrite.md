---
title: 「水坑」略深入的讲解伪静态相关的知识
tags:
- GesF-Force
- Rewrite
- PHP
categories:
- 电脑网络
id: 837
alias: 20190704012
---

url 理论上指向的是一个文件，即使是目录也会按默认设置寻找 index.html 或 index.php，不存在时则由 web 环境返回 404。

但是对于 Z-BlogPHP 这样的动态站点，url 指向都是 index.php，然后由内部逻辑决定是否抛出 404；

<!--more-->

让 url 指向 index.php 的实现叫 URL Rewrite，中文翻译为「伪静态」，虽然严格来说「伪静态」（Pseudo-static）只是「URL 重写」的应用之一；

Redirect 则是「重定向（301）」，虽然可以理解为带有 301 标志的 Rewrite（？）；

> 为什么叫「水坑」见：
>
> [「水坑」系列教程索引](/post/20200617652.html "「水坑」系列教程索引")

代码及讲解注释见下边 Git 链接；

每个链接对应一次「Git 提交」状态，也就是「版本控制」，你可以按顺序复制保存到你的 web 环境进行测试，比如`rewrite/index.php`；

大概理解后就换下一个「版本」覆盖进同一步件查看效果；

\---

纯动态模式 - php-rewrite/index.php · 70063e1 · 沉冰浮水/水水的旧代码合集 - Gitee.com

[https://gitee.com/wdssmq/StaleCode/blob/70063e12f67c31ba5588a2b2a0a0e3fe727ea37b/php-rewrite/index.php](https://gitee.com/wdssmq/StaleCode/blob/70063e12f67c31ba5588a2b2a0a0e3fe727ea37b/php-rewrite/index.php "php-rewrite/index.php · 沉冰浮水/水水的旧代码合集 - Gitee.com")

\---

> php-rewrite · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国：
>
> [https://gitee.com/wdssmq/StaleCode/tree/c04e9f96f4654f484510b93d7453ebf0f6c8b53f/php-rewrite](https://gitee.com/wdssmq/StaleCode/tree/c04e9f96f4654f484510b93d7453ebf0f6c8b53f/php-rewrite "php-rewrite · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")
>
> **↑ 这里可以查看效果截图（纯动态模式）**
>
> 会发现`/?id=1024`和`/post/2048.html`两种访问返回的「不存在」是不一样的；

「- 现在已经 00:41:31 了，提交一下明天继续； -」

「- 补充了几句，拖到 00:46:31 了； -」
