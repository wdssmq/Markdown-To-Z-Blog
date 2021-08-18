---
title: 【备忘】一些 SQL 语句
tags:
- MySQL
- 折腾
- 备忘
categories:
- 电脑网络
id: 601
alias: 20120816277
---

一些偶尔会用到的命令备忘，主要是和 Z-BlogPHP 相关；

<!--more-->

### 查询别名重复的文章

```sql
SELECT * FROM `zbp_post` WHERE `log_Alias` IN (SELECT `log_Alias` FROM `zbp_post` GROUP BY `log_Alias` HAVING COUNT(`log_Alias`)>1)
```

### 替换图片地址

```sql
update `zbp_post` set `log_Content`=(REPLACE(`log_Content`,'{#ZC_BLOG_HOST#}zb_users/upload/','https://cdn.adadd.com/XXXXX/'));
```

### 搜索

```sql
SELECT * FROM `zbp_post` WHERE `log_Content` LIKE '%202012141607949338840263%';
SELECT * FROM `zbp_post` WHERE `log_Content` LIKE '%{#ZC_BLOG_HOST#}zb_users/%';
```
