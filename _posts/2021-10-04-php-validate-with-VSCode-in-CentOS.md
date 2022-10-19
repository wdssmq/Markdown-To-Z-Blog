---
title: 「VSCode」远程 CentOS 中 php.validate.executablePath 的设置
date: 2021-10-04 11:58:00
tags:
- VSCode
- PHP
- CentOS
categories:
- 电脑网络
id: 8
alias: 20211004556
---

> CentOS Linux 要停止维护了，然而更换好麻烦。。

会远程编辑测试一些东西，挂载进 Docker 里运行；

VSCode 每次都会提示`php.validate.executablePath`未设置，虽然之后使用好像没啥影响；

尝试宿主机里单独安装一个 PHP 给 VSCode；

<!--more-->

[Remote Development - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack "Remote Development - Visual Studio Marketplace")


```shell
# 直接安装
yum install php

php -v
# PHP 5.4.16 (cli) (built: Apr  1 2020 04:07:17)
# ↑ 版本略底

whereis php
# php: /usr/bin/php /usr/lib64/php /etc/php.d /etc/php.ini /usr/share/php /usr/share/man/man1/php.1.gz
```

果然不太懂：

```json
{
"php.validate.executablePath": "/usr/bin/php"
}
```

研究了下 CentOS 官方的 SCL，但是感觉和预想不太一样；

```shell
# 安装 SCL（Software Collections）
yum install centos-release-scl-rh

# 搜索
yum search php
# rh-php73.x86_64
# ↑ 大概安装这个就行吧

yum install rh-php73.x86_64

# 列出 scl 安装的库
scl -l
# rh-php73

scl enable rh-php73 "php -v"
# PHP 7.3.29 (cli) (built: Aug  3 2021 12:26:40) ( NTS )

cd /opt/rh/rh-php73 && ls
# deregister  deregister.d  enable  register  register.content  register.d  root
```
