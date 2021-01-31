# Markdown-To-Z-Blog
同步*.md 内容到 Z-Blog

---start---

## 目录( 2021 年 01 月 31 日更新)

[欢迎使用Z-BlogPHP！](https://zbp17.wdssmq.com/post/1.html "欢迎使用Z-BlogPHP！")

[【折腾】VSCode中运行Python提示没有权限](https://zbp17.wdssmq.com/post/3.html "【折腾】VSCode中运行Python提示没有权限")

[【折腾】GM脚本修改B站番剧链接为我的追番](https://zbp17.wdssmq.com/post/4.html "【折腾】GM脚本修改B站番剧链接为我的追番")

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
    "API-USR": "zblog_usr",
    "API-PWD": "zblog_pwd",
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
