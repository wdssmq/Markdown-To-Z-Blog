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

以及，好像在用 VSCode 之前已经用了很久 TortoiseGit 了，所以 VSCode 内置的 Git 相关功能都没怎么了解，`ctrl + shift + g`赛高。。。

部分键为自定义，并且需要删掉冲突的定义；

几个留空的是没有默认项又没决定好自定义成啥；

**请根据命令项查看实际绑定键或自定义；**

| 快捷键            | 操作                         | 命令                                             |
| ----------------- | ---------------------------- | ------------------------------------------------ |
| ctrl + b          | 切换侧栏显隐                 | workbench.action.toggleSidebarVisibility         |
| ctrl + d          | 复制当前行（向下）           | editor.action.copyLinesDownAction                |
| ctrl + e          | 展开 emmet 缩写              | editor.emmet.action.expandAbbreviation           |
| ctrl + q          | 切换注释                     | editor.action.commentLine                        |
| ctrl + l          | 选中当前行                   | expandLineSelection                              |
| ctrl + shift + ↑  | 选中文本 - 向上一行          | cursorUpSelect                                   |
| ctrl + shift + ↓  | 选中文本 - 向下一行          | cursorDownSelect                                 |
| ctrl + ←          | 光标移动 - 单词左侧为界      | cursorWordLeft                                   |
| ctrl + shift + ←  | 选中文本 - 同上              | cursorWordLeftSelect                             |
|                   | 光标移动 - 词首或驼峰        | cursorWordPartLeft                               |
|                   | 选中文本 - 同上              | cursorWordPartLeftSelect                         |
| ctrl + →          | 光标移动 - 单词右侧为界      | cursorWordEndRight                               |
| ctrl + shift + →  | 选中文本 - 同上              | cursorWordEndRightSelect                         |
|                   | 光标移动 - 词尾或驼峰        | cursorWordPartRight                              |
|                   | 选中文本 - 同上              | cursorWordPartRightSelect                        |
| shift + alt + ←   | 收起选择                     | editor.action.smartSelect.shrink                 |
| shift + alt + →   | 展开选择                     | editor.action.smartSelect.expand                 |
| ctrl + p          | 最近打开过的单文件           | workbench.action.quickOpen                       |
| ctrl + r          | 最近打过的工作区或文件夹     | workbench.action.openRecent                      |
| ctrl + shift + o  | 转到编辑器中的符号           | workbench.action.gotoSymbol                      |
| ctrl + alt + b    | 格式化代码/文档              | editor.action.formatDocument                     |
| ctrl + alt + ↑    | 同一列的上一行添加光标       | editor.action.insertCursorAbove                  |
| ctrl + alt + ↓    | 同一列的下一行添加光标       | editor.action.insertCursorBelow                  |
| ctrl + shift + p  | 命令面板                     | workbench.action.showCommands                    |
| ctrl + shift + x  | 扩展/插件 查看               | workbench.view.extensions                        |
| ctrl + shift + g  | 源代码管理（Git）            | workbench.view.scm                               |
| ctrl + shfit + e  | 工作区/文件夹查看            | workbench.view.explorer                          |
| ctrl + shift + k  | 删除当前行                   | 感觉 ctrl + l，然后 del 会更安全？               |
| ctrl + shift + l  | 将全部查找匹配项添加到选择   | addCursorsAtSearchResults                        |
| alt + d           | 将下一个查找匹配项添加到选择 | editor.action.addSelectionToNextFindMatch        |
| alt + ↑           | 向上移动行                   | editor.action.moveLinesUpAction                  |
| alt + ↓           | 向上移动行                   | editor.action.moveLinesDownAction                |
| ctrl + k z        | 禅模式                       | workbench.action.toggleZenMode                   |
| ctrl + k m        | 语言模式                     | workbench.action.editor.changeLanguageMode       |
| ctrl + k k        | 快捷方式设置                 | workbench.action.openGlobalKeybindings           |
| ctrl + k u        | 关闭已经保存的编辑器页       | workbench.action.closeUnmodifiedEditors          |
| ctrl + k o        | 在新窗口打开活动文件         | workbench.action.files.showOpenedFileInNewWindow |
| ctrl + k ctrl + l | 转为小写                     | editor.action.transformToLowercase               |
| ctrl + k ctrl + u | 转为大写                     | editor.action.transformToUppercase               |

<!--1642-->
