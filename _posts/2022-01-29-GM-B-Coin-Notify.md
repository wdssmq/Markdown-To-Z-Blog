---
title: 「GM 脚本」大会员 B 币领取提醒
tags:
- GM_脚本
- JavaScript
- 哔哩哔哩
- 折腾
categories:
- 电脑网络
id: 2456
alias: 20141219446
---

**大部分脚本都以自用优先，所以可能塞了奇怪的功能进去，建议摘取需要的部分自行组织完整代码；**

<!--more-->

> name：「bilibili」- 稍后再看导出为.url

> desc：将 B 站的稍后再看列表导出为.url 文件

> url：https://github.com/wdssmq/userscript/blob/master/bilibili/later.user.js

> cdn：https://cdn.jsdelivr.net/gh/wdssmq/userscript@master/bilibili/later.user.js

以及，现在才知道 localStorage 并不能跨子域使用，所以用了 cookie，其实好像用`GM_setValue`+`GM_getValue`也可以；

**相关推荐**

[「折腾」GM\_脚本修改 bilibili 番剧链接为我的追番\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100222433.html "「折腾」GM\_脚本修改 bilibili 番剧链接为我的追番\_电脑网络\_沉冰浮水")

[「折腾」使用 rollup.js 模块化编写 GM 脚本\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20120627834.html "「折腾」使用 rollup.js 模块化编写 GM 脚本\_电脑网络\_沉冰浮水")

-----

已改用`rollup.js`构建脚本，具体见上方推荐；

「B 币领取提醒」部分的 Git 查看：[https://github.com/wdssmq/userscript/blob/master/bilibili/src/_bcoin.js](https://github.com/wdssmq/userscript/blob/master/bilibili/src/_bcoin.js "userscript/\_bcoin.js at master · wdssmq/userscript")

以下仅为参考，并不能直接使用：

```js
// @grant        GM_notification
// @grant        GM.openInTab

// ==/UserScript==
/* jshint esversion:6 */
import { curUrl, curDate, _log, $n, fnElChange } from './_base.js';

// cookie 封装
const ckeObj = {
  setItem: function (key, value) {
    const Days = 137;
    const exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = key + "=" + encodeURIComponent(value) + ";path=/;domain=.bilibili.com;expires=" + exp.toGMTString();
  },
  getItem: function (key, def = "") {
    const reg = new RegExp("(^| )" + key + "=([^;]*)(;|$)");
    const arr = document.cookie.match(reg);
    if (arr) {
      return decodeURIComponent(arr[2]);
    }
    return def;
  }
};

// 日期转字符串
const getDateStr = (date) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return date.toLocaleDateString("zh-CN", options);
}

// 判断日期间隔
const diffDateDays = (date1, date2) => {
  const diff = date1.getTime() - date2.getTime();
  return diff / (1000 * 60 * 60 * 24);
}

// B 币领取提醒
(() => {
  const ckeName = "bilibili-helper-bcoin-nxtDateStr";
  const curDateStr = getDateStr(curDate);
  const nxtDateStr = ckeObj.getItem(ckeName, curDateStr);
  const bcoinUrl = "https://account.bilibili.com/account/big/myPackage";

  _log(`当前日期: ${curDateStr}`);
  _log(`下次领取: ${nxtDateStr}`);

  // 通知事件封装
  const notify = (title, body) => {
    _log(`通知标题: ${title}`);
    GM_notification({
      title: title,
      text: body,
      timeout: 0,
      onclick: () => {
        // window.location.href = bcoinUrl;
        GM.openInTab(bcoinUrl, false);
      }
    });
  }

  // 判断是否已经领取过
  const fnCheckByDOM = () => {
    const $bcoin = $n(".bcoin-wrapper");
    // _log("fnCheckByDOM", $bcoin);
    // $bcoin && _log("fnCheckByDOM", $bcoin.innerHTML);
    if ($bcoin && $bcoin.innerText.includes("本次已领")) {
      const match = $bcoin.innerText.match(/\d{4}\/\d+\/\d+/);
      if (match && match[0] !== nxtDateStr) {
        ckeObj.setItem(ckeName, match[0]);
        _log("已领取过，更新下次领取日期", match[0]);
        return true;
      }
    } else {
      fnElChange($n("#app"), fnCheckByDOM);
    }
    return false;
  }

  // _log($n("body").innerHTML);
  // _log(nxtDateStr, curMonth);

  // 对比日期
  const iniDiff = diffDateDays(curDate, new Date(nxtDateStr));
  if (iniDiff > 0) {
    _log(curUrl, "\n", bcoinUrl);
    if (curUrl.indexOf(bcoinUrl) > -1) {
      fnCheckByDOM();
    } else {
      notify("B 币领取提醒", "点击查看 B 币领取情况");
    }
  }
})();
```
