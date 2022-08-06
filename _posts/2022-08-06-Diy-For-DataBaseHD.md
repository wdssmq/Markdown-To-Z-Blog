---
title: 「Z-BlogPHP」数据库透析插件 DIY 演示
date: 2022-08-06 13:44:20
tags:
 - Z-BlogPHP
 - 数据库
 - 折腾
categories:
 - 电脑网络
id: 3120
alias: 20220806158
---

感觉自己做很多事都是靠感觉上想做的那种感觉.jpg

<!--more-->

> 数据库透析【基础依赖】 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=20812](https://app.zblogcn.com/?id=20812 "数据库透析【基础依赖】 - Z-Blog 应用中心")

↑ 这个插件的功能描述就是「取出数据，处理后存回去」，适用于一些不适合直接用 SQL 实现的修改管理；

插件本身只是将待操作数据的遍历读取进行了封装，具体修改需要另行注册调用函数来实现；

为此我写了另一个插件——

> 数据库透析【功能定制】 - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=21305](https://app.zblogcn.com/?id=21305 "数据库透析【功能定制】 - Z-Blog 应用中心")

↑ 本质上仍然是把一些东西先写好，然后用一个可定制的 `/usr/xxx.php` 来实现具体的用户需求，而不是为每种用户需求创建维护一个完整的插件；「此插件收费，可根据你的需求实现相应数据修改功能」

其实更早之前我已经写过一个「将不特定功能塞进一个插件」的插件——

> DIY Something - Z-Blog 应用中心：
>
> [https://app.zblogcn.com/?id=1961](https://app.zblogcn.com/?id=1961 "DIY Something - Z-Blog 应用中心")

↑ 同样可以配合「数据库透析【基础依赖】」插件来实现数据库批量操作；

- 按说明在`/zb_users/plugin/diySth/usr/`内创建一个文件夹`DiyForDataBaseHD`；
- 通过刷新「管理页」自动创建内部文件，会同时生成 CSS、JS 文件，不用理会；
- `DiyForDataBaseHD.php`内写入下边内容，通过刷新「`diySth`插件管理页」加载功能；
- 换到「数据库透析【基础依赖】」的管理页，应该就能看到添加的功能按钮；

```php
<?php
// ----
// DiyForDataBaseHD_Filter
Add_Filter_Plugin('Filter_Plugin_Admin_Header', 'DiyForDataBaseHD_AddHook');

// ----
// DiyForDataBaseHD_Function
function DiyForDataBaseHD_AddHook()
{
  global $zbp;
  $fnList = $zbp->Config('DataBaseHD')->fnList;
  $fnList[] = array("fn" => "DiyForDataBaseHD_UpAlias", "mod" => "Post", "name" => "另名规范");
  $zbp->Config('DataBaseHD')->fnList = $fnList;
}

// 历史原因，一些文章的别名长度只有 10 位，对其筛选补一位
function DiyForDataBaseHD_UpAlias(&$post, $csrfToken = "")
{
  $tpl = "<p style='color:-color-;'>-id- 丨 -url- 丨 -oldHash- 丨 -newHash- | -Save- | 「-edit-」「-del-」</p>\n";

  $arrData = array();
  $arrData["-color-"] = "-black-";
  $arrData["-id-"] = $post->ID;
  $arrData["-url-"] = DataBaseHD_DIY_a($post->Url, $post->Title);
  $arrData["-oldHash-"] = crc32($post->Content);

  // 编辑或删除按钮
  $arrData["-edit-"] = "<a class=\"style-visited\" title=\"{$post->Title}\" target=\"_blank\" href='../../../zb_system/admin/edit.php?act=ArticleEdt&id={$post->ID}'>编辑</a>";
  // $arrData["-del-"] = "<a class=\"style-visited\" title=\"{$post->Title}\" target=\"_blank\" onclick=\"return window.confirm('即将删除「{$post->Title}」，请确认！');\" href=\"../../../zb_system/cmd.php?act=ArticleDel&id={$post->ID}&csrfToken={$csrfToken}\">删除</a>";

  // 主要功能代码 ↓

  $intDefLen = strlen("20220806158") - 1;

  // 跳过不符合条件的文章
  if (strlen($post->Alias) !== $intDefLen || !is_numeric($post->Alias)) {
    return;
  }
  // 更新别名
  $post->Alias = $post->Alias . "4";
  $bolRlt = $post->Save();
  // 更新链接
  $arrData["-url-"] = DataBaseHD_DIY_a($post->Url, $post->Title);
  // 保存操作的结果
  $arrData["-Save-"] = $bolRlt ? "保存成功" : "保存失败";

  // 主要功能代码 ↑

  echo strtr($tpl, $arrData);
}

```
