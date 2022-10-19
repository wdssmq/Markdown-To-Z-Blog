---
title: 「水坑」略深入的讲解伪静态相关的知识
date: 2021-12-08 22:56:36
tags:
- GesF-Force
- Rewrite
- PHP
categories:
- 电脑网络
id: 837
alias: 20190704012
---

url 理论上指向的是一个文件，即使是目录也会按默认设置寻找 index.html 或 index.php，不存在时则由 web 环境返回 404。

但是对于 Z-BlogPHP 这样的动态站点，url 指向都是 index.php，然后由内部逻辑决定是否抛出 404；

<!--more-->

让 url 指向 index.php 的实现叫「URL Rewrite」，中文常对应为「伪静态」，虽然严格来说「伪静态」（Pseudo-static）只是「URL 重写」的应用之一；

Redirect 则是「重定向（301）」，虽然可以理解为带有 301 标志的 Rewrite（？）；

> 为什么叫「水坑」见：
>
> [「水坑」系列教程索引](/post/20200617652.html "「水坑」系列教程索引")

代码及讲解注释见下边 Git 链接；

每个链接对应一次「Git 提交」状态，也就是「版本控制」，你可以按顺序复制保存到你的 web 环境进行测试，比如`URL_Rewrite/index.php`；

大概理解后就换下一个「版本」覆盖进同一文件查看效果；

\---

纯动态模式 - php-rewrite/index.php · 70063e1 · 沉冰浮水/水水的旧代码合集 - Gitee.com

[https://gitee.com/wdssmq/StaleCode/blob/70063e12f67c31ba5588a2b2a0a0e3fe727ea37b/php-rewrite/index.php](https://gitee.com/wdssmq/StaleCode/blob/70063e12f67c31ba5588a2b2a0a0e3fe727ea37b/php-rewrite/index.php "php-rewrite/index.php · 沉冰浮水/水水的旧代码合集 - Gitee.com")

\---

> php-rewrite · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国：
>
> [https://gitee.com/wdssmq/StaleCode/tree/c04e9f96f4654f484510b93d7453ebf0f6c8b53f/php-rewrite](https://gitee.com/wdssmq/StaleCode/tree/c04e9f96f4654f484510b93d7453ebf0f6c8b53f/php-rewrite "php-rewrite · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")
>
> **↑ 这里可以查看效果截图（纯动态模式）**
>
> 会发现`/?id=1024`和`/post/2048.html`两种访问返回的「不存在」是不一样的，后者的 404 是由「web 程序」返回；

---

「- 现在已经 00:41:31 了，提交一下明天继续； -」

「- 补充了几句，拖到 00:46:31 了； -」

---

所以继续，前一步代码中已经定义了`$options["is_rewrite"]`作为伪静态的开关；

现在将该值改为`true`然后增加一些代码；

\---

针对性的伪静态 - php-rewrite/index.php · 6464486 · 沉冰浮水/水水的旧代码合集 - Gitee.com：

[https://gitee.com/wdssmq/StaleCode/blob/6464486539fdb4f53a9b834d2a2d444587f14fe8/php-rewrite/index.php](https://gitee.com/wdssmq/StaleCode/blob/6464486539fdb4f53a9b834d2a2d444587f14fe8/php-rewrite/index.php "php-rewrite/index.php · 沉冰浮水/水水的旧代码合集 - Gitee.com")

\---

上边网址是此版本内`index.php`文件的完整代码，可以通过右边链接查看此提交的「文件变更」信息[针对性的伪静态 - php-rewrite/index.php · 6464486 · 文件变更查看](https://gitee.com/wdssmq/StaleCode/commit/6464486539fdb4f53a9b834d2a2d444587f14fe8 "针对性的伪静态 - php-rewrite/index.php · 6464486 · 文件变更查看")

其中增加的 PHP 代码如下，本质概念是，在「网站程序」内「打开伪静态选项」然后根据选项「变更输出到网页的内容（主要是链接）」；

```php
// 伪静态开关切换
$options["is_rewrite"] = true;

// 文章 url 改为静态形式
if ($options["is_rewrite"]) {
  $post["url"] = $options["host"] . "post/3.html";
}
```

↑ 建议使用前边的「文件变更」链接查看，会发现除了`index.php`内容有修改外，还多了一份`.htaccess`；

而只有正确配置`.htaccess`才能完整实现需要的伪静态效果；

注：`.htaccess`为 Apache 的配置文件，IIS 和 Nginx 同样有各自的规则语法；

**总结：**

PHP 代码和文件属于「网站程序」；

IIS/Nginx/Apache 则可以称为「web 程序」，「web 程序」配合 PHP 或其他语言的解析引擎，再加上 MySQL 或其他数据库，构成「web 环境」；

开场提到的「URL Rewrite」则是「web 程序」所提供的功能；

通常意义上，对于 Z-BlogPHP 或其类似程序，「开启伪静态」需要：

- 程序本身支持；
- 开启相应选项开关；
- 正确配置「web 程序」对应的规则文件；

**其他需要了解的：**

- 启用伪静态后，`/?id=3`和`/post/3.html`均能打开，且访问到的内容是一样的，不是 Bug，（本文示例中）也不能让前者「重定向（301）」到后者，会出错；
- 启用伪静态后，`?id=1024`和`post/2048.html`均由 PHP 返回不存在信息；
- 由 PHP 输出 404 时，应该同时设置状态码：
    ```php
    if ($status == "404") {
      header("HTTP/1.1 404 Not Found");
      header("status: 404 Not Found");
    }
    ```
- 「重定向（301）」功能——「网站程序」和「web 程序」都能实现，对于有规律的，强烈建议由「web 程序」实现；
    - 好吧。。好像 301 和 302 都算「重定向」，只不过是永久和临时的区别；
    - 302 到是一般由「网站程序」自己使用；
- 在本文中只配置了「文章」的伪静态规则，实际程序中还会有「标签」「分类」「日期」等等，各自写 Rewrite 规则好像就比较繁琐了；
    - 所以一种选择就是，对于不存在实现文件的访问请求，全部交由 PHP 处理；
    - 见「[php-rewrite/.htaccess · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国](https://gitee.com/wdssmq/StaleCode/blob/master/php-rewrite/.htaccess "php-rewrite/.htaccess · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")」← `12 ~14`行注释掉的部分，也是 Z-BlogPHP 预置的规则形式；

「- 大概就这样吧，写完中午都过去了。 -」
