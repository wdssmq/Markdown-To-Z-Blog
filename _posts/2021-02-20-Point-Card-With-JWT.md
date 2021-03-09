---
title: 【折腾】互联网时代的“纸制”积分卡
tags:
- 折腾
- 互联网
- 脑洞
- Z-Blog
- Z-BLogPHP
categories:
- 电脑网络
id: 397
alias: 20140425674
---

折腾了一个基于 JWT（JSON Web Tokens）的积分卡功能，由于数据使用 Cookie 存放于用户本地，弄丢了就真的丢了，发现还是蛮像「纸制」积分卡的。。

<!--more-->

因为 Z-Blog PHP 1.7 的关系折腾了两个插件：

> API 接口扩展 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=19450](https://app.zblogcn.com/?id=19450 "API 接口扩展 - Z-Blog 应用中心")
>
> Markdown 工具 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=19416](https://app.zblogcn.com/?id=19416 "Markdown 工具 - Z-Blog 应用中心")

虽然其应对的需求比较冷僻，但是自我感觉还算不上「奇怪」：

> 存在本身就比较迷的插件 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/circle/?id=6862](https://app.zblogcn.com/circle/?id=6862 "存在本身就比较迷的插件 - Z-Blog 应用中心")

所以今天又给这个列表里加了一项：

> 积分游戏 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=19573](https://app.zblogcn.com/?id=19573 "积分游戏 - Z-Blog 应用中心")

姐姐的单位搬过几次，最早所在的小区出门就有家卖包子的店，好像是买够 10 屉送一屉，店家印制的卡片，计数则是由店员在卡片上签字。。

其实这个插件算是另一个插件的改进，犹豫之后还是作为新插件发布，然后也是写完之后才发现这就是个「纸制」积分卡。。

因为一直比较执着「博客程序」的属性，其体现就是写出的功能基本都基于用户「无须注册」，虽然就结果而言会很「奇怪」就是了。。

---------------

功能要点：

- 每张「积分卡」初始分为 5；
    + 删除 Cookie/使用隔离的浏览器/匿名模式 均可重置；
- 积分可通过每日签到累计；
    + 后续会增加积分获取方式，比如 QQ、微信验证，RSS 订阅验证等；
- 积分可用于购买文章权限，但并不是 1 点对 1 篇文章，而是在某个时间周期 m （天）内，解锁整站 1/n 的文章；
    + 本插件仅为基础封装，实际锁定和购买判断需要由插件依赖实现；
    + 目前 m 和 n 均为 37；
- 在当期时间周期内解锁全部文章即为「积满」；
    + 其实这个积满是写这篇文章时想到的，判断还没写；
    + 所以积满后能干啥？？？

---------------

JWT 本身是独立插件，可以用来实现其他或许更有用的插件- -：

> JWT 存储管理 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=1813#tab-description](https://app.zblogcn.com/?id=1813#tab-description "JWT存储管理 - Z-Blog 应用中心")

---------------

还是 md2zb 工具，手欠覆盖了`.htaccess`导致`Authorization`鉴权失败- -；

解决方案为添加如下信息：

```conf
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]

# 添加下边一行
RewriteRule .* - [env=HTTP_AUTHORIZATION:%{HTTP:Authorization},last]
</IfModule>
```

wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。：

[https://github.com/wdssmq/Markdown-To-Z-Blog](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。")

<!--397-->
