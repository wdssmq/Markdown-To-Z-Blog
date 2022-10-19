---
title: 「GM_脚本」qBittorrent 批量修改种子 tracker
date: 2021-08-31 23:20:11
tags:
- GM_脚本
- BT
- Tracker
- JavaScript
categories:
- 电脑网络
id: 2925
alias: 20191117777
---

> 结果 4.2.0 版起 qBittorrent 终于终于增加了这个功能。

<!--more-->

感觉「如何看懂别人写的前端」这个问题对于我仍然很难，不知道什么时候才能掌握更有效率的姿势，，，虽然这次遇到的主要问题是怎么在 qBit 的 WebUI 中搞弹出层来放自己要加的功能，本想弄个 layer 以后其他站点也能用，并不成功，姑且用自带的实现了。。。

qBittorrent 槽点真心蛮多，在 uTorrent 去广告授权到期后换过来后时不时的会想换回去。。。

关于批量替换 Tracker，这东西是有`Web API`的：

> Web API Documentation · qbittorrent/qBittorrent Wiki
> https://github.com/qbittorrent/qBittorrent/wiki/Web-API-Documentation

网上到是有一些工具教程，但是即使是走 API 的方案，用的也是浏览器环境以外的方法来进行 http 请求操作，鉴权都要单独考虑，到也不能说不理解，只是感叹一下——需求，能力，意愿，视角——果然人和人是不一样的吧。。。

----严格来说本文重点只有下边的部分----

[lock]

脚本发布地址：

> qBittorrent 管理脚本「QQ 群：189574683」
> [https://greasyfork.org/zh-CN/scripts/391688](https://greasyfork.org/zh-CN/scripts/391688 "qBittorrent 管理脚本「QQ 群：189574683」")

[/lock]

效果及默认应用的`网址:端口`见下图，非默认 url 的可自行添加“用户匹配”。

![脚本效果](https://www.wdssmq.com/zb_users/upload/2019/11/201911172126096447328.png "脚本效果")

> “硬核”技术第二弹：用「油猴子脚本」武装你的浏览器_电脑网络_沉冰浮水
> https://www.wdssmq.com/post/20180606584.html

<!--2925-->
