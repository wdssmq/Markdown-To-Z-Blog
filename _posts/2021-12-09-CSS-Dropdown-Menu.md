---
title: 「水坑」Z-Blog 简易二级导航菜单 CSS
tags:
- GesF-Force
- 折腾
- CSS
- Z-Blog
categories:
- 电脑网络
id: 2940
alias: 20200413146
---

历史原因，Z-Blog 的导航、友情链接管理都比较复杂，虽说将来预定会在系统层面进行修改，眼下作为过渡，推荐使用插件：

<!--more-->

> 链接模块管理 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=1873](https://app.zblogcn.com/?id=1873 "链接模块管理 - Z-Blog 应用中心")

插件目前已支持二级导航，只是前台效果需要主题自行适配。

下边代码适用于`default`主题，本文发出不久后预计将直接内置。

```css
#divNavBar li {
  position: relative;
}
#divNavBar li ul {
  display: none;
  position: absolute;
  left: 0;
  white-space: nowrap;
  /* ↓↓ 一般设置为和#divNavBar高度相同 */
  top: 36px;
  /* ↓↓ 背景色同样以实际为准 */
  background-color: #297bc4;
}
#divNavBar li:hover ul {
  display: block;
}
```

对于响应式主题需要考虑手机站效果，不一而足。

使用 Bootstrap 等前端框架构建的主题也可使用其导航组件，链接管理插件支持自定义模板，可直接生成需要的 html 结构，并不局限于 ul->li>(a+ul>li>a) 这种形式。

<!--2940-->
