---
title: 「代码片段」两段略奇怪的 JS 代码
date: 2024-03-13 21:08:10
tags:
- 代码片段
- JavaScript
- 折腾
- 备忘
categories:
- 电脑网络
id: 2663
alias: 20160621482
---

> 2024-03-13：
>
> 又研究了一段不明所以的代码，然后想起来之前也搞过一段，就合并在一起了，然后发现当年那段迷惑程度要高不少。。

<!-- more -->

**数组中按间隔提取元素：**

```js
(() => {
    const allNum = 21;
    const perNum = 4;

    /**
     * @param {int} all  元素总数
     * @param {int} per 用于将 all 先分成 per 个一组
     * @param {int} offset 通过计算决定从第几个元素开始取，大于等于 0，上不设限
     * @returns {string} 返回一个字符串，每 per 个元素换行
     */
    function fnPickArr(all, per, offset = 0) {
        const rltArr = [];

        // const chunkNum = Math.floor(all / per);
        // ↑ floor 为向下取整，会出现取到 per + 1 个元素的情况
        const chunkNum = Math.ceil(all / per);
        // ↑ ceil 为向上取整，与 floor 相反，会出现取到 per - 1 个元素的情况

        // 本质上就是每隔 chunkNum - 1 个元素取一次，两次取余判断

        for (let i = 0; i < all; i++) {
            if (i % chunkNum === offset % chunkNum) {
                // rltArr[i] = "*";
                rltArr[i] = i % per + 1;

            } else {
                rltArr[i] = "#";
            }
        }

        // 遍历 rltArr，拼接为字符，每 per 个元素换行
        let rltStr = "";
        for (let i = 0; i < rltArr.length; i++) {
            rltStr += rltArr[i];
            if ((i + 1) % per === 0) {
                rltStr += "\n";
            }
        }
        return rltStr;
    }

    for (let i = 0; i < 6; i++) {
        console.log(fnPickArr(allNum, perNum, i));
    }
})();

```

「- -」「- -」「- -」

**在研究缓存失效时间时开的一个脑洞，，虽然不是很清楚有什么实用价值：**


```js
(() => {
    let m;
    let lstM;
    let lstN;
    for (let n = 0; n <= 50; n++) {
        if (!m) {
            m = n + 5;
            lstN = n - 1;
        }
        if (m <= n) {
            if (n !== 11 && n !== 12 && n !== 21) {
                // if (1 == 1) {
                fnLog([m - n, m, n, n - lstN, "do some thing"]);
                lstM = m;
                m = n + n - lstN;
                lstN = n + n - lstM;
            } else {
                fnLog([m - n, m, n, n - lstN, "skip"]);
            }
        } else {
            fnLog([m - n, m, n, n - lstN]);
        }
    }
    // ----------------------------
    function fnLog(n) {
        if (Object.prototype.toString.call(n) === "[object Array]") {
            a = n.join(" , ");
        }
        // document.getElementById("debug").innerHTML += a + "<br />";
        console.log(a);
    }
})();

```

<!--2663-->
