---
title: 「代码片段」JavaScript 数组的 reduce() 方法
date: 2023-12-16 11:13:22
tags:
 - JavaScript
 - 代码片段
 - 代码
categories:
 - 电脑网络
id: 1027
alias: 20231130787
---

刷贴吧时看到的一个需求示例，让 AI 写了下用的 reduce() 方法，之前只是大概知道有这么个东西，姑且借这个例子加深下印象。

<!--more-->

## 文档

> Array.prototype.reduce() - JavaScript | MDN
>
> [https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce "Array.prototype.reduce() - JavaScript | MDN")

## 代码案例

```js
(() => {
    const data = [
        { k: "a", v: 1 },
        { k: "a", v: 1 },
        { k: "a", v: 2 },
        { k: "a", v: 3 },

        { k: "b", v: 3 },
        { k: "b", v: 3 },
        { k: "b", v: 2 },

        { k: "c", v: 2 },
        { k: "c", v: 1 },
        { k: "c", v: 1 },
    ];
    /* 转换成如下格式
        [
            { k: "a", v: [1, 2, 3] },
            { k: "b", v: [3, 2] },
            { k: "c", v: [2, 1] }
        ];
     */
    const result = data.reduce((acc, cur) => {
        const { k, v } = cur;
        const index = acc.findIndex(item => item.k === k);
        if (index === -1) {
            acc.push({ k, v: [v] });
        } else {
            acc[index].v.push(v);
            // 去重，AI 还是会时不时无视一些明明显式声明的要求。。- -
            acc[index].v = [...new Set(acc[index].v)];
        }
        return acc;
    }, []);

    console.log(result);
})();

```

## 结束

虽然有点水，但是好像也没啥好说的。。

一些其他文章：

- [「代码片段」JavaScript 队列执行异步任务\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20210529408.html "「代码片段」JavaScript 队列执行异步任务\_电脑网络\_沉冰浮水")
- [「备忘」JavaScript 错误提示及解决！\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20170313538.html "「备忘」JavaScript 错误提示及解决！\_电脑网络\_沉冰浮水")
- [「代码片段」当网页元素可见时……\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20190701815.html "「代码片段」当网页元素可见时……\_电脑网络\_沉冰浮水")
