---
title: 「CentOS 笔记」常见错误提示整理「2022-04-15」
date: 2022-04-15 11:04:27
tags:
- Linux
- 备忘
- 折腾
categories:
- 电脑网络
id: 2756
alias: 20170421527
---

错误提示：

> `www.wdssmq.com:Verify error:DNS problem: SERVFAIL looking up CAA for www.wdssmq.com`

<!--more-->

解决：

使用脚本申请 SSL，尤其是通配符时可能会遇到以上错误。只说要点：

1、域名只写根域 `wdssmq.com`，`*.wdssmq.com www.wdssmq.com`之类的之后直接在配置文件里添加，包括文件名也可以稍后再改，如果有需要的话；

2、用于申请证书的域名本身必须是 A 记录，不能是 CNAME。

----------------------------

错误提示：

> `# tar: www.wdssmq.com-access_log: file changed as we read it`
>
> `# tar: www.wdssmq.com.log: file changed as we read it`

解决：

```bash
cd /home
if [ ! -d wwwlogs_$(date +%Y%m%d) ]; then
  mkdir wwwlogs_$(date +%Y%m%d)
  mv wwwlogs wwwlogs_$(date +%Y%m%d)
  mkdir wwwlogs
  tar -czvf wwwlogs_$(date +%Y%m%d).tar.gz wwwlogs_$(date +%Y%m%d)
fi
```

说明：

在尝试打包网站日志时会提示文件已发生改变，解决思路为将日志文件夹重名命后再打包。

-----------------

错误提示：

> `/bin/sh: cc: command not found`
>
> 照着其他教程安装 gcc gcc-c++ 后仍然未解决，实际安装 gcc 过程中有另一条提示：
>
> `Requires: kernel-headers -csdn`

解决：

```bahs
yum install -y kernel-headers --disableexcludes=all
```

修复缺少 Kernel-Headers on CentOS 7，导致 gcc glibc-headers 安装失败：
`https://www.cnblogs.com/morse/p/14476783.html`

-----------------

错误提示：

> Yum update fails on a 404 returned from http://***/repodata/repomd.xml
>
> 或者
>
> All mirror URLs are not using ftp, http[s] or file.

解决：

> CentOS 5.9 出现过的错误，2022 年了应该不会再有了吧。。
