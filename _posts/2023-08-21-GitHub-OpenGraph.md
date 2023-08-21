---
title: 关于 GitHub 的 OpenGraph 接口
date: 2023-08-21 18:03:38
tags:
 - GitHub
 - 互联网
categories:
 - 电脑网络
id: 708
alias: 20230223986
---

GitHub 的 OpenGraph 接口，可以用来生成图形化展示 Git 库信息，包括仓库和 issues ，但是好像没有针对用户页的接口。

<!--more-->

> 下边地址可以订阅我的 GitHub 动态，包括公开仓库和 issues:
>
> [https://github.com/wdssmq.atom](https://github.com/wdssmq.atom "GitHub Public Timeline Feed Of wdssmq")

实际 `token` 部分是一个长串，然后可随意更改，或许是针对私有库的？

repo：`https://opengraph.githubassets.com/token/wdssmq/GesF-Note`

issues: `https://opengraph.githubassets.com/token/wdssmq/GesF-Note/issues/1`

![wdssmq/GesF-Note](https://opengraph.githubassets.com/token/wdssmq/GesF-Note)

![wdssmq/GesF-Note/issues/1](https://opengraph.githubassets.com/token/wdssmq/GesF-Note/issues/1)

用户页实际用的是头像 ——

```html
<meta property="og:image" content="https://avatars.githubusercontent.com/u/8186642?v=4?s=400" />
<meta property="og:image:alt"
    content="置百丈玄冰而崩裂，掷须臾池水而漂摇。. wdssmq has 84 repositories available. Follow their code on GitHub." />
<meta property="og:site_name" content="GitHub" />
<meta property="og:type" content="profile" />
<meta property="og:title" content="wdssmq - Overview" />
<meta property="og:url" content="https://github.com/wdssmq" />
<meta property="og:description"
    content="置百丈玄冰而崩裂，掷须臾池水而漂摇。. wdssmq has 84 repositories available. Follow their code on GitHub." />
<meta property="profile:username" content="wdssmq" />

```

