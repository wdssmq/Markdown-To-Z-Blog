---
title: 【备忘】textarea 内输出 html 的转义问题
tags:
- 折腾
- 备忘
- HTML
categories:
- 电脑网络
---

习惯上，在需要使用 `<input type="text" />`或`<textarea></textarea>`回显可编辑内容时，都会将其中的 HTML 实体转义；

<!--more-->

`<input type="text" value="<?php echo htmlspecialchars($strText); ?>" />`

`<textarea><?php echo htmlspecialchars($strLongText); ?></textarea>`

对于前者，因为作为属性值输出，所以必须要转义；

至于后者，以下边代码为例，两个文本框都是可以正确被浏览器渲染的，但是对于不转义的情况，如果`<script>alert("aaaa");</script>`前边插入 `</textarea>`时，JS 代码就会执行。

所以结论是同样推荐使用转义写法；

```html
<!-- 未转义 -->
<textarea name="text1" id="text1" cols="35" rows="10">
  <b>3333</b>
  ---
  <script>alert("aaaa");</script>
</textarea>
<!-- 转义写法 -->
<textarea name="text2" id="text2" cols="35" rows="10">
  &lt;b&gt3333&lt;/b&gt
  ---
  &lt;script&gt;alert(&quot;aaa&quot;);&lt;/script&gt;
</textarea>
```

HTML 字符实体：

[https://www.w3school.com.cn/html/html_entities.asp](https://www.w3school.com.cn/html/html_entities.asp "HTML 字符实体")
