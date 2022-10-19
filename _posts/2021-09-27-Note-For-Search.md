---
title: 【真·碎碎念】2021/09/20 ~ 2021/09/26
date: 2021-09-27 15:33:39
tags:
- 碎雨集
- 碎碎念
- 纠结
categories:
- 杂七杂八
id: 137
alias: 20100305270
---
### 2021-09-20 10:42
正好今天星期一，可以测试下新写的 mdLint 插件。`https://marketplace.visualstudio.com/items?itemName=wdssmq.mdlint` 「- 之前经常拖延到周四什么的 -」

<!-- more -->

### 2021-09-20 10:51
接上条，虽然还需要慢慢优化；

### 2021-09-23 08:55
很多问题确实可以应对，然而好像总是欠缺些什么，比如上一家也有送盒子，但是太大了结果耳塞还是消失在了洗衣机里！这次在盒子问题上确实是意料之外的进步，因为下单的时候并不知道送的盒子能否合用！终究来说，「需要应对」本身就是最迫切想要不用应对的！

### 2021-09-23 11:40
终于写了点儿正式的内容到 logseq 里；

### 2021-09-24 11:57
\#书签 可视化代码执行：`https://pythontutor.com/`；

### 2021-09-24 11:58
\#书签 使用 GitHub 接口转换 Markdown 为 HTML：`https://github.com/calganaygun/MDcat`

### 2021-09-24 12:34
今天我的博客空间挂了，然后 APP 里显示已经 60 天没备份数据了，，，工具什么的，终究架不住人懒。

### 2021-09-24 12:37
终于更新了：《小绿和小蓝》360 魔王 15-造物主-在线漫画-腾讯动漫官方网站 `https://ac.qq.com/ComicView/index/id/536332/cid/826`

### 2021-09-26 14:11
\#书签 一篇对电影《教父》的解析：`https://www.zhihu.com/question/488054014/answer/2137288235`

### 2021-09-27 16:06 总结
最近两次到是很及时的发在周一；

### 2021-09-28 20:04
《掟上今日子的备忘录》真人版里男主打工经验多这一点体现的蛮充分。

### 2021-09-29 19:14
\#无从复盘的过往 普通高中转到职中那一年，数学老师叫学生到黑板上解题时会以一种轻快的语调「提醒」“写高点儿”，14 年过去了仍然能在脑内播放出这句话的感觉；同样的，英语老师，同时也是班主任，怎么也想不起她是用怎样的字词和语气表过同样的含义的。前几天我好像也听到过一句话，以当时来说我应该每个字都有听清楚，偏偏也是完全回忆不起来。

### 2021-09-30 19:07
\#备忘 `find /|grep nginx.conf`

### 2021-10-07 13:26
CentOS 升级 Python；

\#Python \#CentOS

[https://www.python.org/ftp/python/](https://www.python.org/ftp/python/ "Index of /ftp/python/")

```sh
yum install gcc libffi-devel python-devel openssl-devel

cd /root/tmp
# 下载并解压
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
tar -xzvf Python-3.9.6.tgz

# 进入目录
cd /root/tmp/Python-3.9.6

# 创建安装路径
mkdir /usr/local/python3
# 指定安装路径
./configure --prefix=/usr/local/python3 --enable-loadable-sqlite-extensions
# 编译安装
make
make install

# 旧版改名后链接新到到原路径
mv /usr/bin/python /usr/bin/python_old2
ln -s /usr/local/python3/bin/python3  /usr/bin/python
ln -s /usr/local/python3/bin/pip3  /usr/bin/pip

# poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
ln -s /root/.local/bin/poetry  /usr/bin/poetry

# /root/.local/bin/cookiecutter
pip install --user cookiecutter
ln -s /root/.local/bin/cookiecutter  /usr/bin/cookiecutter
cookiecutter gh:rsserpent/template
```

### 2021-10-07 15:11
Window 安装 poetry

```shell
(Invoke-WebRequest -Uri https://cdn.jsdelivr.net/gh/python-poetry/poetry@master/get-poetry.py -UseBasicParsing).Content | python -

```

### 2021-10-07 13:44:50
Git 命令行修改远程地址；

\#Git

```bash
git remote set-url origin url
```
<!--
git remote set-url origin git@github.com:wdssmq/rsserpent-plugin-bilibili.git
-->

find /|grep poetry


### 2021-10-07 18:03

\#Python \#CentOS

> ModuleNotFoundError: No module named '_sqlite3'
> `https://www.jianshu.com/p/dd4532457b9f`

```shell

cd /root/tmp
# 下载并解压
wget http://www.sqlite.org/snapshot/sqlite-snapshot-202110061004.tar.gz
tar -xzvf sqlite-*.tar.gz

# 进入目录
cd /root/tmp/sqlite-*

# 创建安装路径
mkdir /usr/local/sqlite
# 指定安装路径
./configure --prefix=/usr/local/sqlite
# 编译安装
make
make install
# exit


find / -name _sqlite*.so

# /usr/local/python3/lib/python3.9/lib-dynload/_sqlite3.cpython-39-x86_64-linux-gnu.so
# /usr/lib64/python2.7/site-packages/_sqlitecache.so
# /usr/lib64/python2.7/lib-dynload/_sqlite3.so

cp /usr/local/python3/lib/python3.9/lib-dynload/_sqlite3.cpython-39-x86_64-linux-gnu.so \
   /usr/local/python3/lib/python3.9/lib-dynload/_sqlite3.so

```
