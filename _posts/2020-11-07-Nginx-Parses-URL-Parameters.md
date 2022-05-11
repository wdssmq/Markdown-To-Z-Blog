---
title: 「折腾」Nginx 解析网址参数并跳转
tags:
- 301
- LNMP
- Nginx
- 折腾
categories:
- 电脑网络
id: 3106
alias: 20201107566
---

演示网址: [https://demo.wdssmq.com/?id=2887](https://demo.wdssmq.com/?id=2887 "演示地址")

对于如上地址，在 Apache 下可以使用如下规则重定向（301）到伪静态地址。

```conf
RewriteCond %{QUERY_STRING} ^id=(.+)$ # 这里的引用是 %1 而不是 $1
RewriteRule ^$ /post/%1.html [L,R=301]
```

至于 Nginx，同时有`$query_string`与`$args`两个变量用于获取网址参数，效果好像是一样的；

注：`$arg_id.html`后的`?`表示跳转后不携带原来的网址参数；

```conf
# page + post
if ($args ~* "id=\d+") {
    rewrite ^/$ $scheme://$host/post/$arg_id.html? permanent;
}
```

↑↑上述代码的 if 语句中使用了正则判断，但是并没有对匹配结果进行捕获，而是使用了`$arg_id`直接获取到了相应值，同理其他参数也可以使用`$arg_参数名`来获取。

演示地址实际跳转了两次，第二次由 id 跳转到了别名，该效果由插件\[[改版助手 - Z-Blog 应用中心](https://app.zblogcn.com/?id=1284 "改版助手 - Z-Blog 应用中心")\]实现。。

2022-05-11：

当年写这篇记录时还没弄 md2zb 体系来发文章，然后因为 301 会被浏览器缓存，清理的时候一并清掉了登录状态，结果编辑好文章发布时失败了。。

正确的清理姿势见：[「水坑」浏览器内清理特定网站的 301 缓存\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20211130948.html "「水坑」浏览器内清理特定网站的 301 缓存\_电脑网络\_沉冰浮水")


<!--3106-->
