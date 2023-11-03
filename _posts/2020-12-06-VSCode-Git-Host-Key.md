---
title: "「VSCode 笔记」Git: Host key verification failed"
date: 2020-12-06 11:20:52
tags:
- VSCode
- Git
- 笔记
categories:
- 电脑网络
id: 3115
alias: 20201216004
---

一直使用`TortoiseGit`这个工具来操作 Git，然而 VSCode 内置支持的情况下来回切换窗口感觉很不优美。。

今天终于第一次试着用 VSCode 提交和推送，但是报了错误提示：

> Git: Host key verification failed

也可能是这种形式

> Warning: Permanently added 'github.com,192.30.255.113' (RSA) to the list of known hosts.

<!--more-->

解决方法：

执行如下命令

```bash
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
```

来源：

[ssh - Git error: 'Host Key Verification Failed' when connecting to remote repository - Stack Overflow](https://stackoverflow.com/questions/13363553 "ssh - Git error: 'Host Key Verification Failed' when connecting to remote repository - Stack Overflow")

--------------------

> 未能对 git remote 进行身份验证

或者

> Permission denied (publickey).

建议使用 SSH 鉴权。

1、将远程地址改为 `git@github.com:wdssmq/HelloZBlog.git` 的形式；

2、打开 Git Bash 执行：

```bash
cd ~/.ssh
ssh-keygen -t ecdsa
# 列出.ssh文件夹的路径
pwd
# c/Users/用户名/.ssh
```

3、在对应路径中找到 `id_ecdsa.pub` ，使用编辑器打开，将其中的内容复制添加到 GitHub 账号中。

可点击链接直接添加：

Add new SSH keys：[https://github.com/settings/ssh/new](https://github.com/settings/ssh/new "Add new SSH keys")

之后即可在 VSCode 中进行提交操作；

--------------------

> ERROR: You're using an RSA key with SHA-1, which is no longer allowed. Please use a newer client or a different key type

解决：

RSA 算法已被认为不再安全（主要取决于密钥长度）；

更直接的方法是更换算法为 ecdsa 或 ed25519，两者之间后者更安全，当然如果你的环境较旧，出现了`unknown key type ed25519`的提示，那么就选前者；

```bash
ssh-keygen -t ed25519
# unknown key type ed25519
ssh-keygen -t ecdsa
```

--------------------

> kex_exchange_identification: Connection closed by remote host

说明：

以我这儿来说就是网络问题，关于 github 的连接问题，首选建议是配置 host 文件，见这个项目： [521xueweihan/GitHub520](https://github.com/521xueweihan/GitHub520 "521xueweihan/GitHub520")

我遇到这个问题是因为在 SSH 配置中设置了代理，然后代理不通了，理论上换个节点也能好，但是正好前边配置过了 host，之后改为直连看看吧；

```ini
Host github.com
  User git
  # ProxyCommand "C:\Program Files\Git\mingw64\bin\connect.exe" -S 127.0.0.1:10808 %h %p

```

--------------------

相关：

[「备忘」msysGit 安装及使用](https://www.wdssmq.com/post/20140804123.html "「备忘」msysGit安装及使用")

[【VSCode】快捷键备忘](https://www.wdssmq.com/post/20130525410.html "【VSCode】快捷键备忘")

`ctrl + shift + g`即可切换到 Git 管理。

[【折腾】VSCode 远程开发配置（Remote Development）](https://www.wdssmq.com/post/20201120519.html "【折腾】VSCode远程开发配置（Remote Development）")

<!--3115-->
