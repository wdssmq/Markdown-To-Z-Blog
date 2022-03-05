---
title: 「水坑」Z-BlogPHP 中各种错误提示的复现
tags:
- GesF-Force
- 折腾
- 教程
categories:
- 电脑网络
id: 589
alias: 20200922437
---

严格来说并不都是 Z-BlogPHP 独有的错误；

另外这里标题是「复现」，以最简单的例子演示为什么会出现这种错误，至于初学者能否看懂以及能否帮助解决实际的问题。。emmm

> 包月 59.3 看心情解答各种问题。。zblog 为主。。

<!--more-->

HelloZBlog「插件开发演示」 - Z-Blog 应用中心：

[https://app.zblogcn.com/?id=18072](https://app.zblogcn.com/?id=18072 "HelloZBlog「插件开发演示」 - Z-Blog 应用中心")

`zb_users\plugin\HelloZBlog\include.php` 中有一个`HelloZBlog_debug()`函数，在该函数内可以测试复现下边各种错误；


--------------

> Trying to access array offset on value of type null

```php
// 正确
$var = array(0);
echo $var[0];
// die();

// 报错
$var = null;
echo $var[0];
// die();
```

--------------

> Function name must be a string

```php
// 正确
$var = "fnTest"; // 前提是 fnTest() 函数存在
echo $var();
// die();

// 报错
$var = 1024;
echo $var();
// die();
```

--------------

> Call to undefined function fnTest()

对于上边`$var = "fnTest";`的示例能够正确执行，需要定义：

```php
function fnTest()
{
  return "test";
}
```

--------------

> Call to a member function fnTest() on bool

```php
$obj = true;
$obj->fnTest();
// die();
```
