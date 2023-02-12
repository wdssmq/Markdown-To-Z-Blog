---
title: 「折腾」Docker + pipenv 运行 Python 项目
date: 2023-02-12 22:59:16
tags:
 - Python
 - Docker
 - 折腾
categories:
 - 电脑网络
id: 797
alias: 20220531665
---

### 前言

「笔记」和「操作手册」应该怎么区分呢？

<!--more-->

### 正文

有一些使用 Github Actions 跑 Python 的项目，其中一种方案是使用 Docker + pipenv，后者是 Python 的包管理工具，类似于 npm；

本文将记录如何在自建 Linux 环境使用该方案……

```bash
# 克隆项目
GIT_PATH=~/Git
git clone git@github.com:VaultVulp/action-pipenv.git $GIT_PATH/action-pipenv

# 构建 Docker 镜像
cd $GIT_PATH/action-pipenv
docker build -t py-pipenv .
```

· 执行 `mkdir -p ~/test/py-pipenv` 创建测试目录，然后在该目录下创建`main.py`文件，内容如下：

```python
import json
import feedparser
import pprint

# 读取 rss
rss_list = feedparser.parse('https://www.wdssmq.com/feed.php')
# 提取标题和链接
rlt_list = [{'title': entry['title'], 'link':entry['link']} for entry in rss_list['entries']]
# 打印结果
pprint.pprint(rlt_list)
# 保存为 json 文件
with open('output.json', 'w') as f:
    json.dump(rlt_list, f)
```

· 在该目录下创建`Pipfile`文件，内容如下：

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[scripts]
main = "python main.py"

[packages]
feedparser = "*"
```

```bash
# 运行之构建虚拟环境（virtualenv）
PY_DIR=~/test/py-pipenv
ENVS_DIR=${PY_DIR}/virtualenvs
docker run --name py-run \
    --rm \
    --workdir /app \
    -v ${PY_DIR}:/app \
    -v ${ENVS_DIR}/:/root/.local/share/virtualenvs \
    py-pipenv \
    "install -d"
```

· 在`${PY_DIR}`内会生成`virtualenvs`目录，其中包含了虚拟环境的相关文件，在 Pipfile 内依赖项不变的情况下只需要执行一次构建；

```bash
# 运行实际代码
PY_DIR=~/test/py-pipenv
ENVS_DIR=${PY_DIR}/virtualenvs
docker run --name py-run \
    --rm \
    --workdir /app \
    -v ${PY_DIR}:/app \
    -v ${ENVS_DIR}/:/root/.local/share/virtualenvs \
    py-pipenv \
    "run main"
```

· 相当于执行了`pipenv run main`，在`${PY_DIR}`内会生成`output.json`文件；

### 补充

- `--rm` 参数表示运行完毕后自动删除容器；
- `--workdir` 指定工作目录；
- `-v` 挂载目录到容器内；
- `py-pipenv` 是前边构建镜像指定的名称；
- `"install -d"` 或 `"run main"` 将作为参数传递给容器内的 `pipenv` 命令；

### 相关链接

> 「小事」Python 的 Docker 镜像更新了一波\_杂七杂八\_沉冰浮水：
>
> [https://www.wdssmq.com/post/20210820542.html](https://www.wdssmq.com/post/20210820542.html "「小事」Python 的 Docker 镜像更新了一波\_杂七杂八\_沉冰浮水")

> VaultVulp/action-pipenv: Use pipenv commands in your GitHub Actions Workflow：
>
> [https://github.com/VaultVulp/action-pipenv](https://github.com/VaultVulp/action-pipenv "VaultVulp/action-pipenv: Use pipenv commands in your GitHub Actions Workflow")
