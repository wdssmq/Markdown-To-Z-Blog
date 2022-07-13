---
title: 【Ubuntu 笔记】常见错误提示整理
date: 2013-11-01 11:03:40
tags:
- Linux
- Ubuntu
- 备忘
categories:
- 电脑网络
id: 1877
alias: 20131101035
---

错误提示：

> manpath: can't set the locale; make sure $LC_* and $LANG are correct

<!--more-->

解决：

1、分别执行 `locale` 和 `localectl list-locales` 查看数输出：

```bash
locale
# locale: Cannot set LC_CTYPE to default locale: No such file or directory
# locale: Cannot set LC_MESSAGES to default locale: No such file or directory
# locale: Cannot set LC_ALL to default locale: No such file or directory
# LANG=en_US.UTF-8
# LANGUAGE=
# LC_CTYPE="en_US.UTF-8"
# LC_NUMERIC="en_US.UTF-8"
# LC_TIME="en_US.UTF-8"
# LC_COLLATE="en_US.UTF-8"
# LC_MONETARY="en_US.UTF-8"
# LC_MESSAGES="en_US.UTF-8"
# LC_PAPER="en_US.UTF-8"
# LC_NAME="en_US.UTF-8"
# LC_ADDRESS="en_US.UTF-8"
# LC_TELEPHONE="en_US.UTF-8"
# LC_MEASUREMENT="en_US.UTF-8"
# LC_IDENTIFICATION="en_US.UTF-8"
# LC_ALL=

localectl list-locales
# C.UTF-8
```

2、修改文件`/etc/locale.gen`，在其中搜索`en_US.UTF-8`对应的项目，移除前边的`#`注释；

```bash
# 编辑如下文件
code /etc/locale.gen
# —— # en_US.UTF-8 UTF-8 修改为 en_US.UTF-8 UTF-8
```

3、执行 `locale-gen`；

```shell
# locale-gen
locale-gen

# 重新执行查看命令验证效果
localectl list-locales
# C.UTF-8
# en_US.utf8

locale
# LANG=en_US.UTF-8
# LANGUAGE=
# …………
```

\-----

错误提示：

> Package docker-ce is not available, but is referred to by another package.

解决方法：

```shell
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
```

\-----

错误提示：

> Failed to execute child process "dbus-launch" (No such file or directory)

解决方法：

> apt-get remove golang-docker-credential-helpers

\-----

错误提示：

> sudo: unable to resolve host localhost.localdomain

解决方法：

编辑/etc/hosts，将

> 127.0.0.1 localhost

修改为：

> 127.0.0.1 localhost localhost.localdomain
>
> //也可以加上你的域名，如
>
> 127.0.0.1 localhost localhost.localdomain vps.wdssmq.com

\-----

错误提示：

> Missing: Digest::SHA1

解决方法：

> cd /tmp
>
> wget http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-SHA1-2.13.tar.gz
>
> tar -zxvf Digest\*.tar.gz
>
> cd Digest\*
>
> perl Makefile.PL
>
> make
>
> make test
>
> make install

\-----

错误提示：

> requires either NcursesW or Ncurses library
>
> Could not build sigc++-2.0

解决方法：

> //在安装 rtorrent + rutorrent 时遇到的两种错误提示，，精简版系统少太多东西，，统一安装一下
>
> sudo apt-get install libtool automake build-essential libssl-dev libsigc++-2.0-dev libc6-dev libncurses5-dev subversion libcppunit-dev unzip unrar-free curl

\-----

错误提示：

> WARNING: failed to autodetect C++ compiler version (CXX=g++)
>
> WARNING: failed to autodetect C compiler version (CC=gcc)
>
> ERROR: No acceptable C compiler found!
>        Please make sure you have a C compiler installed on your system and/or
>        consider adjusting the CC environment variable if you installed
>        it in a non-standard prefix.

解决：

```bash
sudo apt-get install gcc
sudo apt-get install build-essential
```

<!--1877-->
