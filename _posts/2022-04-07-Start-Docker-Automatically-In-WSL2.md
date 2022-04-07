---
title: 「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动
tags:
- Docker
- Ubuntu
- WSL2
- 折腾
categories:
- 电脑网络
id: 2158
alias: 20140328160
---

### 一、“解决”方案

前文推荐：「[「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220211184.html "「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水")」

网上最常见到命令好像并不生效，所以一直靠着输入法快捷输入`sudo service docker start`来运行，但果然是很麻烦；

<!--more-->

```bash
sudo systemctl enable docker
# Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
# Executing: /lib/systemd/systemd-sysv-install enable docker
```

中间几篇解决方案不知道为什么连尝试都不想尝试，然后点到了一篇英文的：

> How to automatically start the Docker daemon on WSL2 – NillsF blog
> `https://blog.nillsf.com/index.php/2020/06/29/how-to-automatically-start-the-docker-daemon-on-wsl2/`

这个方案需要安装 zsh，安装见本文第二节；

· 首先需要设置你的用户在执行 sudo 时不需要输入密码，我已经设置过了，虽然并不理解为什么能生效所以没也写笔记；

· 向 `~/.zshrc` 写入内容：

```bash
echo '# Start Docker daemon automatically when logging in if not running.' >> ~/.zshrc
echo 'RUNNING=`ps aux | grep dockerd | grep -v grep`' >> ~/.zshrc
echo 'if [ -z "$RUNNING" ]; then' >> ~/.zshrc
echo '    sudo dockerd > /dev/null 2>&1 &' >> ~/.zshrc
echo '    disown' >> ~/.zshrc
echo 'fi' >> ~/.zshrc
```

· 执行如果下命令，效果是在执行 docker 命令时可以不加 `sudo`？：

```bash
sudo usermod -a -G docker $USER
# -G 修改用户附加群组
# -a 参数表示附加，只和 -G 参数一同使用，表示将用户增加到组中
```

### 二、安装 zsh

> Oh-My-Zsh 的配置与使用 - 再见理想_ - 博客园
> https://www.cnblogs.com/monsterdev/p/11166720.html

```bash
sudo apt update
sudo apt install git zsh -y

# 安装 Oh My Zsh
sh -c "$(curl -fsSL https://cdn.jsdelivr.net/gh/ohmyzsh/ohmyzsh@master/tools/install.sh)"

# 切换至 zsh
chsh -s /bin/zsh

# 版本查看
zsh --version
# zsh 5.4.2 (x86_64-ubuntu-linux-gnu)

# 查看当前 shell
# 如果没有切换成功，可以关掉终端或 VSCode 重新打开再看
echo $SHELL
# /bin/zsh

# sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

<!-- > Error: Oh My Zsh can't be loaded from: bash. You need to run zsh instead. -->

