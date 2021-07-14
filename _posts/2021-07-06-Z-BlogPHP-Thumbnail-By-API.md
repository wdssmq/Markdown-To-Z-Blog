---
title: 【备忘】Z-BlogPHP 使用随机图片 API 设置缩略图
tags:
- 备忘
- 折腾
- Z-BlogPHP
categories:
- 电脑网络
id: 77
alias: 20100215532
---

### 简述

Z-BlogPHP 接入随机图 API 用于缩略图

<!--more-->

### 代码

```php
/**
 * 提取或者设置图片
 *
 * @param object $article
 * @param string $type   用于决定返回形式
 * @return string imgurl | <img />
 */
function demoAPP_Thumbnail($article, $type = 'imgurl')
{

  $matches = null;
  preg_match_all("/<img[^>]*src=\"([^\"]+)\"[^>]*>/i", $article->Content, $matches);
  if (isset($matches[1]) && count($matches[1]) > 0) {
    $imgurl = $matches[1][0];
  } else {
    $imgurl = demoAPP_setRndImg($article->ID);
    // $imgurl = demoAPP_setRndImgNetwork(); // 在当前需求下此种方式并不科学。可能会被服务方限制
  }
  // 默认返回图片地址
  if ($type == 'imgurl') {
    return $imgurl;
  }
  // 传入任意其他值可返回 <img /> 标签
  $tplImg = '<img src="imgurl" alt="title">';
  return strtr($tplImg, array('imgurl' => $imgurl, 'title' => $article->Title));
}

/**
 * 可直接引用的随机图接口
 *
 * @param string $rndhash 传入一个参数用于防止图片重复
 * @return string
 */
function demoAPP_setRndImg($rndhash)
{
  return "https://picsum.photos/350/260?random={$rndhash}";
}

/**
 * 接口本身返回 json ，需要额外提取图片地址
 *
 * @return string
 */
function demoAPP_setRndImgNetwork()
{
  global $zbp;
  // 失败时的默认图
  $imgurl = "{$zbp->host}zb_users/theme/demoAPP/var/images/no-image.jpg";
  // 接口地址
  $url = "https://api.vvhan.com/api/acgimg?type=json";
  $http = Network::Create();
  $http->open('GET', $url);
  // $http->setTimeOuts(10, 10, 0, 0);
  $http->send();
  // 对抓取内容进行解析
  if ($http->status == 200 && $json = json_decode($http->responseText, true)) {
    // 返回字段以实际接口为准
    $imgurl = $json['imgurl'];
  }
  return $imgurl;
}
```
模板内调用：

```html
<a href="{$article.Url}" title="{$article.Title}">
{demoAPP_Thumbnail($article,1)}
</a>
```

### 推荐

关于 Z-BlogPHP 1.7 缩略图的一些记录\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20210224481.html](https://www.wdssmq.com/post/20210224481.html "关于 Z-BlogPHP 1.7 缩略图的一些记录\_电脑网络\_沉冰浮水")

\[开发者\]正则表达式相关专贴-开发者中心-ZBlogger 技术交流中心：

[https://bbs.zblogcn.com/thread-101713.html](https://bbs.zblogcn.com/thread-101713.html "\[开发者\]正则表达式相关专贴-开发者中心-ZBlogger技术交流中心")
