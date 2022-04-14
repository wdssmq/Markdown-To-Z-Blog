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

2022-04-13：新增搬家记录，在文章末尾；

2022-04-12：

很多年前的笔记了，也一直有用这个方案备份，然而我能说定时执行用的 crontab 一直没能正确开机自启么？「(╯﹏╰）」

因为开发环境从 Win 换到了 wsl，导致了文件被错误覆盖（代码本身有坑，保是 win 下不会显现），恢复文件时发现备份日期是 3-25，虽然丢失的文本并不是经常修改的到也还好；

<!--more-->

决定先临时搬家到新买的空间里，然后把旧的重装下；

[「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水](https://www.wdssmq.com/post/20220331233.html "「VPS」HostNamaste $20 年付\_广告慎入\_沉冰浮水")

[「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20220211184.html "「折腾」VSCode + wsl2 + Docker 探究\_电脑网络\_沉冰浮水")

[「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20140328160.html "「折腾」莫名其妙得解决了 wsl2 内 Docker 的自启动\_电脑网络\_沉冰浮水") ← 写下这段文字时并没有真正解决

------

相关推荐：[【笔记】LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20200129996.html "【笔记】LNMP 部署/续期 SSL 证书\_电脑网络\_沉冰浮水")

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

> `0 3 * * * /root/bin/bak.sh`

```bash
# 查看定时任务列表
crontab -l
# 0 3 */7 * * /usr/local/acme.sh/upgrade.sh

# 开启命令行编辑
crontab -e
# —— 实际文件路径在`/var/spool/cron`，VSCode 可直接远程编辑；
# —— 参考： https://www.wdssmq.com/post/20201120519.html

# 修改后重新载入配置文件
/sbin/service crond reload
crontab -l
# 0 3 */7 * * /usr/local/acme.sh/upgrade.sh
# 0 3 * * * /root/bin/bak.sh
```


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

----------

搬家记录正文：

把旧空间的`vhost/*.conf`直接搬到新空间就不需要重新创建了，如果有 ssl 也一起；

旧空间内：

```bash
# 进入旧空间实际存放打包文件夹的路径 /root/Backup/bak_20220413
ln -s /usr/local/apache/conf/vhost vhost_a
ln -s /usr/local/nginx/conf/vhost  vhost_n
if [ ! d /usr/local/nginx/conf/ssl ]; then
  mkdir /usr/local/nginx/conf/ssl
fi
ln -s /usr/local/nginx/conf/ssl    ssl_n
```

然后 sftp 把打包文件和 vhost 文件夹一并下载回来；

新空间内：

```bash
# 新空间内
cd /home/wwwroot
ln -s /usr/local/apache/conf/vhost vhost_a
ln -s /usr/local/nginx/conf/vhost  vhost_n
if [ ! -d /usr/local/nginx/conf/ssl ]; then
  mkdir /usr/local/nginx/conf/ssl
fi
ln -s /usr/local/nginx/conf/ssl    ssl_n
```

phpMyAdmin 内创建数据库表上传`db_*.tar.gz`；

sftp 上传 vhost 文件夹和「站点文件」的打包文件到`wwwroot`目录；

```bash
# 新村空间内
cd /home/wwwroot
# 批量解压文件
for tar in *.tar.gz;  do tar xvf $tar; done
# 文件权限
chown -Rv www:www  /home/wwwroot/*
find ./ -type d -print|xargs chmod 755
find ./ -type f -print|xargs chmod 644
```

**先不要删压缩包或符号连接，FileZilla Client 到是应该可以关掉了，之后 VSCode 内操作；**

检查确认下站点程序内的数据库连接信息；

```bash
# 新空间内
# 重启
lnmp restart
# 写入当前日期到 test.txt，用以验证解析切换是否成功
cd /home/wwwroot
for dir in $(ls -d */); do echo $(date +%Y%m%d) > $dir/test.txt; done
```

**切换解析，等待生效；**

**然后照着上边教程重新配置一次自动备份；**

命令备忘录：

```bash
# 列出子目录
ls -d */
# default/  demo.wdssmq.com/ www.wdssmq.com/
# 按行输出
ls -F | grep /$
default/
demo.wdssmq.com/
www.wdssmq.com/
```

