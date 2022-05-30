---
title: 「笔记」.htaccess 及 nginx.conf 可用变量一览
tags:
- 笔记
- Apache
- Nginx
- 折腾
categories:
- 电脑网络
id: 941
alias: 20220301043
---

自己搜索能力明明不算低，但是好多东西并不能快速找到还是好纠结；

<!--more-->

| .htaccess           | nginx.conf        | 说明                        |
| ------------------- | ----------------- | --------------------------- |
| %{REQUEST_SCHEME}   | $scheme           | http /https                 |
| %{HTTP_HOST}        | $host             | 域名 / ip                   |
| %{REQUEST_URI}      | $request_uri      | host/ 后边的部分            |
| %{REQUEST_FILENAME} | $request_filename | 一般情况下好像有 uri 一样？ |
| %{QUERY_STRING}     | $args             | 查询字符串（`?`后边的部分） |

`$scheme://$host/`或`%{REQUEST_SCHEME}://%{HTTP_HOST}/`可直接拼接出当前网址；

--------------

mod\_rewrite 参考文档\_Apache 中文文档：

[https://www.apachehttpd.com/mod/mod_rewrite.html](https://www.apachehttpd.com/mod/mod_rewrite.html "mod\_rewrite参考文档\_Apache中文文档")

Htaccess - THE Ultimate .htaccess tutorial with 100's of Examples：

[https://www.askapache.com/htaccess/#Htaccess_Variables](https://www.askapache.com/htaccess/#Htaccess_Variables "Htaccess - THE Ultimate .htaccess tutorial with 100's of Examples")
