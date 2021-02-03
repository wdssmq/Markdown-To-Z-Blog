---
title: 【折腾】Linux(CentOS)安装Python
tags:
- Linux
- CentOS
- Python
categories:
- 未分类
---

上接：

[【折腾】Python + GitHub Actions 更新 Z-Blog 的探索](https://zbp17.wdssmq.com/post/3.html "【折腾】Python + GitHub Actions 更新 Z-Blog 的探索")

[【折腾】VSCode远程开发配置（Remote Development）_电脑网络_沉冰浮水](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）_电脑网络_沉冰浮水")

<!--more-->

### 安装Python

```shell
python --version
# Python 2.7.5

yum -y install gcc
yum -y install zlib*
yum install readline-devel

# wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz

wget https://npm.taobao.org/mirrors/python/3.7.9/Python-3.7.9.tgz

tar -zxvf Python-3.7.9.tgz

cd Python-3.7.9

# 设置安装路径
mkdir -p /usr/local/python3
./configure --prefix=/usr/local/python3

# 编译安装
make && make install

# 软链接
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip

python3 --version

```

### 各种错误解决

- 设置Python编码

  然后发现py文件中的中文注释会报错，解决方法是在首行添加如果下注释：

  ```py
  # This Python file uses the following encoding: utf-8
  import os,sys
  ```

- GitHub Actions里的 `git diff` 问题

  `git diff "HEAD~" -r --name-only HEAD`

  > fatal: ambiguous argument 'HEAD^': unknown revision or path not in the working tree.

  理论上用双引号或者不加引号就可以，，但是GitHub Actions里是报这个错。

  `git diff --name-only head~1`

  ↑ 另外一种写法，等专门建个版本库再测试吧。。当前先用File Changes Action

- 关于VSCode的Remote - ssh插件

  ```json
  "remote.SSH.remotePlatform": {
    "losangelesvps": "linux",
    "腾讯云": "linux"
  }
  ```

  ↑↑ 理论上首次连接时会询问然后保存，但是主机名设置中文时会失败，可以手动添加；

- `github_token: ${{ secrets.GITHUB_TOKEN }}` 和 `github_token: ${{ secrets.BOT_TOKEN }}`

  在一些示例里用的是`${{ secrets.BOT_TOKEN }}`，而这个值需要自己添加使用，`${{ secrets.GITHUB_TOKEN }}` 则可以直接用。

  > "error": "500/getInputs Error",

  [File Changes Action · Actions · GitHub Marketplace](https://github.com/marketplace/actions/file-changes-action "File Changes Action · Actions · GitHub Marketplace")

- 其他
  然后还有个问题是安装不了python-frontmatter，不知道为什么；

### 其他

linux(centos)安装python - 知乎：[https://zhuanlan.zhihu.com/p/137904053](https://zhuanlan.zhihu.com/p/137904053 "linux(centos)安装python - 知乎")

<!--
git config --local user.email "wdssmq@qq.com"
git config --local user.name "wdssmq"
-->
