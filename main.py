""" 主入口文件 """
import os
import sys
import json
import time
import inspect


# 从 bin/base.py 中导入通用函数
from bin.base import fnBug, fnErr, fnLog
# 从 bin/http.py 中导入 http 请求封装
from bin.http import login, http_init

# 时间信息
_now = int(time.time())
_local_time = time.localtime(_now)
_local_time_format = time.strftime('%Y-%m-%d %H:%M:%S', _local_time)

fnLog("# 开始")
fnLog("当前时间戳：%s, %s" % (_now, _local_time_format))
fnLog()

# 全局变量
config_info = {}
logs_info = {
    "changed": [],
    "list": [],
}
debug_info = {
    "debug": False,
    "log": ""
}

# pylint: disable=global-statement, consider-using-f-string

def init():
    ''' 初始化 '''
    global config_info
    fnLog("## init")

    # 读取 github secrets 配置
    try:
        if os.environ["API_USR"]:
            config_info["API_USR"] = os.environ["API_USR"]

        if os.environ["API_PWD"]:
            config_info["API_PWD"] = os.environ["API_PWD"]

        if os.environ["API_URL"]:
            config_info["API_URL"] = os.environ["API_URL"]

        if os.environ["IMG_HOST"]:
            config_info["IMG_HOST"] = os.environ["IMG_HOST"]

        if os.environ["GIT_REPO"]:
            config_info["GIT_REPO"] = os.environ["GIT_REPO"]

        if os.environ["GIT_CHANGED_FILES"]:
            logs_info["changed"] = os.environ["GIT_CHANGED_FILES"]

    except KeyError:
        fnLog("无法获 github 的 secrets 配置信息，开始使用本地变量")
        fnBug("config 内拥有以下值: %s" % str(config_info.keys()), inspect.currentframe().f_lineno)

    # 读取配置文件
    if os.path.exists("config.json") is True:
        with open("config.json", 'rb') as config_file:
            config_info = json.loads(config_file.read())

    # 读取 debug 配置
    if "DEBUG" in config_info.keys() and config_info["DEBUG"]:
        debug_info["debug"] = True
        fnBug("debug 已开启: %s" % debug_info["debug"],
              inspect.currentframe().f_lineno, debug_info["debug"])

    # 判断为空时退出
    if not any(config_info):
        fnErr("配置信息为空", inspect.currentframe().f_lineno)
        sys.exit(0)
    else:
        fnBug("config 内拥有以下值: %s" % str(config_info.keys()), inspect.currentframe().f_lineno,
              debug_info["debug"])

    # 登录
    http_init(config_info, logs_info, debug_info)
    login()
# 初始化函数


init()
