---
title: 「列表」Beyond Compare 自用过滤规则
date: 2022-09-22 12:28:31
tags:
 - 列表
 - 软件
 - 列表纪事
 - 软件工具
categories:
 - 列表纪事
id: 18
alias: 20100202934
---

使用 Beyond Compare 对文件夹进行比对时可以排除指定文件或文件夹；

<!--more-->

<!-- 文件排除丨排除规则 -->

```ini
; 文件
*-new-post.md
*.crdownload

; 文件夹
__pycache__
_gsdata_
.git
.history
.sync
node_modules
#__SDXC__
*-new-post
*git
*var
*web
Desktop
Documents
OneDrive

```

附：对于「FastCopy」，则使用以下形式排除文件夹：

```txt
.git\;.sync\;.history\;node_modules\;Tencent Files\;tdata\;*-new-post\;
```
