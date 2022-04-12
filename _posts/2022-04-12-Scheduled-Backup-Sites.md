---
title: 「折腾」Linux 定时备份教程
tags:
- VPS
- Linux
- CentOS
- 折腾
categories:
- 电脑网络
id: 2342
alias: 20140816860
---

2022-04-12：

很多年前的笔记了，也一直有用这个方案备份，然而我能说定时执行用的 crontab 一直没能正确开机自启么？「(╯﹏╰）」

因为开发环境从 Win 换到了 wsl，导致了文件被错误覆盖（代码本身有坑，保是 win 下不会显现），恢复文件时发现备份日期是 3-25，虽然丢失的文本并不是经常修改的到也还好；

<!--more-->

决定先临时搬家到新买的空间里，然后把旧的重装下；

[「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水](https://www.wdssmq.com/post/20220331233.html "「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水")

[「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220211184.html "「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水")

[「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140328160.html "「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水") ← 写下这段文字时并没有真正解决

------

使用环境为 CentOS；

```bash
BAK_DIR=~/Backup

# if [ ! -d ~/BackupTMP ]; then
#   mkdir ~/BackupTMP
# fi

if [ ! -d $BAK_DIR ]; then
  mkdir $BAK_DIR
fi

cd $BAK_DIR

DATE_SUFF=$(date +%Y%m%d)
#—— 日期后缀

if [ ! -d bak_$DATE_SUFF ]; then
  mkdir bak_$DATE_SUFF
fi

# 打包网站文件
cd /home/wwwroot
tar -czf $BAK_DIR/bak_$DATE_SUFF/bak_www.wdssmq.com.tar.gz www.wdssmq.com
# tar -czf $BAK_DIR/bak_$DATE_SUFF/bak_www.wdssmq.com.tar.gz www.wdssmq.com --exclude .git
# tar -czf $BAK_DIR/bak_$DATE_SUFF/bak_www.wdssmq.com.tar.gz www.wdssmq.com \
  # --exclude Editormd \
  # --exclude Neditor \
  # --exclude live2d2 \
  # --exclude WebDir/upload/* \
  # --exclude TidWiki/backup/* \
  # --exclude TidWiki/var/* \
  # --exclude zb_users/cache/thumbs/* \
  # --exclude .git
# —— 不确定上边排除姿势对不对；可以打包一次下回来，用 WizTree 分析占用，排除掉不重要的部分
# —— WizTree - https://www.diskanalyzer.com/

# 导出数据库
/usr/local/mysql/bin/mysqldump -uroot -p数据库密码 数据库名 > $BAK_DIR/bak_$DATE_SUFF/db_www.wdssmq.com.sql.gz
# -u 和 -p 参数值前不能有空格

# del 3 days ago
find $BAK_DIR/ -type d -mtime +5 -name "bak*" -print -exec rm -rf {} \;

# 「可选」镜像同步至远程 FTP
lftp -u FTP用户名,FTP密码 -e "mirror -R --delete --only-newer --verbose $BAK_DIR /远程目录;exit" www.FTP地址.com
```

```bash
if [ ! -d ~/bin ]; then
  mkdir ~/bin
fi
cd ~/bin

code bak.sh
# —— code 是 VSCode 远程连接后打开文件的命令

# 添加执行权限
chmod g+x ~/bin/bak.sh

# 主动执行测试
cd ~
./bin/bak.sh
```

将代码写入到 bak.sh 文件放在 `~/bin` 目录下，然后设置一个定时，比如每天凌晨 3 点执行。

crontab -e

> `0 3 \* \* \* /root/bin/bak.sh`

```bash
chkconfig --list crond
chkconfig --list nginx
chkconfig --list httpd
chkconfig --level 35 crond on
# 查看状态
service crond status
# 启动服务
service crond start
```

定时需要 crontabs，参考：[http://www.ha97.com/910.html](http://www.ha97.com/910.html "crontab")

关于 lftp：参考：[https://www.centos.bz/2011/06/incremental-backup-site-using-lftp/](https://www.centos.bz/2011/06/incremental-backup-site-using-lftp/ "lftp")
