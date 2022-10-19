---
title: 「水坑」Z-BlogPHP 中各种错误提示的复现
date: 2021-09-18 21:13:24
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

> Array and string offset access syntax with curly braces is no longer supported

`offset access`直译是「偏移访问」，对应的中文概念是「（数组）下标」；

`syntax`是「语法」，比如`PHP`、`JavaScript`在表达普通字符串时单引号和双引号都可以，但是涉及「变量解析/模板字符串」时有各自的「规则语法」；

`curly braces`是「大括号」；

`no longer supported`——不再支持；

```php
// 正确
$arr = array(1,2,3);
echo $arr[0];
// die();

// 错误
$arr = array(1,2,3);
echo $arr{0}; // Array or string offset access with curly braces deprecated in PHP 7.4. Targeting PHP 8.1.0.
// die();
```

编辑器语法检测会提示：

「花括号」形式的「数组或字符串下标」已经在「PHP 7.4 中废弃（deprecated）」，然后「Targeting PHP 8.1.0」；

所以这个「Targeting」该怎么翻译。。我自己现在用的 7.4，实际花括号并没有报错，各种讨论中也是用 PHP 8 的会出现这个报错；

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

--------------

> Array to string conversion

```php
// 正确，输出前进行转换或额外处理
$arr = array(0, 1, 2);
echo implode(", ",$arr);
// die();

// 错误，直接以 string 输出
$arr = array(0, 1, 2);
echo $arr;
// var_dump("$arr"); // 另外一种错误姿势
// die();
```

参考：

php 提示 Array to string conversion 解决方案：`https://blog.csdn.net/zeroking_vip/article/details/87960319` 「CSDN 少数有用的内容」
