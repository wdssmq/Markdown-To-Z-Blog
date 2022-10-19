---
title: 【折腾】独立博客之「熵」
date: 2021-02-27 14:19:05
tags:
- md2zb
- 折腾
- 独立博客
- 写作
categories:
- 杂七杂八
id: 3116
alias: 20210227485
csdn: https://blog.csdn.net/qq_15022221/article/details/114182024
zhihu: https://zhuanlan.zhihu.com/p/353377278
cnblogs: https://www.cnblogs.com/wdssmq/p/15193312.html
---

### 记不住的快捷键

按理我已经记住了不少快捷键了，，然而也仅限常用的那些；

- 任务视图：Win + Tab(松开键盘界面不会消失)
- 创建新的虚拟桌面：Win + Ctrl + D
- 关闭当前虚拟桌面：Win + Ctrl + F4
- 切换虚拟桌面：Win + Ctrl +左/右

<!--more-->
\----

只所以会提到快捷键，是因为写这篇时也是一边写一边完善各种写作的工具，所以分到不同桌面会比较好的感觉。。

比起因为在工具上投入的时间更多而产生的「本末倒置」，更感觉是因为折腾才有东西可写。。

\----

火狐、Chrome、Edge，先后几次尝试鼠标手势插件，最后同样放弃，后来发现了 Quicker 的轮盘功能，还买了会员，结果使用频度也不高 Orz；

姑且插播下广告：

Quicker 软件 您的指尖工具箱：[https://getquicker.net/](https://getquicker.net/ "Quicker软件 您的指尖工具箱 - Quicker")

推荐码：**105131-1635**

### 一始既往的离题开场

2021 年了，知乎上仍然时不时刷到各种尬吹 win7 比 win10 好用，好用又怎样，**win7 还不是已经停止更新了**；

然后，英文中「died」好像是完成时，「dying」虽然是进行时但是表意却是「垂死（还没死）」，所以为什么没有「dieding」这种表示「处于死亡的持续状态」的词；

而我脑洞过一个「dieding 百科」来记录这一类的事物；

### 既然偏题太远，那就修改标题

略微草率的把主站升级到了 1.7，而这篇预定是使用「[API 工具](https://github.com/wdssmq/Markdown-To-Z-Blog "wdssmq/Markdown-To-Z-Blog: 使用 GitHub Actions + Markdown 更新 Z-Blog 博客。")」发布的第一篇；

[使用 GitHub Actions + Markdown 更新 Z-Blog 博客\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20210224498.html "使用 GitHub Actions + Markdown 更新 Z-Blog 博客\_电脑网络\_沉冰浮水")

结果是和之前很多次一样，内容完全被「过程」影响了；

[【言说】停不下的写作和代码\_杂七杂八\_沉冰浮水](https://www.wdssmq.com/post/20210205073.html "【言说】停不下的写作和代码\_杂七杂八\_沉冰浮水")

### 「熵」从何来

最近好像经常使用`「」`，一个原因是今年开始着手写 Z-Blog 的新文档了，然后在更早之前忘记出于什么原因已经设置为了输入法短语，而且用的是`括号`一词的编码触发（搜狗五笔）；

Z-BlogPHP 官方文档：[https://docs.zblogcn.com/php/](https://docs.zblogcn.com/php/#/ "Z-BlogPHP 官方文档")

然后刚确认了下，在「百度百科」是在「引号」条目下的，而「钩括弧」是日语直译，嘛，，触发编码已经习惯了，就不改了；

就是不知道怎么设置自动定位光标到中间；

\----

「Z-Blog ASP 1.8」 → 「Z-Blog ASP 2.x」 → 「Z-Blog PHP 1.x」 → 「Z-Blog PHP 1.7」

所以这次升级 1.7 为什么就这么草率呢，明明当年放弃 ASP 的时候就纠结了很久；

「- -」

最早给「zbp 1.7」单独弄了个站演示和折腾，期间发布的文章也是打算要沿用到正式站内的，主站既然升级了那么后续工作也只能提前；

先是将新演示站和原来的`demo.wdssmq.com`进行合并，用的还是「[MovableType](https://www.wdssmq.com/post/20170502785.html "适用于Z-Blog的MovableType语法规范\_电脑网络\_沉冰浮水") 导入/导出」，这东西自己用的话还是有些方便的，然而操作后发现「Tag 标签」又又又出现了重复，是的，，第三次出现；

第一次是从 ASP 换到 PHP，原因是 MovableType 语法中 Tag 是一行一个输出，而当时的 Z-BlogPHP 并没能严格过滤空白（换行符）……

第二次是因为 Name 为数字的 Tag……

第三次则是因为「批量导入」数据时用到了缓存设计，终于暴露出了缓存的坑；平时发文章都是单独的请求，直接查数据库判断所以不会走缓存……

**今天是 2021-2-27，截止到本文发出前，主博客内「Tag 最大 ID」为`5593`；**

**话说，虽然现在知道「熵」读音同「商」，内心还是觉得应该读「狄」；**

### 结束

- 最后发到演示站一次；
- 将 Git 库创建一个分支留档；
- 修改鉴权信息到正式站然后发布；

「- -」

差一点弄错，果然 ID 不适合用来判断是否已经发布，不同站不一样；
