---
title: 「笔记」.htaccess 及 nginx.conf 可用变量一览
date: 2022-05-30 12:51:31
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
| %{HTTP_USER_AGENT}  | $http_user_agent  | 客户端 UA                   |
| %{REMOTE_ADDR}      | $remote_addr      | 访问来源 IP                 |

`$scheme://$host/`或`%{REQUEST_SCHEME}://%{HTTP_HOST}/`可直接拼接出当前网址；

--------------

mod\_rewrite 参考文档\_Apache 中文文档：

[https://www.apachehttpd.com/mod/mod_rewrite.html](https://www.apachehttpd.com/mod/mod_rewrite.html "mod\_rewrite参考文档\_Apache中文文档")

Htaccess - THE Ultimate .htaccess tutorial with 100's of Examples：

[https://www.askapache.com/htaccess/#Htaccess_Variables](https://www.askapache.com/htaccess/#Htaccess_Variables "Htaccess - THE Ultimate .htaccess tutorial with 100's of Examples")

----------------

一．正则表达式匹配，其中：

* `~` 为区分大小写匹配；
* `~*` 为不区分大小写匹配；
* `!~` 和 `!~*` 分别为区分大小写不匹配及不区分大小写不匹配；

二．文件及目录匹配，其中：

* `-f` 和 `!-f` 用来判断是否存在文件；
* `-d` 和 `!-d` 用来判断是否存在目录；
* `-e` 和 `!-e` 用来判断是否存在文件或目录；
* `-x` 和 `!-x` 用来判断文件是否可执行；

三．rewrite 指令的最后一项参数为 flag 标记，flag 标记有：

- `last`       对重写后的 URI 发起新请求，最终效果取决于新请求能否匹配到另外的规则；「好像相当于 apache 里面的`[L]`标记」
- `break`      当前指令指定的新 URI 既最终结果；
- `redirect`   返回 302 临时重定向，浏览器地址会显示跳转后的 URL 地址；
- `permanent`  返回 301 永久重定向，浏览器地址会显示跳转后的 URL 地址；

---------------

2022 年了我才知道 Nginx 配置里不能直接用「与」「或」运算什么的？

```conf
# 用来查看访问的 IP，仅测试用
location ~* ^/ip/[\d-]+ {
    # default_type 不能用在下边 if 内
    default_type    text/plain;
    return 200      "${remote_addr}";
}

# 匹配某个路径
# if ($uri ~* ^/SomePath) {
    # ………………
# }

# -----------------

# 默认为 0
set $pass 0;

# 当任意一个条件符合就将 $pass 设置为 1；
# 相当于「或」运算；

# 判断 UA
if ($http_user_agent ~* Edg/\d+) {
    set $pass 1;
}

# 判断 IP
if ($remote_addr ~* 172.*) {
    set $pass 1;
}

# 不为 1 时拒绝访问
if ($pass != 1) {
    return 403;
}

# -----------------

set $flag 0;

# 要求符合全部条件
# 相当于「与」运算；

# 判断 UA
if ($http_user_agent ~* Edg/\d+) {
    set $flag "${flag}1";
}

# 判断 IP
if ($remote_addr ~* 172.*) {
    set $flag "${flag}1";
}

# 结果不匹配时拒绝访问
if ($flag != "011") {
    return 403;
}

```

------------------------

Nginx 实现仅允许搜索引擎或指定 IP 访问：

```conf
# 沉冰浮水（wdssmq）
location / {
    set $pass 0;
    # 判断 UA
    if ($http_user_agent ~* (Baiduspider|YisouSpider|360Spider|HaosouSpider|bingbot|Sosospider|Sosoimagespider|Bytespider|Sogou web spider|Sogou inst spider|Sogou News Spider|Sogou Pic Spider|Sogou Video Spider|Googlebot|Googlebot-Image|AdsBot-Google-Mobile)) {
        set $pass 1;
    }
    # 判断 IP
    if ($remote_addr ~* (123.123.123.123|192.168.0.\d+)) {
        set $pass 1;
    }
    # 不为 1 时拒绝访问
    if ($pass != 1) {
        return 403;
    }
    # 伪静态什么的其他规则
}
```
