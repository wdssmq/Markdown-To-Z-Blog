""" 函数拆分 """
import os
import json
import inspect
import re
import time

from bin.base import fnEmpty, fnLog, fnBug

# pylint: disable=import-outside-toplevel, consider-using-f-string

def up_img_host(md_name, md_content, img_host = ""):
    """ 替换图片路径 """
    if img_host != "":
        if img_host.endswith("/"):
            img_host = img_host[:-1]
        # 图片地址替换 —— ./ 开头
        md_content = re.sub(r'!\[([^\]]+)\]\(\.\/([^\)]+)\)',
                            r'![\1](%s/_posts/\2)' % (img_host, md_name), md_content)
        # 图片地址替换 —— 同级目录
        md_content = re.sub(r'!\[([^\]]+)\]\(((?!http)[^\)]+)\)', r'![\1](%s/_posts/%s/\2)' %
                            (img_host, md_name), md_content)
    return md_content
# 替换图片路径


def read_logs(file_path):
    """ 读取日志 """
    if os.path.exists(file_path) is True:
        with open(file_path, 'r', encoding='utf-8') as logs_file:
            result = json.loads(logs_file.read())
    else:
        result = {}
    return result
# 读取日志


def update_logs(key, value, logs_info):
    """ 写入/更新日志字段 """
    logs_info["list"][key] = value
    return True
# 写入/更新日志字段


def save_logs(logs_info):
    """ 保存日志 """
    fnLog("### 保存日志")
    if not logs_info["need_save"]:
        fnLog("不需要保存")
        fnLog()
        return
    # 按字典键对数据进行排序
    sorted_data = {k: logs_info["list"][k]
                   for k in sorted(logs_info["list"].keys())}
    # 保存
    with open(logs_info["logs_file"], 'w', encoding='utf-8') as file:
        file.write(json.dumps(sorted_data, indent=4))
        file.close()
        fnLog("更新 JSON 成功")
        fnLog()
# 保存日志


def update_logs_git(logs_info, debug=False):
    """ 将 git 更新的文件标记为待更新 """
    from bin.md_func import get_md_info
    fnLog("### 合并 git 更新到 logs")
    # # 判断 logs_info["changed"] 类型
    # print(type(logs_info["changed"]))
    if not any(logs_info["changed"]):
        return
    fnBug(logs_info["changed"], inspect.currentframe().f_lineno, debug)
    for item in logs_info["changed"]:
        if not os.path.splitext(item)[1] == ".md":
            continue
        if "README.md" == item:
            continue
        (md_name, md_mtime) = get_md_info(os.path.join(os.getcwd(), item))
        fnEmpty(md_mtime)
        fnBug(md_name, inspect.currentframe().f_lineno, debug)
        if md_name in logs_info["list"].keys():
            logs_info["list"][md_name]["git_update"] = 1
# 将 git 更新的文件标记为待更新


def check_logs(key, file_mtime, logs_info, debug=False):
    """ 检查是否需要更新 """
    logs_list = logs_info["list"]
    is_git_update = logs_info["is_git_update"]

    log_msg = ""
    log_id = 0
    if key in logs_list:
        log_data = logs_list[key]
        log_id = log_data.get("id", 0)
        log_mtime = log_data.get("mtime", 0)

        fnBug(log_data, inspect.currentframe().f_lineno, debug)

        if is_git_update and log_data.get("git_update", 0) == 1:
            log_msg = "update"
        elif not is_git_update and file_mtime > log_mtime:
            log_msg = "update"
        else:
            log_msg = "skip"

    return log_msg, log_id
# 检查是否需要更新

insert_tpl = """
---start---\n
## 目录 - {date_str} 更新\n
{post_list_str}\n
---end---
"""

def update_readme(readme_file, post_list, debug_info):
    """ 更新 README """
    fnLog("### 更新 README")
    fnBug(len(post_list), inspect.currentframe().f_lineno, debug_info["debug"])
    date_str = time.strftime(
        ' %Y 年 %m 月 %d 日')
    post_list_str = ""
    # 读取 md_list 中的文件标题
    for post in post_list:
        title = post["Title"]
        url = post["Url"]
        md_link = '[%s](%s "%s")' % (title,  url,  title)
        post_list_str = post_list_str + md_link + "\n\n"
    post_list_str = post_list_str.strip()
    # 读取 readme 文件
    with open(readme_file, 'r', encoding='utf-8') as file:
        readme_content = file.read()
        file.close()
    # 替换内容
    insert_str = insert_tpl.format(
        date_str=date_str, post_list_str=post_list_str)
    # 清除前后空白
    insert_str = insert_str.strip()
    new_readme = re.sub(r'---start---(.|\n)*?---end---', insert_str , readme_content, 1)

    with open(readme_file, 'w', encoding='utf-8') as file:
        file.write(new_readme)
        file.close()
    return True
# 更新 README
