---
title: 「GM_脚本」Feedly 标记已读辅助「小代码」
date: 2022-10-18 12:45:44
tags:
 - GM_脚本
 - 小代码
 - JavaScript
 - 折腾
categories:
 - 电脑网络
id: 44
alias: 20100605569
---

录演示视频逐渐熟练什么的，虽然还是好麻烦；

------

· 脚本命名：

- 「Feedly」Less Items

· 脚本简介：

- Feedly 分次标记已读

<!--more-->

· **脚本获取**：

- [https://greasyfork.org/zh-CN/scripts/453258](https://greasyfork.org/zh-CN/scripts/453258 "「Feedly」Less Items")
- [https://cdn.jsdelivr.net/gh/wdssmq/userscript@master/LessItems/LessItems.user.js](https://cdn.jsdelivr.net/gh/wdssmq/userscript@master/LessItems/LessItems.user.js "「Feedly」Less Items")

· 脚本应用站点：

- Feedly（`feedly.com`）

· 具体生效匹配：

- `https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2F*`
- ↑ 「单一订阅源」视图下；

· 功能需求：

- 处理 Feed 订阅时会希望尽可能通览每一条信息，查看或标记感兴趣的，剩下的标记已读；
- 然而 Feedly 自身设计并不是很好：
    - Today 视图下同一订阅源好像最多显示 6 个条目；
    - 标记已读后会加载下一页，条目总数略多时就蛮麻烦的；
    - 其他视图下只能全部标记已读，没有「将以上项目标记已读」之类的功能；

· 解决思路：

- 对应视图下，每次拉到底部会以 20 条为一组拉取新项目；
- 姑且在触发脚本时先自动拉取至多 n 组；「目前 n = 4，然后也不太需要配置的样子」
- 为每组创建一个按钮，点击按钮时自动标记已读；
  - 20 条其实还是太多，所以实际每个按钮最多可以点 4 次，每次标记 1/4；
  - 点击时自动滚动到对应区域，我的屏幕比较小，姑且一屏正好显示 5 条；
  - 虽然实际效果是「先标记已读 → 看有没有感觉兴趣的内容 → 再次点击」，能用就行.jpg；

· **效果演示**：

> 「GM\_脚本」「小代码」Feedly 标记已读辅助：
>
> [https://www.bilibili.com/video/BV1Tt4y1F79z](https://www.bilibili.com/video/BV1Tt4y1F79z "「GM\_脚本」「小代码」Feedly 标记已读辅助")

<iframe src="//player.bilibili.com/player.html?aid=986629921&bvid=BV1Tt4y1F79z&cid=864975347&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

· 投喂支持：

二维码：[https://github.com/wdssmq#二维码](https://github.com/wdssmq#二维码 "wdssmq#二维码")

爱发电：[https://afdian.net/a/wdssmq](https://afdian.net/a/wdssmq "沉冰浮水正在创作和 z-blog 相关或无关的各种有用或没用的代码 | 爱发电")

更多「小代码」：[https://cn.bing.com/search?q=小代码+沉冰浮水](https://cn.bing.com/search?q=%E5%B0%8F%E4%BB%A3%E7%A0%81+%E6%B2%89%E5%86%B0%E6%B5%AE%E6%B0%B4 "小代码 沉冰浮水 - 搜索")

