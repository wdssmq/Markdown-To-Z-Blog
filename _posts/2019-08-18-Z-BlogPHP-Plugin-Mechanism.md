---
title: 「教程」Z-Blog 插件运作机制简述
date: 2019-08-18 13:27:36
tags:
- GesF-Force
- Z-Blog
- 独立博客
categories:
- 电脑网络
id: 2922
alias: 20190817262
---

[TOC]

## 基于 include.php 的标准用法

可以类比一列火车。。出发时会从数据库带上固定的货物，，可以在途经的站点向指定的车箱内增加东西。。或者干脆加挂车箱。再或者把车上的东西搬下来加工一下再搬回来。

所有预定的操作都需要在出发前申请。。

```php
// 申请人“demoPlugin”，具体申请事项见 ActivePlugin_demoPlugin 函数
RegisterPlugin("demoPlugin","ActivePlugin_demoPlugin");

function ActivePlugin_demoPlugin() {
  // 在名为 Filter_Plugin_Index_Begin 的站点停靠，停靠后干啥见 demoPlugin_hello
  Add_Filter_Plugin('Filter_Plugin_Index_Begin', 'demoPlugin_hello');
}

function demoPlugin_hello()
{
  // 在第一节车箱放一箱橘子【雾
  global $zbp;
  $zbp->header .= '<script>alert("hello")</script>';
}

```
预约制和买票上车制的不同是，前者到站后你要等叫号，叫到你你再上。

列车发车后，“车长”手里会有这样一份表格，而前边的 `Add_Filter_Plugin()` 函数就相当于填写这张表；

| 站点名                    | 事项列表              |
| ------------------------- | --------------------- |
| aaa                       | eeee,ttew,aewe        |
| Filter_Plugin_Index_Begin | demoPlugin_hello,XXXX |
| nnn                       |                       |

```php
// 到达名为Filter_Plugin_Index_Begin的站点后，对应表格执行相应的事项
foreach ($GLOBALS['hooks']['Filter_Plugin_Index_Begin'] as $fpname => &$fpsignal) {
    $fpname();
}

```

## 插件自己新开一条铁路

插件下新建一个 `api.php` 文件然后写入如下示例

```php
<?php
// 引入必要的系统文件
require '../../../zb_system/function/c_system_base.php';
// 初始化
$zbp->Load();
// 判断当前所属性插件是否启用
if (!$zbp->CheckPlugin('demoPlugin')) {
  $zbp->ShowError(48);
  die();
}
// 根据功能可能需要鉴权，本示例为任何人知道地址就能访问并查看本页的运行结果
// http://127.0.0.1/zb_users/plugin/demoPlugin/api.php

// 取最新 10 篇文章
$articles = GetList(10);
$pagebar = new Pagebar($zbp->option['ZC_INDEX_REGEX'], true, true);
// 要应用主题模板必须指定pagebar标签，省略了很多属性值，所以结果会是第0页
$zbp->template->SetTags('articles', $articles);
$zbp->template->SetTags('pagebar', $pagebar);
$zbp->template->SetTemplate('index');
$zbp->template->Display();

```

<!--2922-->
