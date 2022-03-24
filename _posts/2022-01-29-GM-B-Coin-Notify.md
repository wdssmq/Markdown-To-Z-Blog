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

-----

大会员 B 币领取提醒核心代码：

```js
// @grant        GM_notification
// @grant        GM.openInTab

// ==/UserScript==
/* jshint esversion:6 */
(function () {
  "use strict";
  // 基础函数或变量
  const curUrl = window.location.href;
  const curDate = new Date();
  const $ = window.$ || unsafeWindow.$;
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const _log = (...args) => console.log('[bilibili-helper]', ...args);
  const _warn = (...args) => console.warn('[bilibili-helper]', ...args);
  const _error = (...args) => console.error('[bilibili-helper]', ...args);
  function $n(e) {
    return document.querySelector(e);
  }
  function $na(e) {
    return document.querySelectorAll(e);
  }

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
        return arr[2];
      }
      return def;
    }
  };

  // B 币领取提醒
  (() => {
    const ckeName = "bilibili-helper-bcoin-lstMonth";
    const curMonth = curDate.getMonth() + 1;
    const lstMonth = ckeObj.getItem(ckeName, 0);
    const bcoinUrl = "https://account.bilibili.com/account/big/myPackage";

    // 元素变化监听
    const fnElChange = (el, fn = () => { }) => {
      const observer = new MutationObserver((mutationRecord, mutationObserver) => {
        _log('body attributes changed!!!'); // body attributes changed!!!
        _log('mutationRecord = ', mutationRecord); // [MutationRecord]
        _log('mutationObserver === observer', mutationObserver === observer); // true
        fn(mutationRecord, mutationObserver);
        mutationObserver.disconnect();
      });
      observer.observe(el, {
        // attributes: false,
        // attributeFilter: ["class"],
        childList: true,
        // characterData: false,
        subtree: true,
      });
    }

    // 通知事件封装
    const fnNotify = (title, body) => {
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
      _log("---");
      // $bcoin && _log($bcoin.innerHTML);
      if ($bcoin && $bcoin.innerText.includes("本月已领")) {
        ckeObj.setItem(ckeName, curMonth);
        return true;
      } else {
        fnElChange($n("#app"), fnCheckByDOM);
      }
      return false;
    }

    // _log($n("body").innerHTML);
    // _log(lstMonth, curMonth);

    // 对比 cookie 数据
    if (lstMonth != curMonth) {
      _log(curUrl, bcoinUrl);
      if (curUrl.indexOf(bcoinUrl) > -1) {
        fnCheckByDOM();
      } else {
        fnNotify("B 币领取提醒", "点击查看 B 币领取情况");
      }
    }
  })();
})();
```
