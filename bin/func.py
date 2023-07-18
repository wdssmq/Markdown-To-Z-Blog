""" 函数拆分 """
import os
import json

def read_logs(file_path):
    """ 读取日志 """
    if os.path.exists(file_path) is True:
        with open(file_path, 'r', encoding='utf-8') as logs_file:
            result = json.loads(logs_file.read())
    else:
        result = {}
    return result
# 读取日志
