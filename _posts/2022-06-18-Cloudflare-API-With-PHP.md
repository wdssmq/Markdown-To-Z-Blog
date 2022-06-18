---
title: 「PHP」Cloudflare API 批量删除解析
date: 2022-06-18 11:24:10
tags:
 - PHP
 - 域名
 - DNS
categories:
 - 电脑网络
id: 767
alias: 20220321262
---

## 前言

为了绑定自定义域名到　Cloudflare Workers 再一次将域名解析托管到了 Cloudflare；

然而在导入解析记录时不知道为什么出现了一大堆，大概近 200 条了；

一条条删除太麻烦了就决定研究下 API 批量操作；

<!--more-->

推荐：

[「折腾」关于 2021 年末仍然没有完备的图床方案这件事\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20211225085.html "「折腾」关于 2021 年末仍然没有完备的图床方案这件事\_电脑网络\_沉冰浮水")

[「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100604351.html "「折腾」Caddy 简易入门教程\_电脑网络\_沉冰浮水")

[「折腾」Git Submodule 探究\_电脑网络\_沉冰浮水](https://www.wdssmq.com/post/20100710361.html "「折腾」Git Submodule 探究\_电脑网络\_沉冰浮水")

## 官方库和文档

cloudflare/cloudflare-php: PHP library for the Cloudflare v4 API：

[https://github.com/cloudflare/cloudflare-php](https://github.com/cloudflare/cloudflare-php "cloudflare/cloudflare-php: PHP library for the Cloudflare v4 API")

Cloudflare PHP API Binding – Cloudflare Help Center：

[https://support.cloudflare.com/hc/en-us/articles/115001661191](https://support.cloudflare.com/hc/en-us/articles/115001661191 "Cloudflare PHP API Binding – Cloudflare Help Center")

官方到是有 PHP 语言的 SDK，在其基础上封装了一个类方便使用；

这次这个东西和前不久折腾的 hexo 插件有一个共同点就是，它们的文档都让人痛苦；

然而过去和将来，也只能一次又一次的趟过这种痛苦，或者倒下吧。。

## 鉴权

API 令牌 | Cloudflare：[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens "API 令牌 | Cloudflare")

↑ 实际用到的是账号邮箱和「Global API Key」，有全部权限的样子，「API 令牌」则用于细化权限，还不太清楚代码中怎么用；


## 相对通用的 class 封装

```php
require __DIR__ . "/vendor/autoload.php";

use Cloudflare\API\Auth\APIKey;
use Cloudflare\API\Adapter\Guzzle;
use Cloudflare\API\Endpoints\User;
use Cloudflare\API\Endpoints\Zones;
use Cloudflare\API\Endpoints\DNS;

class CloudFlare
{
  public $errCode = 0;
  public $errMsg = '';
  // ----
  private $errInfos = array(
    0 => '没有错误',
    1 => '鉴权信息为空或错误 *'
  );
  private $options = array();
  private $oAPIKey = null;
  private $oAdapter = null;
  private $oUser = null;
  private $oZones = null;
  private $oDNS = null;
  // ----
  // 初始化
  public function __construct($options)
  {
    $this->options = $options;
    $bolOK = $this->checkOptions();
    if ($bolOK) {
      $this->initAPI();
    }
  }
  // 初始化用户基类
  public function initUser()
  {
    if ($this->oUser !== null) {
      return $this->oUser;
    }
    $this->oUser   = new User($this->oAdapter);
    return $this->oUser;
  }
  // 初始化域名基类
  public function initZones()
  {
    if ($this->oZones !== null) {
      return $this->oZones;
    }
    $this->oZones   = new Zones($this->oAdapter);
    return $this->oZones;
  }
  // 初始化 DNS 基类
  public function initDNS()
  {
    if ($this->oDNS !== null) {
      return $this->oDNS;
    }
    $this->oDNS   = new DNS($this->oAdapter);
    return $this->oDNS;
  }
  // 获取域名列表
  public function listZones()
  {
    $oZones = $this->initZones();
    return $oZones->listZones();
  }
  // 获取指定域名的 DNS 记录
  public function listRecords($zoneID)
  {
    $oDNS = $this->initDNS();
    return $oDNS->listRecords($zoneID);
  }
  // 删除 DNS 记录
  public function deleteRecord($zoneID, $recordID)
  {
    $oDNS = $this->initDNS();
    return $oDNS->deleteRecord($zoneID, $recordID);
  }
  // ----
  // 初始化 API
  private function initAPI()
  {
    if ($this->oAPIKey === null || $this->oAdapter === null) {
      $cf_email = $this->options['cf_email'];
      $cf_key = $this->options['cf_key'];
      $oAPIKey     = new APIKey($cf_email, $cf_key);
      $oAdapter = new Guzzle($oAPIKey);
      $this->oAPIKey = $oAPIKey;
      $this->oAdapter = $oAdapter;
    }
  }
  // 检查配置
  private function checkOptions()
  {
    foreach ($this->options as $key => $value) {
      if (empty($value)) {
        $this->errCode = 1;
        $this->errMsg = "配置项 {$key} 不能为空";
        return false;
      }
    }
    return true;
  }
}
```

## 上层封装

因为界面和配置项什么的还是 Z-BlogPHP 比较熟悉，另外也可以糊个插件上架；

然而我自己就是想清空一波 DNS 解析，这插件有什么其他用途也是很迷；

以下仅为使用示意，Z-BlogPHP 插件版要不要上架也是略纠结；

甚至想着把 DNSPod 啥的也弄到一个插件里，以及半成品的插件要不要纳入到 Git 里；

```php
// 初始
function CloudFlare_Init()
{
  global $zbp;
  // ----
  $cf_email = $zbp->Config('CloudFlare')->cf_email;
  $cf_key = $zbp->Config('CloudFlare')->cf_key;
  $cf_token = $zbp->Config('CloudFlare')->cf_token;
  // ----
  $options = array(
    'cf_email' => $cf_email,
    'cf_key' => $cf_key,
    'cf_token' => $cf_token,
  );
  // ----
  $cf = new CloudFlare($options);
  return $cf;
}

// 获取域名列表
function CloudFlare_ListDomins()
{
  $cf = CloudFlare_Init();
  if ($cf->errCode !== 0) {
    return "<td rolspan=\"3\">{$cf->errMsg}</td>";
  }
  $tpl = file_get_contents(mz_DNMng_Path('cf_dm_list'));
  $rltHTML = '';
  $listZones = $cf->listZones();
  foreach ($listZones->result as $zone) {
    $rltHTML .= $tpl;
    $rltHTML = str_replace('{id}', $zone->id, $rltHTML);
    $rltHTML = str_replace('{name}', $zone->name, $rltHTML);
    $rltHTML = str_replace('{status}', $zone->status, $rltHTML);
    $rltHTML = str_replace('{plan_name}', $zone->plan->name, $rltHTML);
  }
  return $rltHTML;
}

// 获取指定域名的 DNS 记录
function CloudFlare_ListRecords($zoneID)
{
  global $zbp;
  $cf = CloudFlare_Init();
  if ($cf->errCode !== 0) {
    return "<td rolspan=\"3\">{$cf->errMsg}</td>";
  }
  $tpl = file_get_contents(mz_DNMng_Path('cf_recd_list'));
  $csrfToken = $zbp->GetCSRFToken();
  $rltHTML = '';
  $listRecords = $cf->listRecords($zoneID);
  foreach ($listRecords->result as $record) {
    $rltHTML .= $tpl;
    $rltHTML = str_replace('{name}', $record->name, $rltHTML);
    $rltHTML = str_replace('{type}', $record->type, $rltHTML);
    $rltHTML = str_replace('{content}', $record->content, $rltHTML);
    $rltHTML = str_replace('{zone_id}', $record->zone_id, $rltHTML);
    $rltHTML = str_replace('{id}', $record->id, $rltHTML);
    $rltHTML = str_replace('{csrfToken}', $csrfToken, $rltHTML);
  }
  return $rltHTML;
}

// 删除 DNS 记录
function CloudFlare_DelRecord($zoneID, $recordID)
{
  $cf = CloudFlare_Init();
  if ($cf->errCode !== 0) {
    return false;
  }
  $rlt = $cf->deleteRecord($zoneID, $recordID);
  return $rlt;
}

// 清空 DNS 记录
function CloudFlare_ClearRecords($zoneID)
{
  $cf = CloudFlare_Init();
  if ($cf->errCode !== 0) {
    return false;
  }
  $listRecords = $cf->listRecords($zoneID);
  foreach ($listRecords->result as $record) {
    // $zoneName = $record->zone_name;
    $zoneID = $record->zone_id;
    $recordID = $record->id;
    $cf->deleteRecord($zoneID, $recordID);
  }
  return $cf->errCode === 0 ? true : false;
}
```
