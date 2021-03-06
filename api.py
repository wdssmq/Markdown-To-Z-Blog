# This Python file uses the following encoding: utf-8
import os
import sys
import requests
import json
import time
import locale
import markdown
import frontmatter
import re

from api_function import fnGetDirsInDir, fnGetFilesInDir, fnGetFilesInDir2, fnGetFileTime
from api_function import fnEmpty, fnLog, fnBug, fnErr

# LC_TIME = locale.setlocale(locale.LC_TIME)
# LC_CTYPE = locale.setlocale(locale.LC_CTYPE)
# print(LC_TIME)
# print(LC_CTYPE)
# 目测远程不需要设置这个

_now = int(time.time())
_local_time = time.localtime(_now)
_local_time_format = time.strftime('%Y-%m-%d %H:%M:%S', _local_time)

fnLog("# 开始")
fnLog("当前时间戳：%s, %s" % (_now, _local_time_format))
fnLog()

config_info = {}
_cache_logs_json = "[]"
_debug = False


def init():
    global config_info, _cache_logs_json, _debug
    if((os.path.exists("config.json") == True)):
        with open("config.json", 'rb') as f:
            config_info = json.loads(f.read())
        # fnBug(config_info, sys._getframe().f_lineno)
    try:
        if(os.environ["API_USR"]):
            config_info["API_USR"] = os.environ["API_USR"]

        if(os.environ["API_PWD"]):
            config_info["API_PWD"] = os.environ["API_PWD"]

        if(os.environ["API_URL"]):
            config_info["API_URL"] = os.environ["API_URL"]

        if(os.environ["_cache_logs"]):
            _cache_logs_json = os.environ["_cache_logs"]
    except:
        if not ("USER" in os.environ.keys() and os.environ["USER"] == "root"):
            locale.setlocale(locale.LC_CTYPE, 'chinese')
        # _cache_logs_json = "[]"
        fnLog("## init")
        fnLog("无法获取github的secrets配置信息,开始使用本地变量")
        fnLog()
    fnLog("## init")
    if not any(config_info):
        fnErr("未设置登录信息", sys._getframe().f_lineno)
        sys.exit(0)
    else:
        fnBug(config_info.keys(), sys._getframe().f_lineno)
    fnLog()
    if "DEBUG" in config_info.keys() and config_info["DEBUG"] == 1:
        _debug = True
# 初始化信息


fnLog("# init")
init()
fnLog()


def login():
    data_arg = {"username": config_info["API_USR"],
                "password": config_info["API_PWD"]}
    data = http("post", "member", "login", data_arg)
    if not data is None:
        config_info["token"] = data["token"]
        config_info["AuthorID"] = data["user"]["ID"]
        fnLog("登录成功")
    else:
        fnErr("登录失败", sys._getframe().f_lineno)
        sys.exit(0)

# 登录


def get_post_code(id):
    data = http("get", "post", "get", {"id": id}, "all")
    data["title"] = ""
    if not data["data"] is None:
        # fnLog(data["data"])
        data["title"] = data["data"]["post"]["Title"]
    return (data["code"], data["title"])
# 查找文章，返回状态码


def get_post_list():
    data = http("get", "post", "list", {
                "page": 1, "sortby": "UpdateTime", "order": "DESC", "perpage": 37})
    if not data is None:
        # 调试↓
        # print(data)
        # print(len(data["list"]))
        return data["list"]
# 获取文章列表


def update_post(id, data_arg):
    # Todo 通过分类名获取id
    # cate_id = 12
    # data_arg["CateID"] = cate_id
    author_id = config_info["AuthorID"]
    data_arg["AuthorID"] = author_id
    # data_arg["Intro"] = "请在正文内使用<!--more-->"
    data_arg["Intro"] = "请在正文内使用&lt;!--more--&gt;"
    data = http("post", "post", "post", data_arg)
    if not data is None:
        post = data["post"]
        # print(post)
        return (True, post["ID"], post["UpdateTime"])
    return (False, 0, 0)
# 更新文章


def http(method, mod, act, data_arg={}, format="data"):
    try:
        headers_arg = {"Authorization": "Bearer " + config_info["token"]}
    except:
        headers_arg = {}
        fnLog("未登录")
    if method == "get":
        r = requests.get(config_info["API_URL"] + "?mod=" + mod +
                         "&act=" + act, params=data_arg, headers=headers_arg)
        # 调试↓
        # print(r.url)
    else:
        r = requests.post(config_info["API_URL"] + "?mod=" +
                          mod + "&act=" + act, data=data_arg, headers=headers_arg)
    rlt = r.json()
    if rlt["code"] > 200:
        fnBug(rlt, sys._getframe().f_lineno)
    if format == "all":
        return rlt
    return rlt["data"]
# http封装


def update_readme(readme):
    post_list = get_post_list()
    # 生成插入列表
    insert_info = ""
    # 读取md_list中的文件标题
    for post in post_list:
        title = post["Title"]
        url = post["Url"]
        md_link = '[%s](%s "%s")' % (title,  url,  title)
        insert_info = insert_info + md_link + "\n\n"

    # 替换 ---start--- 到 ---end--- 之间的内容
    insert_info = "---start---\n\n## 目录(" + time.strftime(
        ' %Y 年 %m 月 %d 日') + "更新)" + "\n\n" + insert_info + "---end---"

    # 获取README.md内容
    with open(readme, 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    # print(insert_info)

    new_readme_md_content = re.sub(
        r'---start---(.|\n)*?---end---', insert_info, readme_md_content, 1)

    with open(readme, 'w', encoding='utf-8', newline="\n") as f:
        f.write(new_readme_md_content)

    fnLog("更新ReadMe成功")

    return True
# 在README.md中插入信息文章索引信息，更容易获取google的收录


def read_md(file_path):
    content = ""
    metadata = {}
    with open(file_path, 'r', encoding='UTF-8') as f:
        post = frontmatter.load(f)
        content = post.content
        metadata = post.metadata
        # print("==>>", post.content)
        # print("===>>", post.metadata)
    return (content, metadata)
# 获取markdown文件中的内容


def get_md_name(file):
    (md_mtime, md_ctime) = fnGetFileTime(file)
    fnEmpty(md_ctime)
    file = file.replace("\\", "/")
    md_name = os.path.basename(os.path.splitext(file)[0])
    if md_name == "doc":
        tmp_name = file.replace("/doc.md", "")
        md_name = os.path.basename(tmp_name)
    return (md_name, md_mtime)
# 通过md文件获取项目名和更新时间


def get_md_list(dir_path):
    # 绝对路径列表
    md_list = []
    dirs = os.listdir(dir_path)
    for i in dirs:
        if i == ".gitkeep" or i == "1970-01-01-empty.md":
            continue
        if os.path.splitext(i)[1] == ".md":
            md_list.append(os.path.join(dir_path, i))
        else:
            cur_path = os.path.join(dir_path, i)
            cur_doc = os.path.join(cur_path, "doc.md")
            if os.path.isdir(cur_path) and os.path.isfile(cur_doc):
                md_list.append(cur_doc)
    return md_list
# 获取特定目录的markdown文件列表


def read_logs(file):
    if(os.path.exists(file) == True):
        file_byte = open(file, 'r')
        file_info = file_byte.read()
        result = json.loads(file_info)
        file_byte.close()
    else:
        result = {}
    return result
# 获取同步记录


# 全局变量
# 文章路径
_posts_dir = os.path.join(os.getcwd(), "_posts")

# README.md
_readme_file = os.path.join(os.getcwd(), "README.md")

# 日志文件
_posts_logs_file = os.path.join(os.getcwd(), "_posts_logs.json")

if _debug:
    _posts_logs_file = os.path.join(os.getcwd(), "_debug_posts_logs.json")
    _readme_file = os.path.join(os.getcwd(), "_debug_README.md")

# 日志数据
_posts_logs_data = read_logs(_posts_logs_file)


# git更新的文件（数组）
_cache_logs_data = json.loads(_cache_logs_json)


def update_git_diff():
    if any(_cache_logs_data):
        fnBug(_cache_logs_data, sys._getframe().f_lineno)
        tip = "git"
    else:
        tip = "文件时间"
    fnLog("更新依据：" + tip)
    for item in _cache_logs_data:
        # fnBug(item, sys._getframe().f_lineno)
        if not os.path.splitext(item)[1] == ".md":
            continue
        if "README.md" == item:
            continue
        (md_name, md_mtime) = get_md_name(os.path.join(os.getcwd(), item))
        fnEmpty(md_mtime)
        print(md_name)
        if (md_name in _posts_logs_data.keys()):
            _posts_logs_data[md_name]["git_update"] = 1
            # print(_posts_logs_data[md_name])
# Git中修改的文件


def update_logs(key, value):
    _posts_logs_data[key] = value
    file = open(_posts_logs_file, 'w')
    file.write(json.dumps(_posts_logs_data))
    file.close()
    return True
# 写入同步


def check_logs(key, mtime):
    msg = ""
    id = 0
    if (key in _posts_logs_data.keys()):
        id = _posts_logs_data[key]["id"]
        log_mtime = _posts_logs_data[key]["mtime"]
        if any(_cache_logs_data):
            if ("git_update" in _posts_logs_data[key].keys()):
                msg = "update"
            else:
                msg = "skip"
        else:
            if (mtime > log_mtime):
                msg = "update"
            else:
                msg = "skip"
        # fnBug("md_name：%s, md_time: %s, log_time: %s, msg：%s" %
        #       (key, mtime, log_mtime, msg), sys._getframe().f_lineno)

    return (msg, id)
# 日志查询


def main():
    # Actions中只针对提交的文件
    fnLog("## update_git_diff")
    update_git_diff()
    fnLog()

    # 登录
    fnLog("## login")
    login()
    fnLog()

    fnLog("## -----")
    # 获取md文件列表并处理
    md_list = get_md_list(_posts_dir)
    for md in md_list:
        fnLog("###")
        # 文件标识名
        (md_name, md_mtime) = get_md_name(md)
        fnLog(md_name, sys._getframe().f_lineno)

        # 判断更新时间
        (msg, id) = check_logs(md_name, md_mtime)
        if "skip" == msg:
            fnLog("无需同步")
            fnLog()
            print("---")
            continue
        elif "update" == msg:
            fnLog("md更新")

        # 读取md文件信息
        (md_content, metadata) = read_md(md)

        # 判断内容格式
        if not any(metadata):
            fnErr("md数据错误", md)
            fnLog()
            print("---")
            continue

        # metadata解析
        title = metadata.get("title", "")
        tags = metadata.get("tags", "")
        cate = metadata.get("categories", "")
        alias = metadata.get("alias", "")
        cover_id = metadata.get("id", "")
        status = metadata.get("status", "0")
        # fnBug(cover_id, sys._getframe().f_lineno)
        if title == "未命名":
            fnErr("标题：" + title)
            fnLog()
            print("---")
            continue
        if isinstance(cover_id, int):
            (cover_code, cover_title) = get_post_code(cover_id)
            if cover_code == 200:
                fnLog("使用指定id", cover_id)
                fnLog("文章将被覆盖", ("《%s》" % cover_title))
                id = cover_id

        # Markdown 解析
        content = markdown.markdown(
            md_content, extensions=['tables', 'fenced_code', 'sane_lists', 'md_in_html'])

        content = "%s<!--%i-->\n" % (content, id)
        md_content = "%s<!--%i-->\n" % (md_content, id)

        # post data构造
        data_arg = {"Type": "0", "ID": id, "Title": title,
                    "Content": content, "MD_Content": md_content, "Tag": ",".join(tags), "CateName": cate, "Status": status}
        # 提交请求
        (done, post_id, post_mtime) = update_post(0, data_arg)
        # fnBug("%s %s %s" % (done, post_id, post_mtime), sys._getframe().f_lineno)
        # fnBug(type(post_id), sys._getframe().f_lineno)
        # 写入日志
        if done:
            post_info = {"id": int(post_id), "mtime": post_mtime}
            update_logs(md_name, post_info)

        # 输出结果
        fnLog("文件：" + md_name)
        fnLog("标题：" + title)
        fnLog("状态：" + str(done))
        print("---")
    print("-----")
    fnLog()

    # 更新最新文章到readme
    fnLog("## update_readme")
    update_readme(_readme_file)
    fnLog()
# 入口


fnLog("# main")
main()
# fnLog()
