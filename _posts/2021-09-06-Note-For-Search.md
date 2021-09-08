---
title: 【真·碎碎念】2021/08/30 ~ 2021/09/05
tags:
- 碎雨集
- 碎碎念
- 纠结
categories:
- 杂七杂八
id: 852
alias: 20191011022
---

### 2021-08-31 13:38
\#备忘 Z-BlogPHP 文章表按更新时间降序查看

```sql
SELECT * FROM `zbp_post` ORDER BY `zbp_post`.`log_UpdateTime` DESC
```

<!--more-->

### 2021-09-01 08:25
第四天，疼痛仍然存在，程度上只减轻了 20%，某种意义上唯一真实的后果！

### 2021-09-02 10:58
忘记自己还开着 Visual Studio IntelliCode 了，时不时会弹出提示刷存在感；

### 2021-09-02 14:21
RSS 查看 √

水了一篇文章 √

### 2021-09-03 10:42
\#书签 feed43 同类产品 `https://fetchrss.com/`

### 2021-09-03 15:38
夏天过去了。。时不时会梦到下雪，然而又几乎都会联系到上学、迟到之类的。。so sad

### 2021-09-05 15:54
又是周日，要不今天把碎碎念更新了？Z-BlogPHP 的 RSS 仍然不能按更新时间排序也是个问题；

### 2021-09-05 16:11
一周总结「- 雾

1、新主题只有首页完成了；

2、打算弄个`I'M 名片生成`；

3、还打算弄个`RSS We`；

### 2021-09-05 16:23
\#书签

「折腾」ESLint 安装与使用_电脑网络_沉冰浮水`https://www.wdssmq.com/post/20190917021.html` ←不知道 Bing 会不会收录这条嘟；

### 2021-09-05 18:23
Prettier 和 ESLint 果然是有些重复

### 2021-09-05 20:44
为什么 Linux 上的很多东西都要自己编译安装。。

### 2021-09-05 21:10
这种类型的 Z-BlogPHP 插件官方坚持要求收费，背后的原因……


### 2021-09-08 20:18 - 还是 crontab

安装位置：

`which crontab`

`# /usr/bin/crontab`

查看定时任务：

`crontab -l`

创建 / 编辑 任务：

`crontab -e`

VSCode 编辑查看：

`code /etc/crontab`

↑ `crontab -e` 和 `crontab -l` 看不到这个；

VSCode 编辑查看：

`code /var/spool/cron/root`

↑ root 为当前用户，等同于 `crontab -e`

```shell
service crond start # 启动服务
service crond stop # 关闭服务
service crond restart # 重启服务
service crond reload # 重新载入配置
crontab -l
service crond status # 查看crontab服务状态
```
