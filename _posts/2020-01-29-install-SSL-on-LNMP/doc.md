---
title: 【笔记】LNMP 部署/续期 SSL 证书
tags:
- SSL,笔记,LNMP,Linux
categories:
- 电脑网络
id: 2935
alias: 20200129996
zhihu: https://zhuanlan.zhihu.com/p/404135329
cnblogs: https://www.cnblogs.com/wdssmq/p/15193333.html
---

虽然很早就开始用 SSL 了，但是每次续期等于要从头折腾一次，果然还是把自动续期安排上比较好。

> 本记教程用于使用`lnmp.org`一键安装包构建的环境，且版本号为 1.5 或以上

<!--more-->

### 首次部署的简要教程，具体见[^参考链接 1]

```bash
# 以dnspod和namesilo为例，实际应用的鉴权参数需要自行获取并替换

export DP_Id="12345"
export DP_Key="abcdefg"
lnmp dnsssl dp
# 或者
export Namesilo_Key="qwert"
lnmp dnsssl namesilo

# 之后需要输入域名，站点完整目录等信息
# 没有特别需要主域名直接使用根域名wdssmq.com，更多域名里用*.wdssmq.com
# 不要同时出现*.wdssmq.com和www.wdssmq.com之类的

# /home/wwwroot/www.wdssmq.com ← 站点路径建议在方便复制的地方备一份，因为失败或出错的概率还是很大的 /doge

# 同样前边的参数命令可以在文本应用中修改好再复制
```

### 关于续期

上边使用过的 DNS 服务商的授权参数会保存在`/usr/local/acme.sh/account.conf`文件中，可直接执行相应命令续期

```bash
acme.sh --renew -d wdssmq.com
# Renew: 'wdssmq.com'
# Skip, Next renewal time is: Sun Mar 29 03:15:59 UTC 2020
# Add '--force' to force to renew.
# 默认会根据有效期跳过，可参过参数强制执行

# 多个站点的话可一次性检查
acme.sh --cron

# 设置定时任务
crontab -e

0 3 * * * "/usr/local/acme.sh"/acme.sh --cron --home "/usr/local/acme.sh" > /dev/null
```

End

[^参考链接 1](https://lnmp.org/faq/letsencrypt-wildcard-ssl.html "Let'sEncrypt 免费通配符/泛域名SSL证书添加使用教程 - LNMP一键安装包")

