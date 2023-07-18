""" Markdown 文件相关操作 """
import os
import frontmatter
import inspect

from bin.base import fnEmpty, fnLog, fnGetTimeStr, fnGetFileTime

# pylint: disable=global-statement, consider-using-f-string

# 全局变量
config_info = {}
logs_info = {}
debug_info = {}


def md_init(config, logs, debug):
    """ 初始化 """
    global config_info, logs_info, debug_info

    config_info = config
    logs_info = logs
    debug_info = debug


def get_md_list(dir_path):
    """ 获取特定目录的 markdown 文件列表 """
    # 绝对路径列表
    md_list = []
    dirs = os.listdir(dir_path)
    for i in dirs:
        if i in {".gitkeep", "1970-01-01-empty.md"}:
            continue
        if os.path.splitext(i)[1] == ".md":
            md_list.append(os.path.join(dir_path, i))
        else:
            cur_path = os.path.join(dir_path, i)
            cur_doc = os.path.join(cur_path, "doc.md")
            if os.path.isdir(cur_path) and os.path.isfile(cur_doc):
                md_list.append(cur_doc)
    return md_list
# 获取特定目录的 markdown 文件列表


def get_md_info(file_path):
    """ 通过 md 文件获取项目名和更新时间 """
    (md_mtime, md_ctime) = fnGetFileTime(file_path)
    fnEmpty(md_ctime)
    file_path = file_path.replace("\\", "/")
    md_name = os.path.basename(os.path.splitext(file_path)[0])
    if md_name == "doc":
        tmp_name = file_path.replace("/doc.md", "")
        md_name = os.path.basename(tmp_name)
    return (md_name, md_mtime)
# 通过 md 文件获取项目名和更新时间


def get_md_content(file_path):
    """ 获取 markdown 文件中的内容 """
    content = ""
    metadata = {}
    with open(file_path, 'r', encoding='UTF-8') as f:
        post = frontmatter.load(f)
        content = post.content.replace("<!-- more -->", "<!--more-->")
        metadata = post.metadata
        # print("==>>", post.content)
        # print("===>>", post.metadata)
    return (content, metadata)
# 获取 markdown 文件中的内容


def md_list_fn(posts_dir):
    """ 获取 md 文件列表并处理 """
    fnLog()
    fnLog("## 遍历文章处理：")
    md_list = get_md_list(posts_dir)
    for md in md_list:
        # 获取文件信息
        (md_name, md_mtime) = get_md_info(md)
        fnLog("### %s | %s" % (md_name, fnGetTimeStr(md_mtime)),
              inspect.currentframe().f_lineno)

    # end for
