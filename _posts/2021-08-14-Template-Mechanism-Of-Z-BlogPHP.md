---
title: 「水坑」Z-BlogPHP 模板机制讲解「简易版」
date: 2021-08-14 18:33:04
tags:
- GesF-Force
- Z-BlogPHP
- PHP
categories:
- 电脑网络
id: 2423
alias: 20201026266
---

### 例行中二时间

好像确实会不少东西，然而日常不知道有什么意义；

<!--more-->

### 推荐阅读

Z-BlogPHP 模板语法汇总：

[https://docs.zblogcn.com/php/markup/](https://docs.zblogcn.com/php/markup/ "Z-BlogPHP 模板语法汇总")

「小目标」平均每篇文章/Git Repository 赚取 1 元\_杂七杂八\_沉冰浮水：

[https://www.wdssmq.com/post/20210723266.html](https://www.wdssmq.com/post/20210723266.html "「小目标」平均每篇文章/Git Repository 赚取 1 元\_杂七杂八\_沉冰浮水")

> 为什么叫「水坑」见：
>
> [「水坑」系列教程索引](/post/20200617652.html "「水坑」系列教程索引")

### PHP 可变变量（动态变量）

```php
// 零 - index.php
echo "<h3>零</h3>";
$animal = 'turtles';
$turtles = 103;
print $$animal;
// 此处输出效果同：
// print $turtles
```

利用该语法可以将视图层（View）独立出来，既实现「模板机制」；

参考：
「[PHP: 可变变量 - php.net](https://www.php.net/manual/zh/language.variables.variable.php "PHP: 可变变量 - Manual")」
「[MVC 框架\_百度百科](https://baike.baidu.com/item/MVC%E6%A1%86%E6%9E%B6/9241230 "MVC 框架\_百度百科")」
；

### 正文

**注：注释中`- index.php`部分表示该代码应该放在哪个文件里；**

```php
// 用于展示的数据 - index.php
$tags = array(
  "blog" => "https://www.wdssmq.com",
  "name" => "沉冰浮水",
  "afdian" => "https://afdian.net/@wdssmq"
);
```

将上边数组的每一项输出为一个段落；

```php
// 一 - index.php
echo "<h3>一</h3>";
foreach ($tags as $key => $value) {
  echo "<p>{$key}：{$value}</p>";
}

// 二 - index.php
echo "<h3>二</h3>";
foreach ($tags as $key => $value) {
  $$key = $value;
}
echo "<p>name：{$name}</p>";
echo "<p>blog：{$blog}</p>";
echo "<p>afdian：{$afdian}</p>";
```

方法「一」是比较基本的循环用法，输出顺序和变量赋值时的元素顺序一致；

方法「二」则使用「可变变量」语法为数组中的每个元素创建了一个单独的变量，变量名为各数组元素的键名（字段名）；

然后在输出时调整了顺序，从而不需要关心原始定义；

```php
// 三 - index.php
echo "<h3>三</h3>";
foreach ($tags as $key => $value) {
  $$key = $value;
}
include "user-info-3.php";
```

继续在「index.php」中添加如上代码，然后在同一级目录内，创建「user-info-3.php」并添加如下代码；

```php
<?php
// 3 - user-info-3.php
echo "<p>name：{$name}</p>";
echo "<p>blog：{$blog}</p>";
echo "<p>afdian：{$afdian}</p>";
```

继续改进：

```php
// 四 - index.php
echo "<h3>四</h3>";
foreach ($tags as $key => $value) {
  $$key = $value;
}
include "user-info-4.php";
```

注意，上边全部写入「index.php」或「user-info-3.php」的代码都是在`<?php`内的；

> 小知识：对于 PHP 语法记`<?php ?>`，在不需要中途闭合以插入 HTML 时，用于结束的`?>`是可以省略的；

下边用于「user-info-4.php」文件的代码，是直接以 HTML 为主体的，仅在变量输出部分使用 PHP 语法；

```php
<!-- 4 - user-info-4.php -->
<p>name：<?php echo $name; ?></p>
<p>blog：<?php echo $blog; ?></p>
<p>afdian：<?php echo $afdian; ?></p>
```

某种意义上，「`// 用于展示的数据 - index.php`」「`// 四 - index.php`」「`<!-- 4 - user-info-4.php -->`」三处注释所指代的代码组成及机制就是一个简单的模板语法实现；

然而在 HTML 中插入 PHP 语法仍然不是很方便，而且实际上，「`<!-- 4 - user-info-4.php -->`」部分的代码是由如下代码转换而来：

```html
 <!-- 4 - user-info-4.php -->
<p>name：{$name}</p>
<p>blog：{$blog}</p>
<p>afdian：{$afdian}</p>
```

↑ 而这也是 Z-BlogPHP 所采用的「模板标签」语法；

参考：
「[主题开发 - Z-BlogPHP 文档](https://docs.zblogcn.com/php/#/books/dev-app-theme "主题开发 - Z-BlogPHP 文档")」
「[模板标签 - 主题开发 - Z-BlogPHP 文档](https://docs.zblogcn.com/php/#/books/dev-app-theme?id=%e6%a8%a1%e6%9d%bf%e6%a0%87%e7%ad%be "模板标签 - 主题开发 - Z-BlogPHP 文档")」
；

<!-- Template-Mechanism-Of-Z-BlogPHP -->

### 附件下载

> 链接: [https://pan.baidu.com/s/19wH0sg5mXnY50Gue4ordlw](https://pan.baidu.com/s/19wH0sg5mXnY50Gue4ordlw "度盘分享")
>
提取码: 4gaa
>
> 内含两个压缩包，一个是本页教程直接涉及的代码（未加密），另一个则包含凝练提取的 Z-BlogPHP `Template` 类及注解（加密）；

密码获取方案如下：

「- -」「- -」「- -」

「折腾」Z-BlogPHP 模板机制讲解丨沉冰浮水丨爱发电：

[https://afdian.net/p/5e8460cefdbc11eb80a152540025c377](https://afdian.net/p/5e8460cefdbc11eb80a152540025c377 "「折腾」Z-BlogPHP 模板机制讲解丨沉冰浮水丨爱发电")

↑ 自选金额大概也可以解锁吧；

「- -」「- -」「- -」

关注微信公众号：「水水不想说」；

发送口令。。不，其实什么也不用发，甚至这个公众号也不需要关注，这里并没有密码；

「- -」「- -」「- -」

使用 RSS 订阅本博客；

\[ShortSth:RSS\]\[/ShortSth\]

密码被拆成了两部分，格式为「`php-tpl-xxxx`」，总长度 8 位——「`1\*\*\*\*e\*\*\*\*`」；

[「言说」RSS 是一种态度！！\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20201231613.html "「言说」RSS 是一种态度！！\_杂七杂八\_沉冰浮水")

[「年度套路」水水名下 Z-Blog 应用打包赠送\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20120926864.html "「年度套路」水水名下 Z-Blog 应用打包赠送\_杂七杂八\_沉冰浮水")
