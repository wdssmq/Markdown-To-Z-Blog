---
title: 【备忘】JavaScript 队列任务执行
- JavaScript
- 备忘
- 折腾
- 代码
categories:
- 电脑网络
id: 462
alias: 20210529408
---

### 需求概述

遍历给定数据（此处为数组），依次执行针对数据项的异步任务。

【【所以格翻的文件名真的有意义么「- -」】】

<!--more-->

### 代码

```js
(() => {
  const items = [
    {
      "code": 1,
      "name": "A",
      "children": [
        {
          "code": 101,
          "name": "A-a"
        },
        {
          "code": 102,
          "name": "A-b"
        }
      ]
    },
    {
      "code": 2,
      "name": "B",
      "children": [
        {
          "code": 201,
          "name": "B-a"
        },
        {
          "code": 102,
          "name": "B-b"
        }
      ]
    }
  ];

  // 执行队列，第二个参数控制是否循环执行
  async function runPromiseByQueue(listPromises, loop = 0) {
    // console.log(listPromises);
    for (let itemPromise of listPromises) {
      await itemPromise();
    }
    if (loop) {
      await runPromiseByQueue(listPromises, loop);
    }
  }

  // 返回项为一个函数，该函数调用时会建立一个 Promise 对象并立即执行
  // 当内部调用 solve() 时表示该异步项执行结束
  const createPromise = (item, level = 0) => () =>
    new Promise((solve) => {
      setTimeout(async () => {
        console.log(level, item.name);
        if (item.hasOwnProperty("children")) {
          level++;
          const curQueue = createQueue(item.children, level);
          await runPromiseByQueue(curQueue);
        }
        solve();
      }, 1370);
    });

  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  // // 理论上也可以像下边这样延迟
  // const createPromise = (item, level = 0) => () =>
  //   new Promise((solve) => {
  //     (async () => {
  //       await sleep(1370);
  //       console.log(level, item.name);
  //       if (item.hasOwnProperty("children")) {
  //         level++;
  //         const curQueue = createQueue(item.children, level);
  //         await runPromiseByQueue(curQueue);
  //       }
  //       solve();
  //     })();
  //   })

  // 构造任务队列
  const createQueue = (arr, level = 0) => {
    return arr.map((item) => {
      return createPromise(item, level);
    });
  };

  // 执行
  const curQueue = createQueue(items);

  runPromiseByQueue(curQueue);

  // // 循环执行
  // runPromiseByQueue(curQueue, 1);
})();
```
