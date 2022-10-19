---
title: Nginx 下二级目录伪静态的标准姿势
date: 2021-11-08 11:37:13
tags:
- Nginx
- PHP
- 伪静态
categories:
- 电脑网络
id: 843
alias: 20190721016
---

Hello World

<!--more-->

```conf
# 子目录规则要排在前边；
location /sub/ {
  if (-f $request_filename/index.html) {
    rewrite (.*) $1/index.html break;
  }
  if (-f $request_filename/index.php) {
    rewrite (.*) $1/index.php;
  }
  if (!-f $request_filename) {
    rewrite (.*) /sub/index.php;
  }
}
# 根目录规则
location / {
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
