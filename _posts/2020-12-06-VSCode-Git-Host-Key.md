---
title: 【VSCode 笔记】Git： Host key verification failed
tags:
- VSCode,Git,笔记
categories:
- 电脑网络
id: 3115
alias: 20201216004
---

一直使用`TortoiseGit`这个工具来操作 Git，然而 VSCode 内置支持的情况下来回切换窗口感觉很不优美。。

今天终于第一次试着用 VSCode 提交和推送，但是报了错误提示：

> Git: Host key verification failed

<!--more-->

解决方法,Git Bash 中运行下边代码：

```bash
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
```

来源：

[ssh - Git error: 'Host Key Verification Failed' when connecting to remote repository - Stack Overflow](https://stackoverflow.com/questions/13363553 "ssh - Git error: 'Host Key Verification Failed' when connecting to remote repository - Stack Overflow")

--------------------

> 未能对 git remote 进行身份验证

建议使用 SSH 鉴权。

1、 将远程地址改为 `git@github.com:wdssmq/HelloZBlog.git` 的形式；

2、 打开 Git Bash 执行：

```bash
cd ~/.ssh
ssh-keygen
# 列出.ssh文件夹的路径
pwd
# c/Users/用户名/.ssh
```

3、在对应路径中找到 `id_rsa.pub` ，使用编辑器打开，将其中的内容复制添加到 GitHub 账号中。

可点击链接直接添加：

Add new SSH keys：[https://github.com/settings/ssh/new](https://github.com/settings/ssh/new "Add new SSH keys")

之后即可在 VSCode 中进行提交操作；

--------------------

相关：

[【备忘】msysGit 安装及使用](https://www.wdssmq.com/post/20140804123.html "【备忘】msysGit安装及使用")

[【VSCode】快捷键备忘](https://www.wdssmq.com/post/20130525410.html "【VSCode】快捷键备忘")

`ctrl + shift + g`即可切换到 Git 管理。

[【折腾】VSCode 远程开发配置（Remote Development）](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）")

<!--3115-->
