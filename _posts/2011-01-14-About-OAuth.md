---
title: 关于 API 和 OAuth 授权验证
date: 2011-01-14 13:30:21
tags:
- 微博
- API
- ASP
categories:
- 电脑网络
id: 686
alias: ZuoWanDeMengHaiZhenShiXuanYiJiaKeHuanTuCaoChuMei
---

2023-01-02：这篇文章是 2011 年的，然而 2023 年了仍然有网站在首次使用微信登录时直接给用户一个新账号，而不是问一下要不要绑定邮箱账号……

---------------

前两天有事去市里了，发现火狐便携版仍然那么杯具。。订阅什么的就没管，积了好多。。博客更新是回来后再补的，订阅的童鞋应该发现的。。

这几天有折腾腾讯微博的 API，(刚蓝屏一次，话说用 win7 快一年了，蓝屏不到 10 次，MS 还不错），SDK 什么的都没有 ASP 的，而吾辈偏偏就只会一点 ASP。。。只好自己试着搞定，经过多方 Google，终于明白点 oauth 是什么了，可是运行时总是失败。。。。。

----------------

修订：当年还是 OAuth 1.0，真心蛮折磨人的，2.0 后好了很多；

> 理解 OAuth 2.0 - 阮一峰的网络日志：
>
> [https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html](https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html "理解 OAuth 2.0 - 阮一峰的网络日志")

----------------

**下边内容可能也没啥价值了，姑且留着吧；**

API 通过以下四个步骤来完成认证授权并访问或修改受限资源的流程

1. 获取未授权的 Request Token(temporary credentials)
2. 请求用户授权 Request Token
3. 使用授权后的 Request Token 换取 Access Token(token credentials)
4. 使用 Access Token 访问或修改受保护资源

其中 1~3 步使用 https 方式， 第 4 步使用 http 方式。

我们注册并使用腾讯微博，帐号密码及所发布的信息都保存在腾讯微博的服务器上，但是可以通过 API 接口将数据拿到站外使用，所以第一步，应用方帮用户向腾讯服务器进行“预约”，同时也是对应用方资格的一个验证，二、三步对用户身份进行验证，“办理”将数据拿到站外使用的其他“手续”，最后就可以在应用方“访问或修改受保护资源”。

和 OpenID 挺像的，，只是 OpenID 应用中，对用户身份进行验证的一方只负责验证，不提供资源。

----------------

> 知识普及：什么是“OpenID”？\_电脑网络\_沉冰浮水：
>
> [https://www.wdssmq.com/post/20100519288.html](https://www.wdssmq.com/post/20100519288.html "知识普及：什么是“OpenID”？\_电脑网络\_沉冰浮水")

<!--686-->
