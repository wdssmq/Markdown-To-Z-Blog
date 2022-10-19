---
title: 「GM_脚本」获取 GitHub 项目文件的 jsDelivr CDN 地址「好像没啥用系列」
date: 2021-07-24 17:51:08
tags:
- GM_脚本
- CDN
- GitHub
categories:
- 电脑网络
id: 3125
alias: 20210724854
csdn: https://blog.csdn.net/qq_15022221/article/details/119062390
zhihu: https://zhuanlan.zhihu.com/p/392810766
jianshu: https://www.jianshu.com/p/823c80a6f16f
cnblogs: https://www.cnblogs.com/wdssmq/p/15056067.html
---

使用 jsDelivr 可以反代存放于 GitHub Repo 内的文件，所以写了个脚本实现自动转换链接；

<!-- more -->

基本信息：

> name：「GitHub」获取文件的 jsDelivr 地址
>
> desc：获取项目文件的 CDN 地址
>
> url：https://github.com/wdssmq/userscript/blob/master/Git/jsDelivr.user.js
>
> cdn：https://cdn.jsdelivr.net/gh/wdssmq/userscript@master/Git/jsDelivr.user.js

重要 · 需要配合下边浏览器扩展使用：

> https://github.com/EnixCoda/Gitako

↓ 效果如下图

![001.png](https://i.loli.net/2021/07/24/7UFivqolMYOpyxw.png)

```js
function fnGetCDNUrl(url) {
  const arrMap = [
    ["https://github.com/", "https://cdn.jsdelivr.net/gh/"],
    ["/blob/", "@"]
  ]
  let cdnUrl = url;
  arrMap.forEach(line => {
    cdnUrl = cdnUrl.replace(line[0], line[1]);
  });
  return cdnUrl;
}
```
