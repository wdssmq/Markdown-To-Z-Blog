---
title: 「Git_笔记」HEAD detached from xxxx 问题解决
date: 2022-11-27 14:27:22
tags:
 - Git_笔记
 - 折腾
 - Git
categories:
 - 电脑网络
id: 63
alias: 20221127394
---

久违的想写个有点复杂的 Z-BlogPHP 插件，中间需要参考自己的其他项目，顺手改了下插件的一些格式排版，加了个新方法什么的，然而 git 提交时出错了- -

<!--more-->

重点错误/状态信息：

> (HEAD detached from xxxx)
>
> You are not currently on a branch.

```bash
git pull
# You are not currently on a branch.
# Please specify which branch you want to merge with.
# See git-pull(1) for details.

#     git pull <remote> <branch>

git bra
# * (HEAD detached from 3bff3f0)
#   master
#   remotes/origin/HEAD -> origin/master
#   remotes/origin/master

git rev

# origin  git@github.com:wdssmq/kumo-for-zblog.git (fetch)
# origin  git@github.com:wdssmq/kumo-for-zblog.git (push)
```

**注：**

**`git bra`和`git rev`，包括下边的`git sw` | `git mnc`都是我自己定义的别名；**

**`git branch -h`可以看到具体的命令说明；**

```bash
# 从当前 HEAD 复制一个临时分支

git br for-fix-2211
git bra
# * (HEAD detached from 3bff3f0)
#   for-fix-2211
#   master
#   remotes/origin/HEAD -> origin/master
#   remotes/origin/master

# 好像看不出啥，加个 -v 参数看看

git bra -v
# * (HEAD detached from 3bff3f0) ec3bf35 base. git 配置
#   for-fix-2211                 ec3bf35 base. git 配置
#   master                       3bff3f0 规则为空时的提示信息；
#   remotes/origin/HEAD          -> origin/master
#   remotes/origin/master        3bff3f0 规则为空时的提示信息；

# 切换到 master 分支

git sw master
git bra -v
#   for-fix-2211          ec3bf35 base. git 配置
# * master                3bff3f0 规则为空时的提示信息；
#   remotes/origin/HEAD   -> origin/master
#   remotes/origin/master 3bff3f0 规则为空时的提示信息；

#  合并分支

git mnc for-fix-2211
git bra -v
#   for-fix-2211          ec3bf35 base. git 配置
# * master                ec3bf35 [ahead 3] base. git 配置
#   remotes/origin/HEAD   -> origin/master
#   remotes/origin/master 3bff3f0 规则为空时的提示信息；

# 删除临时分支然后推送就可以了

git br -d for-fix-2211
git push
```

----

Git - git-branch Documentation：

[https://git-scm.com/docs/git-branch/zh_HANS-CN](https://git-scm.com/docs/git-branch/zh_HANS-CN "Git - git-branch Documentation")
----

「折腾」git 及 docker 命令快捷输入\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20171130103.html](https://www.wdssmq.com/post/20171130103.html "「折腾」git 及 docker 命令快捷输入\_电脑网络\_沉冰浮水")
