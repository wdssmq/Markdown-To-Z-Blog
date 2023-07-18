""" 函数拆分 """
import os
import json
import inspect

from bin.base import fnBug


def read_logs(file_path):
    """ 读取日志 """
    if os.path.exists(file_path) is True:
        with open(file_path, 'r', encoding='utf-8') as logs_file:
            result = json.loads(logs_file.read())
    else:
        result = {}
    return result
# 读取日志


def check_logs(key, file_mtime, logs_info, debug=False):
    """ 检查是否需要更新 """
    logs_list = logs_info["list"]
    logs_changed = logs_info["changed"]

    fnBug(logs_changed, inspect.currentframe().f_lineno, debug)
    fnBug(key in logs_changed, inspect.currentframe().f_lineno, debug)

    log_msg = ""
    log_id = 0
    if key in logs_list:
        log_data = logs_list[key]
        log_id = log_data.get("id", 0)
        log_mtime = log_data.get("mtime", 0)

        if file_mtime > log_mtime:
            log_msg = "update"
        else:
            log_msg = "skip"

    return log_msg, log_id
# 检查是否需要更新
