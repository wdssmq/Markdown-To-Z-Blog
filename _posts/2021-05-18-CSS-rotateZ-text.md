---
title: 【折腾】CSS 角标文字（失败版）
tags:
- CSS
- 折腾
- 电脑网络
categories:
- 电脑网络
id: 750
alias: 20141212329
---

### 前言

其实原来弄过同样的效果，，然而我却忘记是从哪儿抄得了。。然后现搜了一个抄，结果总觉得各种不对。。

快弄完才想起来，，我当时是从 Z-Blog 应用中心抄得，，收费应用的价格就是角标效果。。。emmm

<!--more-->

### 代码

以下方法倒也是能实现，但是在三角形的直角边与父元素重合定位时要计算尺寸，或者微调试值。。。

```html
<style>
  .mz-wraper,
  .mz-wraper * {
    box-sizing: border-box;
  }
  .mz-body {
    position: relative;
    width: 180px;
    height: 180px;
  }
  .mz-icon {
    position: absolute;
    right: 0;
    top: 0;
    transform: rotateZ(45deg);
  }
  .mz-icon .mz-bg {
    display: block;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 0 37px 37px 37px;
    border-color: transparent transparent #20C05C transparent;
    /* ↓ 这两个值得确定比较麻烦 ↓ */
    margin-right: -21.5px;
    margin-top: -15.5px;
  }
  .mz-icon .mz-text {
    position: absolute;
    top: 0;
    right: 0;
    display: inline-block;
    text-align: center;
    /* ↓ 这个值也要单独确定 ↓ */
    width: 31px;
    color: #FFF;
  }
</style>

<div class="mz-wraper">
  <div class="mz-body">
    <img src="logo.png" class="mz-img">
    <div class="mz-icon">
      <span class="mz-bg"></span>
      <span class="mz-text">推荐</span>
    </div>
  </div>
</div>
```
