---
title: 「水坑」Z-BlogPHP 接口本质之「PHP 可变函数」
date: 2022-09-22 12:28:31
tags:
- GesF-Force
- Z-BlogPHP
- PHP
categories:
- 电脑网络
id: 787
alias: 20220409155
---

### 一

> 严格来说，全部接口都是「监听」，监听接口本身被触发，然后执行指定的操作，或者对接口传递的数据进行处理。

<!--more-->

上边是写在 Z-BlogPHP 文档里关于插件接口部分的总结：[Z-BlogPHP 官方文档](https://docs.zblogcn.com/php/#/ "Z-BlogPHP 官方文档")；

更进一步，接口机制本质上是 PHP 中「可变函数」的一种应用，将「指定的操作」定义为函数，然后以「可变函数」的方式来调用；

然后 PHP 还有一个 「可变变量」的概念，则是 Z-BlogPHP 模板机制的基础；

> 「水坑」Z-BlogPHP 模板机制讲解「简易版」\_电脑网络\_沉冰浮水：
>
> [https://www.wdssmq.com/post/20201026266.html](https://www.wdssmq.com/post/20201026266.html "「水坑」Z-BlogPHP 模板机制讲解「简易版」\_电脑网络\_沉冰浮水")

对这些基础性质进行封装使用才构成了 Z-BlogPHP 或者其他的 PHP 程序，所以很多时候你需要的是看 PHP 的文档，而不是嫌 Z-BlogPHP 的文档不够详细；

### 二

关于「可变函数」的示意代码；

```php
function fnTest1()
{
    # code...
}
function fnTest2()
{
    # code...
}
function fnTest3()
{
    # code...
}

// 根据 $func 的值来调用不同的函数
$func = "Test1";

// -----------
// 1. 普通的 if else 判断
if ($func === "Test1") {
    fnTest1();
} elseif ($func === "Test2") {
    fnTest2();
} elseif ($func === "Test3") {
    fnTest3();
}

// -----------
// 2. 使用 switch case
switch ($func) {
    case 'Test1':
        fnTest1();
        break;
    case 'Test2':
        fnTest2();
        break;
    case 'Test3':
        fnTest3();
        break;
    default:
        # code...
        break;
}

// -----------
// 3. 使用 call_user_func
call_user_func("fn$func");
// call_user_func 我没怎么用过，但是字面上还是好理解的；
// 因为 AI 提示才写在这里的，不过 AI 还告诉我有个 call_user_func_array，就需要再查下怎么用和有啥用了；
// 然后关于 copilot 有张附图可以见下边 B 站动态链接里；

// -----------
// 4. 使用可变函数
$func = "fn$func";
$func();
```

### 三

> PHP: 可变函数 - Manual：
>
> [https://www.php.net/manual/zh/functions.variable-functions.php](https://www.php.net/manual/zh/functions.variable-functions.php "PHP: 可变函数 - Manual")

> PHP: 可变变量 - Manual：
>
> [https://www.php.net/manual/zh/language.variables.variable.php](https://www.php.net/manual/zh/language.variables.variable.php "PHP: 可变变量 - Manual")


> 关于 copilot 的附图 - 沉冰浮水的动态：
>
> [https://t.bilibili.com/708592243066273862](https://t.bilibili.com/708592243066273862 "关于 copilot 的附图 - 沉冰浮水的动态")
