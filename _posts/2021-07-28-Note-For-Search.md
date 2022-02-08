---
title: 【真·碎碎念】2021/07/19 ~ 2021/07/25
tags:
- 碎碎念
- 杂七杂八
- 纠结
categories:
- 杂七杂八
id: 2106
alias: 20140301127
---
### 2021-07-19 10:47
阮一峰抱怨自己被广告屏蔽规则针对就挺凡尔赛的。。

<!--more-->

### 2021-07-19 12:17
vue3 安装插件的姿势：```export default { install: (app, options) => { app.config.globalProperties.$htmlEscape = htmlEscape }}```

### 2021-07-23 07:48
结果想买的烧饼和包子都没有，豆泥馅的包子太甜了，，对，是豆泥，不是豆沙。。

### 2021-07-23 08:11
「悲喜都不自由」←《人间失格》后边其实还有几个短篇，这是其中一篇的人物台词；然而还有「表达「悲喜都不自由」的自由」。。

### 2021-07-23 10:02
Z-BlogPHP 的置顶逻辑果然很有问题，，然而要怎么改进呢。。

### 2021-07-23 10:49
所以说能够「认同自己」是否也是一种才能。。

### 2021-07-23 11:42
可能喵星人存在的意义就是「努力成为一只喵」，包括惹人生气的各种行为，也包括惹人生气后努力逃跑的举动，还包括下次仍然会犯始终如一。。

### 2021-07-23 15:12
点了这季的《白沙水族馆》，看介绍和开场第一感觉是《樱花任务》一类，然而还有超自然要素？？《樱花任务》也是前不久才补完，要不要看一部番果然契机很重要。

### 2021-07-24 13:41
\#书签 \#VSCode 插件 —— 插件入递增数字：`https://marketplace.visualstudio.com/items?itemName=albymor.increment-selection`

### 2021-07-24 18:01
sm.ms 不支持 webp 格式；

### 2021-07-24 19:20
所以果然早就注册过博客园。

### 2021-07-25 22:48
重装了系统，所以决定试下不装搜狗五笔而用下微软五笔，然后找到了 wubiLex 这个辅助设置工具；然后在发这条嘟时发现需要先设置话题`PubWord`快捷短语，在研究了一通回来后发现还是忘记了。。

### 2021-07-28 11:17 规则备忘
```xml
<rule name="/ vue_break" stopProcessing="false">
  <match url="^(tPre/[^/]+/[^/]+)" ignoreCase="false" />
  <action type="Rewrite" url="{R:1}?vue_break" />
</rule>
```
```conf
RewriteRule ^(tPre/[^/]+/[^/]+) $1?vue_break
```

### 2021-07-28 11:28 快速删除 node_modules
```bash
# 淘宝镜像
npm install -g cnpm --registry=https://registry.npm.taobao.org
# 安装rimraf
cnpm install -g rimraf
# 进入工作路径执行，Windows可将Git Bash注册到右键，
rimraf node_modules
```
