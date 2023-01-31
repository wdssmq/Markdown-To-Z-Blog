---
title: 「折腾」GitHub Actions 如何提取推送的 Tag
date: 2023-01-31 15:25:41
tags:
 - GitHub
 - 备忘
 - 折腾
categories:
 - 电脑网络
id: 625
alias: 20220706871
---

使用 GitHub Actions 也有近两年了，然后今天发现了两个警告信息；

<!--more-->

> 今天折腾的项目是这个：[wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」](https://github.com/wdssmq/rollup-plugin-monkey "wdssmq/rollup-plugin-monkey: 使用 rollup 开发「GM\_脚本」")

-------------

> Node.js 12 actions are deprecated. Please update the following actions to use Node.js 16: actions/checkout@v2. For more information see: https://github.blog/changelog/2022-09-22-github-actions-all-actions-will-begin-running-on-node16-instead-of-node12/.

↑ 这个好解决，`actions/checkout@v2`更新为`actions/checkout@v3`就好；

> The `set-output` command is deprecated and will be disabled soon. Please upgrade to using Environment Files. For more information see: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/

↑ 这个感觉需要研究一下，所以在此记录下，虽然实际发现只是照新的写法改一句就好……

工作流配置中的主要步骤如下，完整的配置文件见文末链接：

```yaml
    steps:
      # Checkout
      - name: Checkout
        uses: actions/checkout@v3
      # Build Release
      - name: Copy && Gen ZIP
        env:
          PUB_NAME: ${{ env.PUB_NAME }}
        run: |
          # 这里用来生成 ${PUB_NAME}.tar.gz 文件
      # Get Tag For Release
      - name: Get Tag
        id: get_tag
        env:
          REF: ${{ github.ref }} # e.g. refs/tags/v1.0.0
        run: |
          TAG=${REF/refs\/tags\/v}
          echo "::set-output name=tag::${TAG}"
      # Publish Release
      - name: Publish Release
        id: release
        uses: softprops/action-gh-release@v1
        env:
          TAG: ${{ steps.get_tag.outputs.tag }} # 获取上一步截取到的版本号，既 1.0.0
        with:
          name: ${{ env.PUB_NAME }} Build ${{ env.TAG }}
          body: ${{ env.PUB_NAME }} Build ${{ env.TAG }} Release.
          files: ${{ env.PUB_NAME }}.tar.gz
```

功能概述为，在每次打 Tag 的时候，自动构建并发布 Release，同时提取 Tag 作为 Release 的版本号；

所以其中用于提取 Tag 的步骤为：

```yaml
      # Get Tag For Release
      - name: Get Tag
        id: get_tag
        env:
          REF: ${{ github.ref }} # e.g. refs/tags/v1.0.0
        run: |
          TAG=${REF/refs\/tags\/v}
          echo "::set-output name=tag::${TAG}"
```

其中`TAG=${REF/refs\/tags\/v}`将变量`REF`中指定部分替换为空，然后将结果赋值给`TAG`，`${TAG}`内容既为`1.0.0`；

只是这个变量只在当前`run`区块内有效，需要将其导出以便后续步骤使用；

旧的导出命令如上，只是这种写法被废弃了……

↓ 新的写法：

```yaml
      # Get Tag For Release
      - name: Get Tag
        id: get_tag
        env:
          REF: ${{ github.ref }} # e.g. refs/tags/v1.0.0
        run: |
          TAG=${REF/refs\/tags\/v}
          echo "tag=${TAG}" >> $GITHUB_OUTPUT
```

-----

官方文档：[Setting an output parameter](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter "Setting an output parameter")

中文文档：[设置输出参数](https://docs.github.com/zh/actions/using-workflows/workflow-commands-for-github-actions#%E8%AE%BE%E7%BD%AE%E8%BE%93%E5%87%BA%E5%8F%82%E6%95%B0 "设置输出参数")

完整的工作流配置文件：[wdssmq/rollup-plugin-monkey/blob/main/.github/workflows/push_def.yml](https://github.com/wdssmq/rollup-plugin-monkey/blob/main/.github/workflows/push_def.yml "wdssmq/rollup-plugin-monkey/blob/main/.github/workflows/push_def.yml")

GitHub Actions 运行结果（旧）：[wdssmq/rollup-plugin-monkey/actions/runs/4051596042](https://github.com/wdssmq/rollup-plugin-monkey/actions/runs/4051596042 "wdssmq/rollup-plugin-monkey/actions/runs/4051596042")
