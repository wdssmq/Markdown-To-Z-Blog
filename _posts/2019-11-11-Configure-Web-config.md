---
title: 「备忘」web.config 设置重定向（301）
date: 2019-11-11 07:42:09
tags:
- 虚拟主机
- 备忘
- IIS
- 301
categories:
- 电脑网络
id: 838
alias: web-configSheZhiZhongDingXiang-301
---

2023-01-18：这是一篇旧文件，重新排版更新；

从 IIS7.0 开始支持通过 web.config 文件进行一些设置，包括重定向（301）。

需要服务器安装重写组件（Rewrite），下载安装或者询问空间商是否支持；

> URL Rewrite : The Official Microsoft IIS Site
>
> https://www.iis.net/downloads/microsoft/url-rewrite#additionalDownloads

安装后可以在 IIS 站点的功能视图里找到，自己添加规则外还可以将文未的的.htaccess 规则导入。。不过现在直接复制下边的示例修改要更快捷些。。

在站点根目录下创建 web.config 文件，然后复制下边内容（XML 代码）粘贴进去后再按需要修改，如果已经有 web.config 文件则按需复制`<rewrite>`或`<rule>`节点。可设置多个 URL 规则重定向到同一地址。另`<urlCompression>`节点一行为开启 GZIP 压缩。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
      <urlCompression doStaticCompression="true" doDynamicCompression="true" />
      <rewrite>
        <rules>
            <rule name="feed" stopProcessing="true">
                <match url="^(.*)$" />
                <conditions logicalGrouping="MatchAny">
                    <add input="{HTTP_HOST}" pattern="^feed.wdssmq.tk$" />
                    <add input="{HTTP_HOST}" pattern="^feed.wdssmq.com$" />
                    <add input="{URL}" pattern="^/rss.xml$" />
                </conditions>
                <action type="Redirect" redirectType="Permanent"
                    url="https://www.wdssmq.com/feed.php" />
            </rule>
            <rule name="host" stopProcessing="true">
                <match url="^(.*)$" />
                <conditions logicalGrouping="MatchAny">
                    <add input="{HTTP_HOST}" pattern="^wdssmq.tk$" />
                    <add input="{HTTP_HOST}" pattern="^www.wdssmq.tk$" />
                    <add input="{HTTP_HOST}" pattern="^wdssmq.com$" />
                    <add input="{HTTP_HOST}" pattern="^xn--37q595dihas5a.tk$" />
                    <add input="{HTTP_HOST}" pattern="^www.xn--37q595dihas5a.tk$" />
                </conditions>
                <action type="Redirect" redirectType="Permanent"
                    url="https://www.wdssmq.com/{R:0}" />
            </rule>
        </rules>
      </rewrite>
  </system.webServer>
</configuration>
```

下边附上 Linux 主机通过.htaccess 文件配置网址重定向（301）的方法，MS 要简单一些，。。然后强烈建议通过<http://feed.wdssmq.com>重新订阅本站

```conf
RewriteEngine on

RewriteCond %{http_host} ^feed.wdssmq.tk [NC]
RewriteRule ^(.*)$ http://feed.wdssmq.com$1 [L,R=301]

RewriteCond %{http_host} ^wdssmq.tk [NC,OR]
RewriteCond %{http_host} ^wdssmq.com [NC,OR]
RewriteCond %{http_host} ^www.wdssmq.tk [NC]
RewriteRule ^(.*)$ https://www.wdssmq.com/$1 [L,R=301]
```

相关文章：

\--[备忘 - IIS7 显示具体错误提示](https://www.wdssmq.com/post/BeiWang-IIS7XianShiJuTiCuoWuTiShi.html "备忘 - IIS7 显示具体错误提示")--

\--[备忘 - win7 如何启用父路径](https://www.wdssmq.com/post/bei-wang-win7ru-he-qi-yong-fu-lu-jing.html "备忘 - win7 如何启用父路径")--

\--[备忘 - IIS7 配置 web.config 开启 gzip 压缩](https://www.wdssmq.com/post/BeiWang-IIS7PeiZhiweb-configKaiQigzipYaSuo.html "备忘 - IIS7 配置 web.config 开启 gzip 压缩")--

<!--838-->
