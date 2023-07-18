""" HTTP 请求 """
import sys
import inspect
import requests

# pylint: disable=global-statement

from bin.base import fnBug, fnErr, fnLog

# 全局变量
config_info = {}
logs_info = {}
debug_info = {}


def http_init(config, logs, debug):
    """ 初始化 """
    global config_info, logs_info, debug_info

    config_info = config
    logs_info = logs
    debug_info = debug


def http(req_arg=None, data_arg=None, return_format="data"):
    """ HTTP 请求 """
    if req_arg is None:
        req_arg = {}
    if data_arg is None:
        data_arg = {}
    # ----------------------------------------
    req_arg["base_url"] = config_info["API_URL"]

    try:
        headers_arg = {"Authorization": "Bearer " + config_info["token"]}
    except KeyError:
        headers_arg = {}

    url = req_arg["base_url"] + "?mod=" + \
        req_arg["mod"] + "&act=" + req_arg["act"]

    fnBug(url, inspect.currentframe().f_lineno, debug_info["debug"])

    try:
        if req_arg["method"] == "get":
            res_info = requests.get(
                url, params=data_arg, headers=headers_arg, timeout=10)
        else:
            res_info = requests.post(
                url, data=data_arg, headers=headers_arg, timeout=10)
    except KeyError:
        fnErr("网络错误", inspect.currentframe().f_lineno)
        sys.exit(0)

    res_data = res_info.json()
    if res_data["code"] > 200:
        fnBug(res_data, inspect.currentframe().f_lineno, debug_info["debug"])
    if return_format == "all":
        return res_data
    return res_data["data"]
# http 封装


def login():
    """ 登录 """
    fnLog()
    fnLog("## login")
    # 登录
    data_arg = {
        "username": config_info["API_USR"],
        "password": config_info["API_PWD"]
    }
    data = http({
        "method": "post",
        "mod": "member",
        "act": "login"
    }, data_arg)

    if not data is None:
        config_info["token"] = data["token"]
        config_info["AuthorID"] = data["user"]["ID"]
        fnLog("登录成功")
    else:
        fnErr("登录失败", inspect.currentframe().f_lineno)
        sys.exit(0)
# 登录


def get_post_code(id):
    """ 查找文章，返回状态码 """
    data = http({
        "method": "get",
        "mod": "post",
        "act": "get"
    }, {
        "id": id
    }, "all")
    data["title"] = ""
    if not data["data"] is None:
        data["title"] = data["data"]["post"]["Title"]
    return (data["code"], data["title"])
# 查找文章，返回状态码

def update_post(data_arg):
    """ 更新文章 """
    # Todo 通过分类名获取 id
    # cate_id = 12
    # data_arg["CateID"] = cate_id
    author_id = config_info["AuthorID"]
    data_arg["AuthorID"] = author_id
    # data_arg["Intro"] = "请在正文内使用 <!-- more -->"
    data_arg["Intro"] = "请在正文内使用 &lt;!-- more --&gt;"
    data = http({
        "method": "post",
        "mod": "post",
        "act": "post"
    }, data_arg)
    if not data is None:
        post = data["post"]
        # print(post)
        return (True, post["ID"], post["UpdateTime"])
    return (False, 0, 0)
# 更新文章
