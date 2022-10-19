---
title: 「折腾」Composer In Ubuntu / WSL2
date: 2022-04-05 08:38:44
tags:
- 折腾
- PHP
- Ubuntu
- WSL2
categories:
- 电脑网络
id: 1503
alias: 20120830162
---

### 虽然但是

所以 wsl 要不要大写这种事。。。

> 「小目标」平均每篇文章/Git Repository 赚取 1 元\_杂七杂八\_沉冰浮水：
>
> [https://www.wdssmq.com/post/20210723266.html](https://www.wdssmq.com/post/20210723266.html "「小目标」平均每篇文章/Git Repository 赚取 1 元\_杂七杂八\_沉冰浮水")

<!--more-->

### 写在前边的相关推荐

[「VSCode」远程 CentOS 中 php.validate.executablePath 的设置\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20211004556.html "「VSCode」远程 CentOS 中 php.validate.executablePath 的设置\_电脑网络\_沉冰浮水")

[「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220211184.html "「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水")

## Ubuntu 下安装 PHP 7.4

```bash
# sudo apt-get upgrade

sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install -y php7.4

# 查看版本
php -v

# PHP 7.4.29 (cli) (built: Apr 21 2022 10:16:17) ( NTS )

# 查看安装路径
whereis php

# php: /usr/bin/php7.4 /usr/bin/php ……
```
· 配置 VSCode 用于 PHP 验证：

```json
{
  "php.validate.executablePath": "/usr/bin/php"
}
```

> 无法验证，因为找不到 PHP 安装。使用设置 "php.validate.executablePath" 来配置 PHP 可执行文件。
> 「[图示查看](https://www.wdssmq.com/post/20100204118.html#001)」

### 正文

姑且会写各种 Z-BlogPHP 插件，目前主要开发（折腾）环境是 `WSL2` + `Ubuntu-18.04` + `Docker`；

Docker 宿主环境内安装 PHP 主要是给 VSCode 语法验证使用；「安装方法已在上方补充」

然后部分插件有用到 Composer 安装依赖；

完整直接使用的代码：

```bash
# 添加写权限
sudo chown -R `whoami`:admin /usr/local/bin
# 进入目录
cd /usr/local/bin
# 下载安装
sudo curl -sS https://getcomposer.org/installer | php
# All settings correct for using Composer
# Downloading...

# Composer (version 2.3.3) successfully installed to: /usr/local/bin/composer.phar
# Use it: php composer.phar

# 重命名并设置别名
mv composer.phar /usr/local/bin/composer
alias composer='/usr/local/bin/composer'

composer -V
# Composer version 2.3.3 2022-04-01 22:15:35
```

如果提示没有写权限，则需要先执行 `chown -R` 加上写权限；

```bash
cd /usr/local/bin
sudo curl -sS https://getcomposer.org/installer | php
# All settings correct for using Composer
# The installation directory "/usr/local/bin" is not writable

sudo chown -R `whoami`:admin /usr/local/bin
# sudo chmod a+x /usr/local/bin

# 然后重新执行安装命令
```

网上教程都是安装或移动到 `/usr/local/bin`，然而执行会提示路径不存在，位置是 `/usr/bin`；

```bash
composer -V
# bash: /usr/bin/composer: No such file or directory

alias composer='/usr/local/bin/composer'

composer -V
# Composer version 2.3.3 2022-04-01 22:15:35
```

### 使用及遇到的其他坑

进入已经有 `composer.json` 的路径执行 `composer install`，然而我的项目报错依赖的 PHP 组件没开；

因为实际代码是跑在 Docker 里的，外边没有也无所谓，照着提示加上相应的提示就可以；

```bash
composer install
# Install or enable PHP's curl extension

# 忽略依赖缺失直接安装
composer install --ignore-platform-req=ext-curl
```


