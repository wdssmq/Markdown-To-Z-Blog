""" 函数拆分 """
import os
import json
import inspect

from bin.base import fnEmpty, fnBug

# pylint: disable=import-outside-toplevel

def read_logs(file_path):
    """ 读取日志 """
    if os.path.exists(file_path) is True:
        with open(file_path, 'r', encoding='utf-8') as logs_file:
            result = json.loads(logs_file.read())
    else:
        result = {}
    return result
# 读取日志


def update_logs_git(logs_info):
    """ 将 git 更新的文件标记为待更新 """
    from bin.md_func import get_md_info
    if not any(logs_info["changed"]):
        return
    for item in logs_info["changed"]:
        if not os.path.splitext(item)[1] == ".md":
            continue
        if "README.md" == item:
            continue
        (md_name, md_mtime) = get_md_info(os.path.join(os.getcwd(), item))
        fnEmpty(md_mtime)
        print(md_name)
        if md_name in logs_info["list"].keys():
            logs_info["list"][md_name]["git_update"] = 1
# 将 git 更新的文件标记为待更新


def check_logs(key, file_mtime, logs_info, debug=False):
    """ 检查是否需要更新 """
    logs_list = logs_info["list"]
    logs_changed = logs_info["changed"]

    # fnBug(logs_changed, inspect.currentframe().f_lineno, debug)
    # fnBug(key in logs_changed, inspect.currentframe().f_lineno, debug)

    log_msg = ""
    log_id = 0
    if key in logs_list:
        log_data = logs_list[key]
        log_id = log_data.get("id", 0)
        log_mtime = log_data.get("mtime", 0)

        fnBug(log_data, inspect.currentframe().f_lineno , debug)

        if file_mtime > log_mtime:
            log_msg = "update"
        else:
            log_msg = "skip"

    return log_msg, log_id
# 检查是否需要更新
