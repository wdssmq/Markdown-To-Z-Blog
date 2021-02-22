---
title: 【折腾】用手机写 Markdown 并发布到 Z-Blog
tags:
- 折腾
- Z-Blog
- Markdown
categories:
- 电脑网络
---

## 前言

还是 md2zb 系列，而且可能是最蛋疼的一篇。

更多的只是研究能不能实现，而不是我真的有这个需要。

<!--more-->

## 步骤

- 手机安装 Pocket Git；（收费）
- 手机安装 GitHub 并登录；（免费，好像是官方客户端）
- 准备好 GitHub 的鉴权密钥到手机上；（.ppk格式）
- 在 GitHub 客户端中将相应的库「分享」到 Pocket Git，指定密钥路径后即可添加进来，之后可以执行克隆操作；
- MD 编辑器最终选用了 Markor ；（免费）

----

- 软件内置模板，但是并没有我需要的 hexo 格式，也没有直接自定义的功能：


![001.png](https://i.loli.net/2021/02/22/DSv7O4jf1agcAIx.png) 

- 将模板文件放在一个方便快速找到的位置：

![002.png](https://i.loli.net/2021/02/22/Z8V4ScPIBzLDt1K.png)

- 使用 Markor 的「从本设备导入」功能导入上一步放置的模板文件：

![003.png](https://i.loli.net/2021/02/22/CTjts1b9K2qygYM.png) 

- 改名后编辑使用：

![004.png](https://i.loli.net/2021/02/22/zm5aNjkB39KTcy4.png)

----

- 这个编辑器功能感觉还是蛮给力的：

<details markdown='1'><summary>展开/收起</summary>

2021-22-02 21:21

![005.png](https://i.loli.net/2021/02/22/xany2LQ5lpeoZiT.png) 

</details>



## 关于图片

- `https://imgkr.com/` 好像并不能自动给出 MD 语法。

- `https://sm.ms/` 则有手机端，但是登录失败，先用的网页版，果然很不方便。
- 建议在上传前将图片按使用序号重命名。

以上。
