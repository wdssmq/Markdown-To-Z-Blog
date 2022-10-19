---
title: 「水坑」一些 SQL 语句
date: 2021-05-20 13:05:02
tags:
- GesF-Force
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

### 修改评论作者 ID

当年从 ASP 换到 PHP，自己的评论回复记录并没有关联到用户表 - -；

```sql
-- 再条效果是一样的
UPDATE `zbp_comment` SET `comm_AuthorID` = 1 WHERE `comm_Name` = '沉冰浮水' AND `comm_AuthorID` = 0
UPDATE `zbp_comment` SET `comm_AuthorID` = 1 WHERE `comm_Name` = '沉冰浮水'
```
