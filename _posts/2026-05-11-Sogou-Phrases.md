---
title: 「小代码」搜狗输入法自定义短语分片管理「Python」
date: 2026-05-11 14:47:43
tags:
 - 小代码
 - Python
 - 输入法
 - 五笔
categories:
 - 电脑网络
id: 667
alias: 20221009482
---

**· 简介 ——**

搜狗输入法有个「自定义短语」功能 —— 「通过英文字符作为缩写，来输入自定义的特殊符号、短语、短文等」；

<!--more-->

```ini
; 键入 vsc 就能输入 VSCode，数字序号用于指定目标短语在候选列表中的位置
vsc,3=VSCode

```

这个东西有表单管理界面，也可以直接编辑 `.ini` 文件，登录账号后还可以云同步；

不过我还是 Vibe 了一个 Python 脚本来实现特殊的管理姿势 —— 编辑维护多个 `yaml` 文件，由脚本拼接为所需的 `.ini` 文件；

**· 代码地址 ——**

> L78Z-No-Code/py-sogou-phrases at main · wdssmq/L78Z-No-Code
>
> [https://github.com/wdssmq/L78Z-No-Code/tree/main/py-sogou-phrases](https://github.com/wdssmq/L78Z-No-Code/tree/main/py-sogou-phrases "L78Z-No-Code/py-sogou-phrases at main · wdssmq/L78Z-No-Code")

**· 其他 ——**

用五笔打字的人你伤不起啊\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/YongWuBiDaZiDeRenNiShangBuQiA.html](https://www.wdssmq.com/post/YongWuBiDaZiDeRenNiShangBuQiA.html "用五笔打字的人你伤不起啊\_电脑网络\_沉冰浮水")

更多「小代码」：

[https://cn.bing.com/search?q=小代码+沉冰浮水](https://cn.bing.com/search?q=%E5%B0%8F%E4%BB%A3%E7%A0%81+%E6%B2%89%E5%86%B0%E6%B5%AE%E6%B0%B4 "小代码 沉冰浮水 - 必应搜索")
