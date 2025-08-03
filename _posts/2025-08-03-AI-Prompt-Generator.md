---
title: 「小代码」使用 YAML 配置拼接 AI 提示词，随机及条件语句
date: 2025-08-03 09:21:13
tags:
 - 小代码
 - Python
categories:
 - 电脑网络
id: 664
alias: 20230425779
---

### 工具简介

定义好 YAML 配置文件后，使用 Python 脚本处理生成 AI 提示词，支持随机和条件语句；

<!--more-->

### 工具类型

Python 脚本，需要有相应的使用能力；

### 使用方法

命令行执行，具体命令参数见项目内说明，支持交互式输入；

```bash
python prompt_generator.py ../examples/config.yaml -p demo

```

### 配置示例

就是简单的变量替换、随机和条件判断；

普通变量`{{variable}}`，涉及随机时使用`{{$variable}}`防止重新随机；

```yaml
- items:
  - name: base
    content: |
      女性，二次元少女

  - name: 动物类型
    content: |
      {{rnd(猫,兔子,)}}

  - name: 动物
    content: |
      {{if($动物类型):桌子上有{{$动物类型}}:}}

  - name: 头发
    content: |
      {{rnd(黑,白,红,蓝)}}色头发

- prompts:
  - name: demo
    content: |
      {{base}}，坐在椅子上，{{头发}}，{{动物}}

```

### 项目地址


> wdssmq/AI-Prompt-Generator: 一个基于 YAML 配置的 AI 提示词生成工具，支持变量替换和随机选择功能。
>
> [https://github.com/wdssmq/AI-Prompt-Generator](https://github.com/wdssmq/AI-Prompt-Generator "wdssmq/AI-Prompt-Generator: 一个基于 YAML 配置的 AI 提示词生成工具，支持变量替换和随机选择功能。")
