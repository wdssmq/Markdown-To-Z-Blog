---
title: 「列表」Z-Blog 主题、插件注意事项
date: 2020-11-03 10:26:00
tags:
- 列表
- 折腾
- Z-Blog
categories:
- 列表纪事
id: 2926
alias: 20191120012
---

所以用来分隔摘要的`<!-- more -->`标签内要不要加空格呢？

<!-- more -->

1. 404 模板；
2. 404 页标题需要单独指定；
3. 后台配置关键词项逗号替换；
4. 侧栏分类模块过滤文章数为 0 的项；
5. 返回顶部按钮；
6. 字体图标类名不要用默认的；

--------------

1. 使用`$zbp->SetHint('bad', $msg);`之后应该马上重定向页面让错误信息显示；

```php
$zbp->SetHint('bad', $msg);
Redirect('main.php');
```

2. 插件启用时的`$zbp->BuildTemplate();`

3. 插件控制的元素样式应该全部重置一次；

```css
.app,.app * {
  box-sizing: content-box;
  margin: 0;
  padding: 0;
}
```

4. 尽量用`$("p").toggleClass("hidden")`代替`$("p").toggle()`控制显示隐藏/切换；

5. 间接函数尽量封装成`function.php`，只在需要时引入，还有`class`和`vendor`；

<!--2926-->
