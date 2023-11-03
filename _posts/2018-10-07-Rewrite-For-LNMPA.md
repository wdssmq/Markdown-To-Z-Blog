---
title: 「备忘」LNMPA 伪静态/301 相关
date: 2018-10-07 09:38:54
tags:
- LNMP
- 301
- 伪静态
- 备忘
categories:
- 电脑网络
id: 2861
alias: 20181007103
---

之前经过折腾终于配置好了 ssl 证书，，然后 301 和伪静态什么就需要相应的调整。

因为迷之执着现在用的 LNMPA，需要兼顾 apache 和 nginx 两份配置：

<!-- more -->

`/usr/local/apache/conf/vhost/wdssmq.com.conf`

`/usr/local/nginx/conf/vhost/wdssmq.com.conf`

`/home/wwwroot/wdssmq.com/.htaccess`

前两份在自动生成的基础上微调就可以。

**要点：http 跳转 https 只能在 nginx 中配置。**

```conf
server
{
    listen 80;
    # listen [::]:80;
    server_name www.wdssmq.com wdssmq.com feed.wdssmq.com;
    return 301 https://$host$request_uri;
}

server
{
    listen 443 ssl http2;
    # listen [::]:443 ssl http2;
    server_name www.wdssmq.com wdssmq.com feed.wdssmq.com;
    # ……………………
    # ……
    # ……
}
```

其他的都可以在 .htaccess 实现：

```conf
<IfModule mod_rewrite.c>

RewriteEngine On
RewriteBase /

RewriteCond %{http_host} ^feed.wdssmq.com$ [NC]
RewriteCond %{request_uri} !^/feed.php [NC]
RewriteRule ^(.+)$ https://feed.wdssmq.com [L,R=301]

RewriteCond %{http_host} ^feed.wdssmq.com$ [NC]
RewriteCond %{request_uri} !^/feed.php [NC]
RewriteRule . /feed.php [L]

RewriteRule ^feed.asp /feed.php [L]
RewriteRule ^rss.xml /feed.php [L]

RewriteCond %{http_host} !^www.wdssmq.com [NC]
RewriteCond %{http_host} !^feed.wdssmq.com [NC]
RewriteRule ^(.*)$ https://www.wdssmq.com/$1 [L,R=301]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+[^/])$ /$1/ [L,R=301]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
```

相关推荐：

[「备忘」Nginx 重定向（301）相关\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140819797.html "「备忘」Nginx 重定向（301）相关\_电脑网络\_沉冰浮水")

[「折腾」Nginx 解析网址参数并跳转\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20201107566.html "「折腾」Nginx 解析网址参数并跳转\_电脑网络\_沉冰浮水")

[「备忘」LNMPA 伪静态/301 相关\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20181007103.html "「备忘」LNMPA 伪静态/301 相关\_电脑网络\_沉冰浮水")「当前」

[「笔记」LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20200129996.html "「笔记」LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水")

<!--2861-->
