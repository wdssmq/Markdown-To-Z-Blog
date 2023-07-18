""" 主入口文件 """
import os
import sys
import json
import time
import inspect


# 从 bin/base.py 中导入通用函数
from bin.base import fnBug, fnErr, fnLog
# 从 bin/func.py 中导入函数
from bin.func import read_logs, update_logs_git
# 从 bin/http_func.py 中导入 http 请求封装
from bin.http_func import http_init, login
# 众 bin/md_func.py 中导入 md 文件处理函数
from bin.md_func import md_init, md_list_fn

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
    "logs_file": os.path.join(os.getcwd(), "_posts_logs.json"),
    "readme_file": os.path.join(os.getcwd(), "README.md"),
    "posts_dir": os.path.join(os.getcwd(), "_posts"),
    "need_save": False
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
            # logs_info["changed"] = os.environ["GIT_CHANGED_FILES"]
            # 字符串转列表，去除首尾空格，空格分割
            logs_info["changed"] = os.environ["GIT_CHANGED_FILES"].strip().split(" ")

    except KeyError:
        fnLog("无法获 github 的 secrets 配置信息，开始使用本地变量")
        fnBug("config 内拥有以下值: %s" % str(config_info.keys()),
              inspect.currentframe().f_lineno)

    # 读取配置文件
    if os.path.exists("config.json") is True:
        with open("config.json", 'rb') as config_file:
            config_info = json.loads(config_file.read())

    # 读取 debug 配置
    if "DEBUG" in config_info.keys() and config_info["DEBUG"]:
        debug_info["debug"] = True
        fnBug("debug 已开启: %s" % debug_info["debug"],
              inspect.currentframe().f_lineno, debug_info["debug"])

    # 判断同时有 'API_USR', 'API_PWD', 'API_URL' 三个配置
    if "API_USR" not in config_info.keys() or "API_PWD" not in config_info.keys() or "API_URL" not in config_info.keys():
        fnErr("缺少配置信息: %s" % str(config_info.keys()),
              inspect.currentframe().f_lineno)
        sys.exit(0)
    else:
        fnBug("config 内拥有以下值: %s" % str(config_info.keys()), inspect.currentframe().f_lineno,
              debug_info["debug"])

    # 自定义图床域名
    if "IMG_HOST" not in config_info.keys():
        config_info["IMG_HOST"] = ""

    # 调试模式使用另外的文件路径
    if debug_info["debug"]:
        logs_info["logs_file"] = os.path.join(
            os.getcwd(), "_debug_posts_logs.json")
        logs_info["readme_file"] = os.path.join(
            os.getcwd(), "_debug_README.md")

    # 读取日志文件
    logs_info["list"] = read_logs(logs_info["logs_file"])
    # 合并更新日志
    update_logs_git(logs_info, debug_info["debug"])

    # fnBug(logs_info["list"], inspect.currentframe().f_lineno, debug_info["debug"])
# 初始化函数


# 初始化调用
init()

# 登录调用
http_init(config_info, logs_info, debug_info)
login()

# md 处理调用
md_init(config_info, logs_info, debug_info)
md_list_fn(logs_info["posts_dir"])
