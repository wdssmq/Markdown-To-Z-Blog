---
title: 「水坑」如何正确的自定义 CSS 样式
tags:
- GesF-Force
- 折腾
- 教程
categories:
- 电脑网络
id: 477
alias: 20190705015
---

### 索引

[「水坑」系列教程索引](/post/20200617652.html "「水坑」系列教程索引")

[「水坑」如何正确的自定义 CSS 样式](/post/20190705015.html "「水坑」如何正确的自定义 CSS 样式") 「当前」

<!--more-->

### DevTools

在浏览器中，`Ctrl + Shift + i` 或 `F12` 都可以打开「开发者工具」，常说的是「控制台」也指的是这里；

### 查看元素

除使用快捷外，也可以在网页内「右键」→「检查/查看元素」打开，具体浏览器选项名会有差异；「图 1」

此种方式打开时，会自动在控制台的「元素」选项卡内定位到右键操作时鼠标所指向的元素；「图 2」

![001.png](https://i.loli.net/2021/08/27/M9QW2DilxaqnIpm.png)

图 1 ↑

![002.png](https://i.loli.net/2021/08/27/wPWKOeRMs6kvI4u.png)

图 2 ↑

同时右边会显示相应元素的「样式」信息；「图 3」

点击某一条样式后边的蓝色链接（`*.css`），会跳转到具体的样式定义查看，可以得到具体所在的行号等信息「- 如果没有压缩的话 -」；

在「图 3」区域所作的修改会实时反应在页面中，达到所需效果后可以复制到真实文件中实现样式更新；

**然而除非你是该样式的实际维护者，并不推荐这么做。**

比如对于 Z-Blog 主题，如果主题自身未提供自定义功能，推荐使用：[添加自定义CSS样式 - Z-Blog 应用中心](https://app.zblogcn.com/?id=18357 "添加自定义CSS样式 - Z-Blog 应用中心")

追加的样式会覆盖已有定义，主题升级也不会被重置；

![003.png](https://i.loli.net/2021/08/27/dpCYxEvRgVWhubj.png)

图 3 ↑

### 「样式类」和「语义类」

虽然现在才说，CSS 的知识终究需要你自己学习「CSS 教程：[https://www.w3school.com.cn/css/index.asp](https://www.w3school.com.cn/css/index.asp "CSS 教程")」

本次的需求是自定义调整「图 2」中链接的字号；

然而直接影响到该元素的样式定义如下：

```css
a.a-color, .a-color a {
    color: #000;
}
.is-px-12 {
    font-size: 14px;
}
.has-text-centered {
    text-align: center !important;
}
```

个人定义为「样式类」，具体怎么理解和划分只能靠经验补足吧.jpg

简单说上边几个样式定义，如果修改或覆盖的话，极大概率会影响到其他使用了该样式的元素；

所以需要从目标元素开始，由内向外选取一个有足够「语义」的元素——

`p`：并没有额外类名所以跳过；——

「图 4」`div.media-content`：`.media-content`本身是前端框架组件中的定义，有一定的「语义」，然而其他地方也有可能使用该组件和结构；——

「图 5」`div.media.slide-info`：`.media`同样是前端组件，但是`.slide-info`，英文单词「slide」在网页前端语境下通常就是指「幻灯片」，虽然也有存在多处幻灯片的情况，然而相对容易直接观察求证，另外也可以通过组合多级选择器尽量避免非预期的影响；

![004.png](https://i.loli.net/2021/08/27/wdSyfK7kBnGraqZ.png)

图 4 ↑

![005.png](https://i.loli.net/2021/08/27/YufkalnKIB3dAmH.png)

图 5 ↑

最终结果就是：

```css
.slide-info .media-content a {
  /* 可自行确定字号或其他样式定义 */
  font-size: 15px;
}
```

### 其他

「图 3」所示区域内，点击右上的「+」号按钮，可以触发针对「选中元素」的「新建样式规则」，示例：

```css
.media.slide-info {
}
```

↑ 会自动拼接全部类名作为选择器，可能需要根据实际情况调整；

另「:hov」「.cls」两个按钮我竟然才注意到，会是非常有用的功能，一直都不知道这里有快捷入口；

![003.png](https://i.loli.net/2021/08/27/dpCYxEvRgVWhubj.png)

图 3 ↑
