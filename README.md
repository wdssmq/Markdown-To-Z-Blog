# Markdown-To-Z-Blog
同步*.md 内容到 Z-Blog

---start---

---end---

zhaoolee/WordPressXMLRPCTools: 用 Hexo 的方式管理 WordPress
https://github.com/zhaoolee/WordPressXMLRPCTools

## 命令（本地测试）

```shell
pip install markdown
pip install requests
pip install python-frontmatter
```

创建config.json并按如下示例填写内容：

```json
{
    "username": "zblog_usr",
    "password": "zblog_pwd",
    "API-URL": "http://zblog.site/zb_system/api.php"
}
```

## 文章书写

_posts/*.md

```md
---
title: 文章标题
tags:
- 标签一
- 标签二
categories:
- 分类名
---

正文段落一

正文段落二

```
