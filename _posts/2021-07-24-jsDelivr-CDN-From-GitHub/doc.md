---
title: 「GM_脚本」获取 GitHub 项目文件的 jsDelivr CDN 地址「好像没啥用系列」
tags:
- GM_脚本
- CDN
- GitHub
categories:
- 电脑网络
id: 3125
alias: 20210724854
---

基本信息：

> name：「 GitHub 」获取文件的 jsDelivr 地址
>
> desc：获取项目文件的 CDN 地址
>
> url： https://github.com/wdssmq/userscript/blob/master/Git/jsDelivr.user.js

可以直接通过这个链接安装：

> `https://cdn.jsdelivr.net/gh/wdssmq/userscript@master/Git/jsDelivr.user.js`

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
