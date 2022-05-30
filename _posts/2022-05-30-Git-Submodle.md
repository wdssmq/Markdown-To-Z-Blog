---
title: 「折腾」Git Submodule 探究
date: 2022-05-31 12:05:58
tags:
- 折腾
- Git
- Hexo
categories:
- 电脑网络
id: 673
alias: 20100710361
---

## 果然还是 Hexo

Hugo 号称自己很快，但是文档过于不完善，还是选择了 Hexo；

## Git Submodule

我已经有一个 git 库，里边有一个`_post`文件夹存放文章；

现想直接让 Hexo 读取里边的文章构建静态站点；

```bash
cd ~/wwwroot/blog
git submodule add git@github.com:wdssmq/Markdown-To-Z-Blog.git md2zb

cd ~/wwwroot/blog/source
# cd ../md2zb/_posts
rm -rf _posts

ln -si ../md2zb/_posts _posts
```

## 两个 Git 库单独存放

```bash
cd ~/wwwroot
git clone git@github.com:wdssmq/Markdown-To-Z-Blog.git md2zb

cd ~/wwwroot/blog/source
# cd ../../md2zb/_posts
rm -rf _posts

ln -si ../../md2zb/_posts _posts
```

## 相关推荐

「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20100604351.html](https://www.wdssmq.com/post/20100604351.html "「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水")
