---
title: 「Git_笔记」Git Tag 操作汇总
date: 2022-09-02 17:26:59
tags:
 - Git_笔记
 - 折腾
 - Git
categories:
 - 电脑网络
id: 637
alias: 20220407047
---

日常纠结之：本文内容是因为实际需要查找的资料汇总而成，所以过程中时临时存在哪里更合适呢.jpg

这一次是存在了 github 的 issues 中，之前也了解过一个基于 VSCode 的[[FoamNote]]插件，然而也不太方便；

<!--more-->

`OneNote`，`Simple Sticky Notes`，`QQ 收藏`也是平时者在用的，就挺割裂的；

前不久看到「思源笔记」可以自部署，也想试下；

### 删除 Tag

```bash
# 本地
git tag -d <tagname>
# 远程
git push origin --delete tag <tagname>
```

另一种写法

```bash
git tag -d [tagname]
git push origin :[tagname]
```

### 查看远程 Tag

```bash
git ls-remote --tags origin
# e4eeb3dfc265044ad1a9c367d7d9ad76026194b0        refs/tags/v-2021-08-03
# 5eaed018d1da95e3c2fcd69c02a0b98380f95878        refs/tags/v-2021-08-04
# 1b9476e7e41e39d0575edc461b62ca10c338f572        refs/tags/v-2022-09-02
```

### 查看本地 Tag

```bash
git tag
# v-2021-08-03
# v-2021-08-04
# v-2022-09-02

git tag -n
# v-2021-08-03    工作流 - 自动发布
# v-2021-08-04    update .github\workflows\Release.yml
# v-2022-09-02    base. git CI
```

### 添加并推送 Tag

```bash
git tag -a v-test-2022-09-02 -m '2022-09-02'
git push origin --tags
```

### 远程和本地 Tag 冲突

拉取操作时报错：

> would clobber existing tag

解决：

```bash
# 强制覆盖本地 Tag
git fetch --tags -f
```

would clobber existing tag - 追忆枉然 - 博客园

`https://www.cnblogs.com/liangfc/p/14372579.html`
