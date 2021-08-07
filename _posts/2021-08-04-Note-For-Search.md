---
title: 【真·碎碎念】2021/07/26 ~ 2021/08/01
tags:
- 碎雨集
- 碎碎念
- 杂七杂八
- 纠结
categories:
- 杂七杂八
---
### 2021-07-26 08:20
微软五笔不能自动调整词序，结果仍然不够好用。

<!--more-->

### 2021-07-26 08:23
搜狗五笔 2021-7-23 更新了一波，其实不更新也可以的。

### 2021-07-26 09:10
QTTabBar 也是有点好用又好像不太够的感觉；这次装了 Beta，虽然我并没有升级 Win11；Win11 也要加入输入法短语了。

### 2021-07-26 09:44
然后发现 Beta 版没语言包。。。

### 2021-07-27 14:34
xampp 并不好用的感觉。。

### 2021-07-27 14:56
由于扩展配置问题而无法提供您请求的页面。如果该页面是脚本，请添加处理程序。如果应下载文件，请添加 MIME 映射。

### 2021-07-27 14:58
FastCGI feature must be enabled in order to register PHP.

### 2021-07-27 17:24
IIS 才是最好的 PHP 开发环境；

### 2021-07-27 19:16
日常搞不懂各种选项；

### 2021-07-28 11:13
人生就是在不断填旧坑的过程中发现新坑；

### 2021-07-30 13:04
正好八月一号是星期日，要不改成按月？还是说按双周，，再就是弄个提醒。

### 2021-07-31 09:21
学校，迟到，电梯故障，17 楼和 16 楼中间出现的特异空间，也是要素齐全的梦。

### 2021-08-04 13:07 备忘 | 碎雨集回调函数

```js
$(".mz-snt-item h3").each(function(i,el){
  const $this = $(this);
  const strText = $this.html();
  $this.html(`### ${strText}`);
  i===0 && $this.parent().append("<p>&lt;!--more--&gt;</p>");
});
```
### 2021-08-07 17:58 笔记 | Docker 网络相关

- 列出网络：

`docker network ls`

- 创建网络：

`docker network create --driver bridge net_web`

或者：

`docker network create -d bridge net_web`

- 查看指定网络信息：

`docker network inspect net_web`

- 创建容器时指定网络：

`docker run --name MySQL -d --network net_web -e MYSQL_ROOT_HOST=172.%.%.% -e MYSQL_ROOT_PASSWORD=MySQLPWD mysql/mysql-server:5.7`

- 使用容器名访问同网络的数据库：

`docker run --name PHPMyAdmin -d --network net_web -e PMA_HOST=MySQL -p 9100:80 phpmyadmin/phpmyadmin`

- 已经存在的容器连接到网络：

`docker network connect net_web zbp_ForAPP`

- 备份容器内的数据库：

`docker exec -it MySQL mysqldump -uroot -pMySQLPWD zbp_ForAPP > /root/mysql_file_backup/Docker_db_zbp_ForAPP.sql`

- 附加说明：

对于同一网络内的容器，相互之间可以通过容器名进行访问通信，该功能称之为`Docker DNS Server`；

使用 docker DNS 有个限制：只能在 user-defined 网络中使用。也就是说，默认的 bridge 网络是无法使用 DNS 的。