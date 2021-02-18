---
title: Chrome 再次试图隐藏地址栏中的`www`部分
tags:
- 浏览器,Chrome,谷歌,软件工具
categories:
- 电脑网络
id: 2851
alias: 20180905434
---

**注：本文发布于 2018 年 9 月，之后版本取消了本文所提及的改动，然后本人也已经改用 Edge；**

<!--more-->

不知道什么时候起，，浏览器的地址栏会默认隐藏掉网址前的`http://`协议，而绿锁版的`https://`则会保持显示。

一直以来，虽然是网址的重要组成部分，我们却很少需要主动关注协议名。

手动输入时我们很少特意键入它，因为浏览器会自动补全；人力输入不可及的地方我们会使用复制粘贴或者书签，至于里边有没有带协议我们其实也无所谓，，只不过大部分时候自动带着罢了 。

然而协议名之后紧跟的部分，最常体现为并被称作域名的部分，比如：www.bilibili.com ，www.zhihu.com ，www.baidu.com

上边三个域名的共同点，甚至整个互联网上相当一部分域名的共同点是，带上`www.`和不带时在浏览器里访问的效果是一样的。

对于复制粘贴的场景来说，多四个字符，少四个字符同样是无所谓的。然而这部分被手动输入的次数，和前边存在感极底的协议名相比的话，可以想像一下其数量级上的差异。。嗯。

![输入法](https://i.loli.net/2018/09/05/5b8f64641f72b.png)
<!-- ![001](https://i.loli.net/2021/02/06/HdwYocCEuseq9RM.png "001") -->

![输入法](https://i.loli.net/2018/09/05/5b8f3d652d3a0.png)
<!-- ![002](https://i.loli.net/2021/02/06/bn1WY8DsMVjqk3m.png "002") -->

因为长久以来的习惯，www 子域和其根域被捆绑使用了，虽然平摊到每个人身上根本算不上有什么困扰或影响，虽然我每次在建立站点文件夹和数据库时都会在微妙的挣扎后选择用 www 子域来命名……

谷歌的“态度”？或者根本没有态度——

不管出于何种目的，想法或者考虑，总之 Google Chrome 69 在这个好像“保持原样就可以吧”的地方投入了其关注和行动。

↓火狐↓
![火狐](https://i.loli.net/2018/09/05/5b8f36be0aabf.png)
<!-- ![003](https://i.loli.net/2021/02/06/3dIp5lcrKw4NFCf.png "003") -->
↓谷歌↓
![Chrome](https://i.loli.net/2018/09/05/5b8f370e8f44e.png)
<!-- ![004](https://i.loli.net/2021/02/06/hev8KTi51tqxoOw.png "004") -->

在新版 Chrome 浏览器中，，不仅协议名，www 子域的部分也被默认隐藏了。。

完全有理由说这只是整个版本更新中占比很小的改动和变化，虽然更容易被直接看到，虽然直接导致了我写出这篇文章，虽然在可预想的后续使用上反而会造成麻烦（301 重定向的效果确认什么的）。

虽然我自己附加的视角其实已经完全和软件技术、体验什么的无关了。。。。。。。。

------

如何评价新版 Chrome 默认隐藏域名中的 www.？ - 知乎

https://www.zhihu.com/question/293426033

统一资源定位符 - 维基百科，自由的百科全书

https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E5%AE%9A%E4%BD%8D%E7%AC%A6

URL 和 URI 有什么不同? - 知乎

https://www.zhihu.com/question/19557151

<!--2851-->