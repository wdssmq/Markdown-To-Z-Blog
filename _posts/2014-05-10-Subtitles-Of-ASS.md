---
title: 【备忘】ASS 字幕格式简要
date: 2014-05-10 09:37:05
tags:
- 字幕
- 电影
- 备忘
categories:
- 杂七杂八
id: 2224
alias: 20140510891
---

常见的几种字幕：

1、`srt`：全称 SubRip Text，一句时间代码+一句字幕，体积小，可以用记事本打开编辑。

<!-- more -->

2、`sub+idx`：图形字幕，每条字幕就是一张图片，idx 文件为时间索引，可以用附注的 OCR 工具转换为 srt 字幕。

3、`SSA`：SubStation Alpha，目前版本为 v4.00；

4、`ASS`：Advanced SubStation Alpha，相当于 SSA v4.00+。

`SSA/ASS` 脚本可以更方便的给字幕（尤其是双语字幕）设置文本特效。

------------------

2022-08-26：字幕编辑现在推荐这个：[https://github.com/SubtitleEdit/subtitleedit/releases](https://github.com/SubtitleEdit/subtitleedit/releases "Releases · SubtitleEdit/subtitleedit")

------------------

使用文本编辑器打开一个 ASS 字幕（SrtEdit v6.3 生成）「下载: [StrEdit - 百度网盘](http://url.cn/HVAs87 "StrEdit - 百度网盘")」

```ini
[Script Info]
;SrtEdit 6.3.2012.1001
;Copyright(C) 2005-2012 Yuan Weiguo
;注释信息，标为可选的均可为空

Title: （可选）字幕的标题、描述。例：钟楼怪人双语字幕
Original Script: （可选）脚本原作者
Original Translation: （可选）翻译人员
Original Timing: （可选）时间轴
Original Editing: （可选）参与编辑校对的人员
Script Updated By: （可选）优化、二次编辑人员
Update Details: （可选）更新说明。如：修正错别字及部分翻译错误，字幕样式调整。
Synch Point: （可选）从哪一个时间点开始进行字幕加载播放
ScriptType: v4.00+
Collisions: Normal
PlayResX: 384
PlayResY: 288
Timer: 100.0000
WrapStyle: 0
ScaledBorderAndShadow: no

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: eng,Microsoft YaHei,12,&H003CF1F3,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,1,2,0,0,2,1
Style: Default,Microsoft YaHei,18,&H00E0E0E0,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,1,2,0,0,15,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 1,0:00:57.33,0:01:00.53,Default,,0000,0000,0000,,圣母院的钟声
Dialogue: 1,0:01:00.60,0:01:03.87,Default,,0000,0000,0000,,敲醒了巴黎的晨曦
Dialogue: 1,0:01:03.94,0:01:07.24,Default,,0000,0000,0000,,渔夫捕着鱼\n面包师烤着面包
Dialogue: 1,0:01:07.31,0:01:10.30,Default,,0000,0000,0000,,圣母院的钟声响起
Dialogue: 1,0:01:10.38,0:01:13.61,Default,,0000,0000,0000,,大钟如雷鸣般响彻云霄

Dialogue: 0,0:00:57.33,0:01:00.53,eng,,0000,0000,0000,,[ Man ]\nMorning in Paris\nThe city awakes
Dialogue: 0,0:01:00.60,0:01:03.87,eng,,0000,0000,0000,,To the bells\nof Notre Dame
Dialogue: 0,0:01:03.94,0:01:07.24,eng,,0000,0000,0000,,The fisherman fishes\nThe baker man bakes
Dialogue: 0,0:01:07.31,0:01:10.30,eng,,0000,0000,0000,,To the bells\nof Notre Dame
Dialogue: 0,0:01:10.38,0:01:13.61,eng,,0000,0000,0000,,- To the big bells\nas loud as the thunder\n- [ Bells Tolling ]
```

**`[Script Info]`区域说明**

`ScriptType: v4.00+`

样式版本声明；

`Collisions: Normal`

当字幕时间重叠时, 前后字幕的堆叠方式 ——

- `Normal`：后一条字幕出现在前一条字幕的上方；
- `Reverse`：前一条字幕往上移动给后一条字幕让位。

注：经测试好像无效的样子，建议通过设置字幕下边距实现字幕相对位置的控制；

`PlayResX: 384 | PlayResY: 288`

视频尺寸参考标准，下边字号、边距等属性指基于此处设置将画面等分后所取的份数。建议与视频宽高比一致，然后值越大控制越精确；

`Timer: 100.0000`

字幕加载的速度调整；

`WrapStyle: 0`

字幕超出屏幕宽度时默认的换行方式：

- `0`: 智能换行，行分得较平均，上面的行较长；
- `1`: 一行结束后从行尾的词分行；
- `2`: 不换行，此模式下只有\\n, \\N 才换行；
- `3`: 与模式 0 相同, 但下面的行分得比较长。

`ScaledBorderAndShadow: no`

指定边框宽度与阴影深度是否随着视频分辨率等比例缩放 ——

- 当取值为`No`时, 边框宽度与阴影深度完全按照指定的像素数显示；
- 当取值为`Yes`时, 边框宽度与阴影深度随着实际视频的分辨率同等比例缩放；

**`[V4+ Styles]`区域说明：**

第一行声明要定义的属性字段，之后每一行定义相应的属性值，英文逗号分隔；

`Name`: 样式名称，`[Events]`区域内的具体字幕可通过设置`Style`属性调用相匹配的样式定义；

`Fontname`: 字体名称；

`Fontsize`: 字号大小；

`PrimaryColour`: 主体颜色 —— 颜色格式为`&HAABBGGRR`，十六进制，00-FF，alpha 蓝绿红。alpha 指透明度，00 为不透明。下同；

`SecondaryColour`: 次要颜色 —— 卡拉 OK 效果使用；

`OutlineColor`: 边框颜色 —— SSA 中为 TertiaryColour；

`BackColour`: 阴影颜色；

`Bold`: 粗体 —— `0`关闭，`1`开启。`Italic`,`Underline`,`Strikeout`相同；

`Italic`: 斜体；

`Underline`: 下划线；

`Strikeout`: 删除线；

`ScaleX`: 横向缩放 —— 单位是 `%`，默认为`100`，即正常大小；

`ScaleY`: 纵向缩放；

`Spacing`: 字间距；

`Angle`: 旋转 —— `0`到`360`的角度值，正值为逆时针，负值为顺时针；

`BorderStyle`: 边框样式 —— `1`=边框+阴影, `3`=纯色背景. 当值为`3`时, 文字下方为轮廓颜色的背景, 最下方为阴影颜色背景；

`Outline`: 边框宽度；

`Shadow`: 阴影距离；

`Alignment`: 对齐方式 —— 取值`1`到`9`，对应数字小键盘上的位置；

注：SSA 中 `1`, `2`, `3`加上`4`后字幕出现在屏幕上方； `1`, `2`, `3`加上`8`后字幕出现在屏幕中间；

`MarginL`: 字幕距左边的距离，右对齐时无效；

`MarginR`: 字幕距右边的距离，左对齐时无效；

`MarginV`: 字幕高度 —— 下对齐时表示到底部的距离-------上对齐时表示到顶部的距离------中对齐时无效；

`Encoding`: 字符集或编码方式 —— `1`为默认，`0`为 ANSI，`134`为简体中文，`136`为繁体中文。当文件为非 UNICODE 类型编码时, 该值对字幕的显示起作用；

附注：

\--[IdxSubOcr](https://www.cnblogs.com/stronghorse/p/14594337.html "IdxSubOcr")--OCR 引擎为 Microsoft Office Document Imaging (MODI)，MODI 的安装请仔细阅读软件说明，支持英文、简体中文、繁体中文、日文。另对 OCR 出来的字幕进行校对也是很恐怖的，感谢所有制作出优秀字幕的童鞋。

\--[MKV 内置字幕提取/字幕编辑工具推荐](https://www.wdssmq.com/post/20120727734.html "MKV 内置字幕提取/字幕编辑工具推荐")--

