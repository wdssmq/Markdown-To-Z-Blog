---
title: 「油猴」针对 QQ 群管理的「值日生」提示功能
date: 2021-06-15 10:56:34
tags:
- GM_脚本
- 折腾
- QQ
categories:
- 电脑网络
id: 11
alias: 20210531442
---

## 简述

又一个有点奇怪（没用）的脚本

<!--more-->

## 链接直达

\[QQ 群\] - 今天谁值日：

[https://greasyfork.org/zh-CN/scripts/427517](https://greasyfork.org/zh-CN/scripts/427517 "\[QQ 群\] - 今天谁值日")

## 说明

作用于 QQ 群管理的网页内：

> QQ 群官网-成员管理：
>
> [https://qun.qq.com/member.html](https://qun.qq.com/member.html "QQ 群官网-成员管理")

将「群主 + 群管理」按 QQ 号排序，然后每 N 人一组，每 7 天一轮换。

- 当前写死为两人一组，因为懒 —— `const config_num = 2;`
- 时间也是按时间戳直接计算，并不与周一到周日对应；
- 效果是将相应成员的名字标红显示，控制台也会打印出 QQ 号；

---没了---
