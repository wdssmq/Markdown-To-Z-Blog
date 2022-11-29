---
title: 「Git_笔记」git remote 命令
date: 2022-11-29 22:27:15
tags:
 - Git_笔记
 - 折腾
 - Git
categories:
 - 电脑网络
id: 702
alias: 20220525683
---

经常是先克隆了原始项目查看，然后发现需要作些修改，就需要 Fork 到自己账号下一份，所以要再修改一下远程仓库地址；

涉及命令为：`git remote`；

<!--more-->

```bash
# 查看远程仓库

git remote -v
# origin  git@github.com:BrowserSync/browser-sync.git (fetch)
# origin  git@github.com:BrowserSync/browser-sync.git (push)

# 重命名远程仓库

git remote rename origin BrowserSync
git remote -v

# 添加远程仓库

git remote add wdssmq git@github.com:wdssmq/browser-sync.git
git remote -v

# 获取并查看分支信息

git fetch -a
git branch -a

# 设置默认仓库

git config branch.master.remote wdssmq

# 下边命令可以直接修改远程仓库地址

# git remote set-url origin <url>

```


