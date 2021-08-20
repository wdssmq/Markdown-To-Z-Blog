---
title: 【VSCode】快捷键备忘
tags:
- 编辑器,VSCode,备忘
categories:
- 电脑网络
id: 1642
alias: 20130525410
csdn: https://blog.csdn.net/qq_15022221/article/details/119830398
jianshu: https://www.jianshu.com/p/d69630634042
cdblogs: https://www.cnblogs.com/wdssmq/p/15167982.html
---

[建议]查看 >> 外观 >> 取消`显示活动栏`的勾选 ← 基本上记住`资源管理器`、`全局搜索`、`扩展`的快捷键后就不需要这个了，可以节省显示的空间。

[可选]查看 >> 外观 >> 取消`显示菜单栏`的勾选 ← 因为是和标题栏在一行，所以并不会省空间，但是干净点也算不错，按单按 alt 可以临时显示。

<!--more-->

好吧，传说中的`禅模式`也就是关掉`活动栏`的快捷键。。

以及，好像在用 VSCode 之前已经用了很久 TortoiseGit 了，所以 VSCode 内置的 Git 相关功能都没怎么了解，`ctrl+shift+g`赛高。。。

部分键为自定义，并且需要删掉冲突的定义。

| 快捷键            | 操作                         | 命令                                             |
| ----------------- | ---------------------------- | ------------------------------------------------ |
| ctrl + b          | 切换侧栏显隐                 | workbench.action.toggleSidebarVisibility         |
| ctrl + d          | 复制当前行                   | editor.action.copyLinesDownAction                |
| ctrl + e          | 展开 emmet 缩写              | editor.emmet.action.expandAbbreviation           |
| ctrl + q          | 切换注释                     | editor.action.commentLine                        |
| ctrl + l          | 选中当前行                   | expandLineSelection                              |
| ctrl + p          | 最近文件                     | workbench.action.quickOpen                       |
| ctrl + alt + b    | 格式化代码/文档              | editor.action.formatDocument                     |
| ctrl + shift + o  | 转到编辑器中的符号           | workbench.action.gotoSymbol                      |
| ctrl + shift + p  | 命令面板                     |                                                  |
| ctrl + shift + x  | 扩展/插件 查看               |                                                  |
| ctrl + shift + g  | 源代码管理（Git）            |                                                  |
| ctrl + shfit + e  | 资源管理器                   |                                                  |
| ctrl + shift + k  | 删除当前行                   | 感觉 ctrl + l，然后 del 会更安全？               |
| alt + d           | 将下一个查找匹配项添加到选择 | editor.action.addSelectionToNextFindMatch        |
| alt + up          | 向上移动行                   | editor.action.moveLinesUpAction                  |
| alt + down        | 向上移动行                   | editor.action.moveLinesDownAction                |
| ctrl + k z        | 禅模式                       |                                                  |
| ctrl + k m        | 语言模式                     |                                                  |
| ctrl + k k        | 快捷方式设置                 | workbench.action.openGlobalKeybindings           |
| ctrl + k u        | 关闭已经保存的编辑器页       | workbench.action.closeUnmodifiedEditors          |
| ctrl + k o        | 在新窗口打开活动文件         | workbench.action.files.showOpenedFileInNewWindow |
| ctrl + k ctrl + l | 转为小写                     | editor.action.transformToLowercase               |
| ctrl + k ctrl + u | 转为大写                     | editor.action.transformToUppercase               |

<!--1642-->
