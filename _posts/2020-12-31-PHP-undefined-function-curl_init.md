---
title: 【PHP 笔记】Call to undefined function curl_init()
tags:
- PHP,笔记,折腾
categories:
- 电脑网络
id: 331
alias: 20201231275
---

### 一

本地环境用的 EasyPHP。

官网：[https://www.easyphp.org/](https://www.easyphp.org/ "EasyPHP - Code with Devserver & host with Webserver")

之前的评价：[总觉得 phpstudy 的“国产”属性太浓烈……](https://www.wdssmq.com/post/20200325228.html "总觉得phpstudy的“国产”属性太浓烈……")

### 二

然后重点是我再一次需要用 Z-Blog 的网络类实现一个功能。

```php
$url = "https://demo.wdssmq.com/";
$http = Network::Create();
$http->open('GET', $url);
// $http->setTimeOuts(10, 10, 0, 0);
$http->send();
if ($http->status == 200) {
  $zbp->SetHint("good", "成功");
} else {
  $zbp->SetHint("bad", "失败");
}
$html = $http->responseText;
```

`$http->status`直接是 0，，然而我换成`https://www.baidu.com/`又能拿到内容，，之前好像也遇到过最后放弃了（已经忘记当时是想弄什么功能了。。）

这次插件主题都写好了，就差这最后一环了，通过比照「应用中心客户端」插件，最后发现环境里并没有「curl」。。【虽然还是不懂为什么百度和应用中心在没有的情况下仍然能访问到。。

### 三

php.ini 中已经启用 curl，但是仍然不行。

```ini
extension=php_curl.dll
```

最后实际成功的方案是，复制下边几个文件到`apache\bin`路径下；

`libeay32.dll|ssleay32.dll|libssh2.dl|php_curl.dll`

使用「Everything」的「在文件夹内搜索」功能在「php 的文件夹内」找到上述文件后复制（需要开启正则模式）。

好像有几个提示已经存在的，我选了跳过。。实际好像也是可以的。。

### 四

有说复制到`C:\Windows\System32`下的，实测无效。

windows 下 php Call to undefined function curl\_init() - A 灵云 A 的个人页面 - OSCHINA - 中文开源技术交流社区：[https://my.oschina.net/AlingyunA/blog/1860034](https://my.oschina.net/AlingyunA/blog/1860034 "windows下php Call to undefined function curl\_init() - A灵云A的个人页面 - OSCHINA - 中文开源技术交流社区")

<!--331-->
