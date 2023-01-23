---
title: 「备忘」RustDesk 服务端安装
date: 2023-01-23 11:05:03
tags:
 - 折腾
 - 备忘
 - 远程桌面
categories:
 - 电脑网络
id: 806
alias: 20230103207
---

Hello World

<!--more-->

```bash
# 下载 rustdesk-server
cd ~/tmp
wget https://github.com/rustdesk/rustdesk-server/releases/download/1.1.7/rustdesk-server-linux-amd64.zip
# 移动到 /usr/local/bin/rustdesk-server
unzip rustdesk-server-linux-amd64.zip
mv amd64 /usr/local/bin/rustdesk-server

# 安装 pm2
npm install pm2 -g

# 获取当前服务器的公网 IP
ip=$(curl -s https://api.ipify.org)

# pm2 start hbbs -- -r <relay-server-ip[:port]>
pm2 start hbbs -- -r $ip -k _
pm2 start hbbr -- -k _
# 端口默认为 21117
# -k _ 参数表示仅允许使用公钥连接，公钥在首次运行时生成的 id_ed25519.pub

# 保存 pm2 进程，并设置开机自启
pm2 save
pm2 startup

# 查看 ip 及公钥
ip=$(curl -s https://api.ipify.org)
key=$(cat /usr/local/bin/rustdesk-server/id_ed25519.pub)
echo -e "ip: $ip\nkey: $key"
```

## 一个报错处理

使用 node 时遇到如下报错，搜索到的答案是 CentOS 7 不支持 node 18.13.0，降级后解决；

```bash
# node: /lib64/libm.so.6: version `GLIBC_2.27' not found (required by node)
# node: /lib64/libc.so.6: version `GLIBC_2.25' not found (required by node)
# node: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by node)
# node: /lib64/libstdc++.so.6: version `CXXABI_1.3.9' not found (required by node)
# node: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by node)
# node: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by node)
```
node 使用的是 nvm 管理；

```bash
nvm list
#        v18.13.0
# default -> lts/* (-> v18.13.0)
# iojs -> N/A (default)
# unstable -> N/A (default)
# node -> stable (-> v18.13.0) (default)
# stable -> 18.13 (-> v18.13.0) (default)
# lts/* -> lts/hydrogen (-> v18.13.0)
# lts/argon -> v4.9.1 (-> N/A)
# lts/boron -> v6.17.1 (-> N/A)
# lts/carbon -> v8.17.0 (-> N/A)
# lts/dubnium -> v10.24.1 (-> N/A)
# lts/erbium -> v12.22.12 (-> N/A)
# lts/fermium -> v14.21.2 (-> N/A)
# lts/gallium -> v16.19.0 (-> N/A)
# lts/hydrogen -> v18.13.0

# 安装并使用 16.19.0
nvm install 16.19.0
nvm use 16.19.0
```
