---
title: 「VSCode」PHP 跨文件夹函数定义提示
tags:
- VSCode
- 代码
- PHP
categories:
- 电脑网络
id: 3103
alias: 20200930532
---

2021-09-05：

> Undefined function 'CheckIsRefererValid'.intelephense(1010)

一直以来，即使设置了`intelephense.environment.includePaths`，也时不时会出现函数未定义的提示，一个可能有关的原因是文件路径的分隔符不统一；

可以尝试将`intelephense.environment.includePaths`和`folders`中的项目路径格式统一改为`"..\\..\\..\\zb_system"`或`"../../../zb_system"`中的一种，然后关掉窗口重新打开「*.code-workspace」工作区；

<!--more-->

试了几个项目，然而并不能明确是复现。。也是超纠结。。

---------------

首先语法提示和检测用的是这个插件：

> PHP Intelephense - Visual Studio Marketplace
>
> <a href="https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client" target="_blank" title="PHP Intelephense - Visual Studio Marketplace">https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client</a>

主要用来写 Z-Blog 的插件，「*.code-workspace」文件如下：

```json
{
  "folders": [
    {
      "path": "."
    },
    {
      "path": "../../../zb_system"
    }
  ],
  "settings": {
    "intelephense.environment.includePaths": [
      "../../../zb_system"
    ]
  }
}
```

配置中已经针对当前工作区设置了`intelephense.environment.includePaths`属性，如果没有该设置，那么当在主题或插件中使用`zb_system`文件夹中的函数中会提示未定义。

`Undefined function 'AddNameInString'.intelephense(1010)`

--------

方案来自：

Allow folders to be included outside of workspace · Issue \#253 · bmewburn/vscode-intelephense

<a href="https://github.com/bmewburn/vscode-intelephense/issues/253" target="_blank" title="Allow folders to be included outside of workspace · Issue \#253 · bmewburn/vscode-intelephense">https://github.com/bmewburn/vscode-intelephense/issues/253</a>

<!--3103-->
