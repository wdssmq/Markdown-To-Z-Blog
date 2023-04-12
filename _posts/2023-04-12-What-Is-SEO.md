---
title: 所以就不是很懂 SEO
date: 2023-04-12 14:37:01
tags:
 - SEO
 - 杂七杂八
categories:
 - 杂七杂八
id: 283
alias: 20100609752
xlog: https://xlog.wdssmq.com/2023-04-12-What-Is-SEO
csdn: https://blog.csdn.net/qq_15022221/article/details/130109705
cnblogs: https://www.cnblogs.com/wdssmq/p/17310169.html
geeknote: https://geeknote.net/wdssmq/posts/2280
---

「[SEO](https://www.wdssmq.com/tag/SEO/ "SEO")」 这个 TAG 下以前有没有发过文章甚至都不记得了，至少现在本篇是第一篇……

<!--more-->

我的 web 工具箱里有这个：

> LMSTFY - 让我帮你搜索一下 - 水水的演示站：
>
> [https://demo.wdssmq.com/tools/LMSTFY/](https://demo.wdssmq.com/tools/LMSTFY/ "LMSTFY - 让我帮你搜索一下 - 水水的演示站")

但是有时的有时，一些问题是没有明确答案的，比如：

- 「`browser-sync`的命令行参数能否排除多个路径？」
- 「在导入 json 文件时 eslint 报错：`Parsing error: Unexpected token assert`」

前者我实际看过源码发现并不支持，自己魔改了下用，哪天试下给官方 PR 下看能不能过；

后者有个比较绕路的解决方案，就不是很优雅……

还有一些对我自己构不上困扰但也确实搜索不到现成的答案的问题，然而怎么说呢。。。

「一两句话就能说清的答案，想让别人能搜索到就略艰难……」


------

今天帮人解决的问题是这个：

> Call to undefined function SplitAndGet()

答案：

> 这个函数是 Z-BlogPHP 自身的，如果出现该问题需要下载一份新版 zb_system/ 覆盖进站点内……

然后让 AI 扩写一下：

> 该错误信息 "Call to undefined function SplitAndGet()" 意味着在您的代码中有一个调用了一个名为 SplitAndGet() 的函数，但这个函数并不存在。这通常意味着您可能没有正确地包含或加载所需的文件，或者必须安装某些插件或扩展程序。
>
> 在这种情况下，根据您提供的信息，SplitAndGet() 函数是 Z-BlogPHP 自身的一个函数。如果您在使用 Z-BlogPHP 并且出现此问题，那么最可能的原因是您的系统缺少某些必要的文件或资源。因此，您需要下载一份最新的 Z-BlogPHP 并将其中的 zb_system/ 目录覆盖到您的站点中，以确保所有必要的文件都被正确地加载和使用。
>
> 总之，如果您遇到这样的错误，请检查您的代码或系统是否缺少必要的文件或资源，并尝试更新或重新安装相应的软件。


------

其实昨天还遇到个字幕编辑软件 SubtitleEdit 的问题，该软件播放视频依赖 mpv，但是直接自动下载很慢。。

官方有一个 `SubtitleEdit/support-files` 仓库提供了 mpv 下载，可以将解压后的 `mpv-2.dll` 放到 `%AppData%\Subtitle Edit`  目录下（对于安装版）；


------

然后就突然想到了可以这么理解 SEO：

我：

> 「食指扎了刺怎么拔」，把这个句式套进每个手指，包括左右手

AI：

> 好的，以下是每个手指的对应句式：
>
> - 食指扎了刺怎么拔？
> - 中指扎了刺怎么拔？
> - 无名指扎了刺怎么拔？
> - 小指扎了刺怎么拔？
> - 大拇指扎了刺怎么拔？
>
> 针对以上问题的回答如下：
>
> 首先，如果手指上有刺，我们应该先用消毒酒精或者肥皂清洗伤口，避免感染。然后，可以用一根干净的针头或者镊子来尝试把刺拔出来。在操作过程中需要小心，避免进一步损伤伤口，同时也要确保工具是干净的，以避免感染。
>
> 如果自己无法成功拔出刺，或者伤口感染严重，建议及时就医，由专业医生进行处理。
