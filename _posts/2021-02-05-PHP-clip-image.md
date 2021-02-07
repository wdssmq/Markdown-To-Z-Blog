---
title: 关于 Z-BlogPHP 1.7 缩略图的一些记录
tags:
- PHP
- Z-BlogPHP
- Z-Blog
- 折腾
categories:
- 未分类
---

Z-BlogPHP 1.7 将会提供一个`Thumb`基础类，本身只实现从「原图」到「缩略图」的转换和保存，简单说就是自动帮你变小。

生成路径为`zb_users/cache/thumbs/`。

<!--more-->

### 主题内的使用示例

```php
function ActivePlugin_acgME()
{
  Add_Filter_Plugin('Filter_Plugin_ViewList_Template', 'acgME_Main');
  Add_Filter_Plugin('Filter_Plugin_Post_Thumbs', 'acgME_Thumbs');
  Add_Filter_Plugin('Filter_Plugin_Zbp_BuildTemplate', 'acgME_BuidTemp');
}
function acgME_Main(&$template)
{
  global $zbp;
  // 遍历文章设置图片
  if ($articles = $template->GetTags('articles')) {
    foreach ($articles as $article) {
      acgME_SetIMG($article);
    }
  }
  // else if ($article = $template->GetTags('article')) {
  //   acgME_SetIMG($article);
  // }
}
// 这部分还会有改动
function acgME_Thumbs($article, &$all_images, $width, $height, $count, $clip)
{
  $rndNum = $article->ID % 19 + 1;
  $rndImg = acgME_Path("v-noimg", "host") . $rndNum . ".jpg";
  // $all_images为文章正文内的图片，追加一张保证能拿到图
  $all_images[] = $rndImg;
}
// 通过封装函数赋值给属性用于调用
function acgME_SetIMG(&$article)
{
  if (!isset($article->Img_640x360)) {
    $article->Img_640x360 = $article->Thumbs(640, 360, 1, false)[0];
    // ↑此处获取值无法保存，保存请用Metas
  }
}
// 用于幻灯片
function acgME_BuidTemp(&$templates)
{
  global $zbp;
  // 幻灯片
  $templates['n-slide'] = "";
  if (!$zbp->template->HasTemplate("m-slide")) {
    return;
  }
  $uFile = acgME_Path("u-slide");
  if (!is_file($uFile)) {
    return;
  }
  // 核心部分
  $slides = json_decode(file_get_contents($uFile));
  foreach ($slides as $key => &$item) {
    $item->Img_142x80 = Thumb::Thumbs([$item->Img], 142, 80, 1, false)[0];
    $item->Img_647x404 = Thumb::Thumbs([$item->Img], 647, 404, 1, false)[0];
  }
  $zbp->template->SetTags('slides', $slides);
  $templates['n-slide'] = $zbp->template->Output("m-slide");
  $templates['n-slide'] .= '{php}$footer .= \'<script src="' . $zbp->host . 'zb_users/theme/acgME/script/swiper-3.4.2.jquery.min.js"></script>\'{/php}';
  $templates['n-slide'] .= '{php}$footer .= \'<script src="' . $zbp->host . 'zb_users/theme/acgME/script/swiper-act.js"></script>\'{/php}';
}
```

模板内调用：

```html
<div class="post-img"><img src="{$article.Img_640x360}" alt="{$article.Title}"></div>
```

### 关于图片裁切部分的代码笔记

```php
  public function handle()
  {
    if ($this->shouldClip) {
      // 原图：宽/高
      $src_scale = ($this->srcWidth / $this->srcHeight);
      // 新图：宽/高
      $dst_scale = ($this->dstWidth / $this->dstHeight);

      // 高度：原/新
      $h_scale = ($this->srcHeight / $this->dstHeight);
      // 宽度：原/新
      $w_scale = ($this->srcWidth / $this->dstWidth);

      // 原图需要裁切至的目标宽度（横向）
      $w_des = ($this->dstWidth * $h_scale);
      // 原图需要裁切至的目标高度（纵向）
      $h_des = ($this->dstHeight * $w_scale);

      // 新旧比例变化判断裁切方向
      if ($src_scale >= $dst_scale) {
        // 24:15 // 原图 8:5
        // 12:10 // 目标 6:5
        // x:15 = 12:10
        // x = 18 = 12*(15/10) = 15*(12/10) // $w_des
        // 原图高度不变，宽度裁切至 $w_des
        $dst_widthx = (($this->srcWidth - $w_des) / 2); // ((24-18)/2)
        $this->clip($dst_widthx, 0, $w_des, $this->srcHeight);
        // 先将原图裁切至 18:15，再缩放至 12:10
        $this->zoom($this->dstWidth, $this->dstHeight);
      } else {
        // 24:15 // 原图 8:5
        // 40:20 // 目标 10:5
        // 24:y = 40:20
        // y = 12 = 20*(24/40) = 24/(40/20) // $h_des
        // 原图宽度不变，高度裁切至 $h_des
        $dst_heighty = (($this->srcHeight - $h_des) / 2); // ((15-12)/2)
        $this->clip(0, $dst_heighty, $this->srcWidth, $h_des);
        // 理论上，当目标尺寸大于原图尺寸时，这里可以选择返回 24:12 的图片，即上一步裁切好的尺寸
        $this->zoom($this->dstWidth, $this->dstHeight); // 这里实际会返回 24:15
      }
    } else {
      $this->zoom($this->dstWidth);
    }
    $this->save();
    imagedestroy($this->srcRes);
  }
```

### 其他

【备忘】访止别人用 iframe 调用你的页面\_电脑网络\_沉冰浮水：

[https://www.wdssmq.com/post/20160730633.html](https://www.wdssmq.com/post/20160730633.html "【备忘】访止别人用 iframe 调用你的页面\_电脑网络\_沉冰浮水")
