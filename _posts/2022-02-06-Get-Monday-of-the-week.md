---
title: 「PHP」获取指定时间所在周的第一天（星期一）
tags:
- PHP
- 折腾
categories:
- 电脑网络
id: 498
alias: 20190704010
---

下边 Z-BlogPHP 应用里用到了「获取时间戳所在周的第一天」的功能，然而一开始的实现并不对「- -」；

<!--more-->

> 碎雨集 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=21047](https://app.zblogcn.com/?id=21047 "碎雨集 - Z-Blog 应用中心")

一开始是想直接拿到`00:00:00`的时间戳，果然太麻烦了就容易出错；

```php
function mz_ShikonNoTama_GetCurMonday($time)
{
  // 错误实现
  // $w = date("N", $time);
  // return $time - ($time % 86400) - 86400 * ($w - 1) - 3600 * 8;

  // 正确实现
  $week = date("N", $time);
  return $time - ($week - 1) * 86400;

  // 如果确实要拿 00:00 好像可以这样
  // $week = date("N", $time);
  // return $time - ($week - 1) * 86400 - (($time + 28800) % 86400);
}
```


```php
$arr = [1642896000, 1642953599, 1642953600, 1642957612];
$rltHTML = '';
for ($i = 0; $i < count($arr); $i++) {
  $time = $arr[$i];
  $date = date("Y-m-d H:i", $time);
  $week = date("N", $time);
  $monday = $time - ($week - 1) * 86400;
  // $monday = $time - ($week - 1) * 86400 - (($time + 28800) % 86400);
  $rltHTML .= strtr($tpl, [
    '{key}' => 'time',
    '{value}' => $date,
  ]);
  $rltHTML .= strtr($tpl, [
    '{key}' => 'week',
    '{value}' => $week,
  ]);
  $rltHTML .= strtr($tpl, [
    '{key}' => 'monday',
    '{value}' => date("Y-m-d H:i", $monday),
  ]);
  $rltHTML .= "<br>";
}

echo $rltHTML;

// N	               丨 ISO-8601 格式数字表示的星期中的第几天 丨 1（表示星期一）到 7（表示星期天）
// w	               丨 星期中的第几天，数字表示	            丨 0（表示星期天）到 6（表示星期六）
// D	               丨 星期中的第几天，文本表示，3 个字母     丨 Mon 到 Sun
// l（“L”的小写字母） 丨 星期几，完整的文本格式	               丨 Sunday 到 Saturday
```

```text
time：2022-01-23 08:00

week：7

monday：2022-01-17 08:00


time：2022-01-23 23:59

week：7

monday：2022-01-17 23:59


time：2022-01-24 00:00

week：1

monday：2022-01-24 00:00


time：2022-01-24 01:06

week：1

monday：2022-01-24 01:06
```
