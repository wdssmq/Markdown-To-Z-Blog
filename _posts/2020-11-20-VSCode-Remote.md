---
title: 【折腾】VSCode 远程开发配置（Remote Development）
tags:
- VSCode,Linux,VPS,折腾
categories:
- 电脑网络
id: 3110
alias: 20201120519
---

如果你用的空间系统版本不支持，可以先参考下边文章：

[【折腾】CentOS 6 无法使用 Remote Development\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20201120244.html "【折腾】CentOS 6无法使用Remote Development\_电脑网络\_沉冰浮水")

[ShortSth:主机云][/ShortSth] ←← 没办法，用的这家的垃圾空间（他们自我评价的原话，`虽然我们是很垃圾，但是我们也严格限制垃圾客户入住.`）←←（没错，这段是广告）←←（所以主要是升级 CentOS 7 太麻烦了）

<!--more-->

1、本地安装 Git [【备忘】msysGit 安装及使用\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140804123.html "【备忘】msysGit安装及使用\_电脑网络\_沉冰浮水")

2、VSCode 中搜索安装 Remote Development（会安装一整套的插件）

3、打开 Git Bash 执行：

```bash
cd ~/.ssh
ssh-keygen
# 列出.ssh文件夹的路径
pwd
# c/Users/用户名/.ssh
```

4.1、对于腾讯云添加`id_rsa.pub`的内容到服务器的[SSH 密钥]中并绑定到[实例]

4.2、

对于面板中没有添加公钥位置的空间，可以通过 sftp 上传`id_rsa.pub`到远程的某个文件夹下，比如`/root/.ssh`

然后使用密码连接到远程终端：

```shell
cd /root/.ssh
cat id_rsa.pub >> authorized_keys
```

5、VSCode 的「活动栏」里会多出一个「远程资源管理器」，虽然我习惯隐藏掉「活动栏」，也可以用编辑器左下角的绿色图标「打开远程窗口」【感觉需要给「远程资源管理器」设置个快捷键。

「远程资源管理器」→「SSH Targets」→「点击+符号」 → 输入 `ssh root@远程ip` → 选择默认的保存位置。

一般是`C:\Users\用户名\.ssh\config`;

6、编辑配置可设置别名（侧栏的齿轮图标）

```conf
Host 腾讯云
  HostName 56.123.132.111
  User root

Host 另一台
  HostName 56.34.77.22
  User root
```

7、「远程资源管理器」→「SSH Targets」中列出已经添加的远程项目列表，相应项目上右键可选择在当前窗口打开或新窗口打开。

7.1

```json
"remote.SSH.remotePlatform": { "losangelesvps": "linux", "腾讯云": "linux" }
```

↑↑ 理论上首次连接时会询问要连接的主机系统然后保存（Linux，Mac，Windows），但是主机名设置中文时好像会每次都要询问，可以手动添加；

8、查看 → 终端 直接就是远端的命令行。快捷键[ctrl + `]

9、这时「资源管理器」(ctrl + shift + e)中会显示「已连接到远程」，点击「打开文件夹」可浏览并选择远程文件夹作为工作路径，可直接编辑其中的文件然后保存；已经打开过的文件夹会在「远程资源管理器」中其所属的服务器下列出，下次可快速打开。

10、接第 8 条，远程安装 Git 和 Node

```bash
# 依赖
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
yum install gcc perl-ExtUtils-MakeMaker

# yum install git ← 这个安装版本不是最新的
yum remove git

yum install wget # 未安装过 wget，需要先安装

cd ~
if [ ! -d "tmp" ]; then
  mkdir tmp
fi
cd ~/tmp
# 最新版本地址见：https://git-scm.com/download/linux
GIT_VER=2.33.0
wget https://www.kernel.org/pub/software/scm/git/git-${GIT_VER}.tar.gz
# 镜像地址
# wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-${GIT_VER}.tar.gz
tar zxf git-${GIT_VER}.tar.gz

# 编译安装
# cd ~/tmp
# cd git-${GIT_VER}
# make prefix=/usr/local/git all
# make install

# 编译安装
cd ~/tmp
cd git-${GIT_VER}
./configure --prefix=/usr/local/git
make && make install

# 环境变量
echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/profile
source /etc/profile

# 查看版本
git version

# Node

# 安装nvm
# 最新版见：https://github.com/nvm-sh/nvm
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.0/install.sh | bash

nvm install --lts
nvm use --lts

```

这才是真正的远程开发——VS Code Remote 环境搭建
https://juejin.im/post/6844904000639205384

VS Code Remote SSH 配置 - 知乎
https://zhuanlan.zhihu.com/p/68577071
<!--3110-->
