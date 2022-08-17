---
title: 「小代码」跨文件按行统计文本「Python」
date: 2022-08-17 14:51:48
tags:
 - 小代码
 - Python
 - 折腾
categories:
 - 电脑网络
id: 32
alias: 20120901104
---

## 说明

一个自用脚本，使用场景如下：

不时会导出一个浏览器插件的配置项作为备份，每个文件可视为一个列表；

想着统计下每一项在全部历史文件中出现在次数然后排序，出现过少的就可以从插件配置中剔除；

<!--more-->

## config.json

需要在脚本同目录下准备一个`config.json`来定义配置项；

```json
{
    "pwd": "目标文件夹路径，绝对地址",
    "ext": ".txt | 要匹配的文件后缀",
    "header": "header demo | 写入生成文件开头\n",
    "footer": "\nfooter demo | 写入生成文件结尾",
    "tpl": "#str# #count# 每一行的文本模板",
    "outfile": "输出文件路径，绝对地址，缺省为「{pwd}/out{ext}」"
}
```

## 下载

py-statistics-lines · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国：

[https://gitee.com/wdssmq/StaleCode/tree/master/py-statistics-lines](https://gitee.com/wdssmq/StaleCode/tree/master/py-statistics-lines "py-statistics-lines · 沉冰浮水/水水的旧代码合集 - 码云 - 开源中国")
