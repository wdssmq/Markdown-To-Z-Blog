---
title: 「折腾」重装了 VPS 却没有 tar 命令这种事
tags:
- 折腾
- CentOS
- VPS
categories:
- 电脑网络
id: 1117
alias: 20211120519
---

久违的想重装下网站空间，之前用的 CentOS 6，可选里有 CentOS 8 就点了，结果发现 VSCode 服务安装不上，看了下日志发现连 tar 都没有，手动安装又接连出现其他问题，最后直接放弃了，换 CentOS 7 试试；

<!--more-->

推荐：

临时把网站搬到了这里：[「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水](https://www.wdssmq.com/post/20220331233.html "「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水")

备份及搬家总结：[「折腾」Linux 定时备份教程\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140816860.html "「折腾」Linux 定时备份教程\_电脑网络\_沉冰浮水")

VSCode 远程连接教程：[「折腾」VSCode 远程开发配置（Remote Development）\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20201120519.html "「折腾」VSCode 远程开发配置（Remote Development）\_电脑网络\_沉冰浮水")

对于 CentOS 6：[「折腾」CentOS 6 无法使用 Remote Development\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20201120244.html "「折腾」CentOS 6 无法使用 Remote Development\_电脑网络\_沉冰浮水")「当然实际建议还是换掉 CentOS 6 比较好」

并没能解决问题的折腾记录：

```bash
tar --version
# -bash: tar: command not found

yum install -y tar
# CentOS-8 - AppStream  73  B/s |  38  B     00:00
# Failed to download metadata for repo 'AppStream'
# Error: Failed to download metadata for repo 'AppStream'

# 就挺离谱，照着搜索到的方法折腾还是没搞定，错误变成了：
# Error: There are no enabled repositories in "/etc/yum.repos.d", "/etc/yum/repos.d", "/etc/distro.repos.d".

# 算了，，换 CentOS 7 试试；
```
