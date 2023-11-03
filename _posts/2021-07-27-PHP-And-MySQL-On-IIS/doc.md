---
title: 「备忘」win10 + IIS + PHP + MySQL
date: 2021-07-27 18:44:10
tags:
- IIS
- PHP
- MySQL
- Win10
- 折腾
categories:
- 电脑网络
id: 612
alias: 20210705807
---

### 前言

又重装了系统，再试过了各种 PHP 环境部署工具后，决定换回 IIS；

<!--more-->

在这之前用的是「[EasyPHP - 略有极客感的 WEB 环境工具\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20210224528.html "EasyPHP - 略有极客感的 WEB 环境工具\_电脑网络\_沉冰浮水")」，最大的问题是只能使用 8000 或 8080 端口，然后所有站点以二级目录的形式访问，再再然后就是每次遇到重启端口号会变；

然后在「下载」文件夹内看到了`xampp`的安装包就顺便试了下，果然也没搞定；


### 安装 IIS

- `Win + x`  → `应用和功能` → `程序和功能` → `启用或关闭 Windows 功能`；
    - 勾选「Internet Information Services」；
    - 依次展开「万维网服务」→「应用程序开发功能」；
    - 勾选「CGI」；
- `开始菜单`  → `Windows 管理工具` → `Internet Information Services (IIS)管理器`；
    - 可以拖动到固定到右边方便打开；

> FastCGI feature must be enabled in order to register PHP.

![001.png](https://i.loli.net/2021/07/27/NqwJDRnU7VegKtb.png "001.png")
![002.png](https://i.loli.net/2021/07/27/D4L7T6gHGulBxvh.png "002.png")


### 创建站点

- 创建一个站点；
    - 绑定域名需要 host 到本机；
    - 对应目录已经存在 Z-BlogPHP 的程序文件，然而访问 403；
    - 「默认文档」里添加`index.php`；
    - 访问站点好像还是不对；

> 由于扩展配置问题而无法提供您请求的页面。如果该页面是脚本，请添加处理程序。如果应下载文件，请添加 MIME 映射。

![003.png](https://i.loli.net/2021/07/27/O4t7bPk9mzLMfCQ.png "003.png")
![004.png](https://i.loli.net/2021/07/27/SpG1WyIXeuZV78d.png "004.png")
![005.png](https://i.loli.net/2021/07/27/TvAP4zbkdxLlSpH.png "005.png")


### PHP 安装和配置

- 下载并安装「PHP Manager For IIS」；
    - 「[PHP Manager 1.5.0 for IIS 10](https://www.iis.net/downloads/community/2018/05/php-manager-150-for-iis-10 "PHP Manager 1.5.0 for IIS 10 : The Official Microsoft IIS Site")」；
- 下载并解压「PHP For Windows」;
    - 「[PHP For Windows: Binaries and sources Releases](https://windows.php.net/download#php-7.4 "PHP For Windows: Binaries and sources Releases")」；
    - 据说 →「Non Thread Safe」版本适用于 IIS，「Thread Safe」适用于 Apache；
    - 本次实际使用「[https://windows.php.net/downloads/releases/php-7.4.21-nts-Win32-vc15-x64.zip](https://windows.php.net/downloads/releases/php-7.4.21-nts-Win32-vc15-x64.zip "VC15 x64 Non Thread Safe")」
- 注册 PHP 到 IIS；
    - 可添加多个版本供切换使用；

![006.png](https://i.loli.net/2021/07/27/prnFJl6y1NvZGPo.png "006.png")
![007.png](https://i.loli.net/2021/07/27/fecKASUltNEhgH8.png "007.png")


### 安装 MySQL 服务

- 安装「MySQL For Windows」；
    - 最新版：「[MySQL :: Download MySQL Installer](https://dev.mysql.com/downloads/windows/installer/ "MySQL :: Download MySQL Installer")」；
    - 历史版本：「[MySQL :: Download MySQL Installer (Archived Versions)](https://downloads.mysql.com/archives/installer/ "MySQL :: Download MySQL Installer (Archived Versions)")」；
    - 可以选择下载在线安装版或者完整版，以实际体验业说，建议下载完整版；
    - 会提示注册账号，但是可以跳过——「`No thanks, just start my download.`」；

![008.png](https://i.loli.net/2021/07/27/mKABRs7PcLkEYQW.png "008.png")
![009.png](https://i.loli.net/2021/07/27/5onyD3xHCISEWf1.png "009.png")
![010.png](https://i.loli.net/2021/07/27/85XYthDfrmOqI3j.png "010.png")
![011.png](https://i.loli.net/2021/07/27/mGhc81wlrsZkNYU.png "011.png")
![012.png](https://i.loli.net/2021/07/27/VPfZJabMWs8ySOX.png "012.png")
![013.png](https://i.loli.net/2021/07/27/2qjRtswhLrHQbkX.png "013.png")
![014.png](https://i.loli.net/2021/07/27/K7toYxVzAva5mbF.png "014.png")
![015.png](https://i.loli.net/2021/07/27/b59FeDZHpENic1W.png "015.png")
![016.png](https://i.loli.net/2021/07/27/b85jnB2H7oySzth.png "016.png")
![017.png](https://i.loli.net/2021/07/27/3TCOtDWXPNFEe4K.png "017.png")
![018.png](https://i.loli.net/2021/07/27/Khqg2MkzVodp3DE.png "018.png")


### phpMyAdmin

- 下载 phpMyAdmin 并在 IIS 添加一个站点；
    - 「[phpMyAdmin](https://www.phpmyadmin.net/ "phpMyAdmin")」；
    - 默认连接端口号就是 3306，理论上可以直接使用 root 账号登录；
    - 上传文件大小限制可能需要修改；「待补充」


### 其他

有个名为「Web 平台安装程序」的东西，理论上可以用来向 IIS 安装 PHP 和 MySQL 之类的，然而 MySQL 版本选项很少，也没装成功；

Web Platform Installer [Web Platform Installer : The Official Microsoft IIS Site](https://www.microsoft.com/web/downloads/platform.aspx "Web Platform Installer : The Official Microsoft IIS Site")
