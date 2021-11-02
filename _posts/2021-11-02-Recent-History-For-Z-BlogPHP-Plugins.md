---
title: 「Z-BlogPHP」插件管理添加「最近使用」功能
tags:
- Z-BlogPHP
- 插件
- JavaScript
categories:
- 电脑网络
id: 109
alias: 2010022472
---

不管线上还是本地开发，插件管理里经常找不到刚安装或最近操作过的某个应用，也是鸽了略久搞出了「最近使用」功能：

<!--more-->

功能一如既往的塞进了某个已有插件里：

> 后台二级菜单 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=1212](https://app.zblogcn.com/?id=1212 "后台二级菜单 - Z-Blog 应用中心")

插件免费，链接内也有截图效果；

「- -」「- -」「- -」

下边是部分代码，感觉可以在其他项目利用；

想说`GitHub Copilot`还是有点儿好用的。

```js
  // localStorage 封装
  const lsObj = {
    setItem: function (key, value) {
      localStorage.setItem(key, JSON.stringify(value));
    },
    getItem: function (key, def = "") {
      const item = localStorage.getItem(key);
      if (item) {
        return JSON.parse(item);
      }
      return def;
    },
  };

  const gob = {
    // 永远从当前页面读取的完整列表；
    curPlugList: null,
    // 上一次保存的完整列表，和 cur 对比不同 —— 新安装或启用状态改变 —— 压入 his；
    lstPlugList: null,
    // 此处记录内容即为「最近使用」或者说「最近活动」的项目，main.php 点击时也会记录并压入此数组；
    hisPlugList: null,
    lsKey: {
      lst: "lstPlugList",
      his: "hisPlugList",
    },
    load: function (lstDef, hisDef) {
      this.lstPlugList = lsObj.getItem(this.lsKey.lst, lstDef);
      this.hisPlugList = lsObj.getItem(this.lsKey.his, hisDef);
    },
    save: function () {
      lsObj.setItem(this.lsKey.lst, this.lstPlugList);
      lsObj.setItem(this.lsKey.his, this.hisPlugList);
    },
  };
```
