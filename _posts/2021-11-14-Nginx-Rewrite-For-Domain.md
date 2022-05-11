---
title: 「备忘」nginx 重定向(301)相关
tags:
- LNMP,Linux,301,Nginx
categories:
- 电脑网络
id: 2346
alias: 20140819797
---

LNMP 网站配置路径：

> `/usr/local/nginx/conf/vhost/`

然后编辑`域名.conf`文件；

**根域名跳转到 www：**

```conf
server {
    listen 443 ssl http2;
    server_name www.wdssmq.com feed.wdssmq.com wdssmq.com;

    #……………………

    # 一般在 server_name 下边，自己找合适的位置
    if ($host = 'wdssmq.com' ) {
        rewrite ^/(.*)$ https://www.wdssmq.com/$1 permanent;
    }
    # 如有伪静态规则，则放在这里
    if (-f $request_filename/index.html) {
        rewrite (.*) $1/index.html break;
    }
    if (-f $request_filename/index.php) {
        rewrite (.*) $1/index.php;
    }
    if (!-f $request_filename) {
        rewrite (.*) /index.php;
    }
}
```

**另外的写法：**

```conf
server {
    listen 443 ssl http2;
    server_name demo.wdssmq.com zbp17.wdssmq.com;

    #……………………

    # 一般在 server_name 下边，自己找合适的位置
    if ($host != 'demo.wdssmq.com' ) {
        rewrite ^/(.*)$ http://demo.wdssmq.com/$1 permanent;
    }

    #……………………
}
```

然后重启 nginx

```bash
/usr/local/nginx/sbin/nginx -s reload
```

下边命令为重启 lnmp

```bash
/root/lnmp restart
```

相关推荐：

[「折腾」Nginx 解析网址参数并跳转\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20201107566.html "「折腾」Nginx 解析网址参数并跳转\_电脑网络\_沉冰浮水")

[「备案」LNMPA 伪静态/301 相关\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20181007103.html "「备案」LNMPA 伪静态/301 相关\_电脑网络\_沉冰浮水")

[「笔记」LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20200129996.html "「笔记」LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水")

<!--2346-->
