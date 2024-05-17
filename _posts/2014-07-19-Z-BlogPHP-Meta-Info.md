---
title: 「备忘」Z-BlogPHP 代码设置页面标题、关键词及描述
date: 2014-07-19 16:51:50
tags:
- 备忘
- 折腾
- PHP
categories:
- 电脑网络
id: 2312
alias: 20140719962
---

2023-11-02：

又是一篇超久远的文章重新修改，总有种 2014 年是不是还没有 PHP 版的错觉……

最早记录了用在第一个 PHP 主题的相关代码，后边主题中又不断修改，虽然总共没写过几个主题；

<!-- more -->

↓ 完整代码见下边链接

> mzERK/template/header.php · 沉冰浮水/ZBP\_THEME - 码云 - 开源中国
>
> [https://gitee.com/wdssmq/ZBP_THEME/blob/master/mzERK/template/header.php](https://gitee.com/wdssmq/ZBP_THEME/blob/master/mzERK/template/header.php "mzERK/template/header.php · 沉冰浮水/ZBP\_THEME - 码云 - 开源中国")

**重要：**

`<link rel="canonical" href="{$zbp.fullcurrenturl}">` 其实要配合接口使用，而且也并不合理，当时为什么要这样用……


```html
{if $type=='article'}
  <title>{$title}_{$article.Category.Name}_{$name}</title>
  {php}
    $keywords = $article->TagsToNameString();
    $description = preg_replace('/[\r\n\s]+/', ' ', trim(SubStrUTF8(TransferHTML($article->Content,'[nohtml]'),135)).'...');
  {/php}
  <meta name="keywords" content="{$keywords}">
  <meta name="description" content="{$description}">
  <meta name="author" content="{$article.Author.StaticName}">
  <link rel="canonical" href="{$article.Url}">
{elseif $type=='page'}
  <title>{$title}_{$name}_{$subname}</title>
  <meta name="keywords" content="{$title},{$name}">
  {php}
    $description = preg_replace('/[\r\n\s]+/', ' ', trim(SubStrUTF8(TransferHTML($article->Content,'[nohtml]'),135)).'...');
  {/php}
  <meta name="description" content="{$description}">
  <meta name="author" content="{$article.Author.StaticName}">
  <link rel="canonical" href="{$article.Url}">
{elseif $type=='index'}
  <title>{$name}{if $page>'1'}_第{$pagebar.PageNow}页{/if}_{$subname}</title>
  <meta name="keywords" content="{$zbp->Config('mzERK')->keywords},{$name}">
  <meta name="description" content="{$zbp->Config('mzERK')->description}_{$name}_{$title}">
  <meta name="author" content="{$zbp.members[1].Name}">
  <link rel="canonical" href="{$zbp.fullcurrenturl}">
{else}
  {php}
  $title = preg_replace('/\s.+$/','',$title);
  $fixTitle = "";
  $fixDesc = "";
  if (isset($pagebar)){
    $fixTitle = "_第{$pagebar->PageNow}页";
    $fixDesc = "_当前是第{$pagebar->PageNow}页";
  }
  {/php}
  <title>{$title}_{$name}{$fixTitle}</title>
  <meta name="keywords" content="{$title},{$name}">
  <meta name="description" content="{$title}_{$name}{$fixDesc}">
  <meta name="author" content="{$zbp.members[1].Name}">
  <link rel="canonical" href="{$zbp.fullcurrenturl}">
{/if}

```

第一个 PHP 主题：

> BootWord 响应式主题 - Z-Blog 应用中心
>
> [https://app.zblogcn.com/?id=428](https://app.zblogcn.com/?id=428 "BootWord响应式主题 - Z-Blog 应用中心")

<!--2312-->
