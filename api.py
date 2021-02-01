import os
import requests
import json
import time
import locale
import markdown
import frontmatter
import re
import sys

from api_function import fnGetDirsInDir, fnGetFilesInDir, fnGetFilesInDir2, fnGetFileTime
from api_function import fnLog, fnBug, fnErr, fnEmpty

# LC_TIME = locale.setlocale(locale.LC_TIME)
# LC_CTYPE = locale.setlocale(locale.LC_CTYPE)
# print(LC_TIME)
# print(LC_CTYPE)
# 目测远程不需要设置这个

config_info = {}


if((os.path.exists("config.json") == True)):
    with open("config.json", 'rb') as f:
        config_info = json.loads(f.read())

try:
    if(os.environ["API_USR"]):
        config_info["API_USR"] = os.environ["API_USR"]

    if(os.environ["API_PWD"]):
        config_info["API_PWD"] = os.environ["API_PWD"]

    if(os.environ["API_URL"]):
        config_info["API_URL"] = os.environ["API_URL"]

    if(os.environ["_cache_logs"]):
        config_info["_cache_logs"] = os.environ["_cache_logs"]
except:
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    config_info["_cache_logs"] = "_fake.json"
    fnLog("无法获取github的secrets配置信息,开始使用本地变量")

fnBug(config_info)

if not any(config_info):
    fnErr("未设置登录信息")
    sys.exit(0)


def login():
    data_arg = {"username": config_info["API_USR"],
                "password": config_info["API_PWD"]}
    data = http("post", "member", "login", data_arg)
    if not data is None:
        config_info["token"] = data["token"]
        config_info["AuthorID"] = data["user"]["ID"]
        fnLog("登录成功")
        # 调试↓
        # print(data)
        # print(config_info)
# 登录


def get_post_list():
    data = http("get", "post", "list", {"page": 1})
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
        return (True, post["ID"], post["UpdateTime"])
    return (False, 0, 0)
# 更新文章


def http(method, mod, act, data_arg={}):
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
        print(rlt)
        print(rlt["message"])
    return rlt["data"]
# http封装


def update_readme():
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
    with open(os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    # print(insert_info)

    new_readme_md_content = re.sub(
        r'---start---(.|\n)*---end---', insert_info, readme_md_content)

    with open(os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8', newline="\n") as f:
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
        if i == ".gitkeep":
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
_posts_dir_path = os.path.join(os.getcwd(), "_posts")
# 日志文件
_posts_logs_file = os.path.join(os.getcwd(), "_posts_logs.json")
# 日志数据
_posts_logs_data = read_logs(_posts_logs_file)

# git时间缓存文件
# _cache_logs_file = os.path.join(os.getcwd(), "_cache_logs.json")
_cache_logs_file = config_info["_cache_logs"]
# git时间缓存数据
_cache_logs_data = read_logs(_cache_logs_file)


def update_git_time():
    if any(_cache_logs_data):
        tip = "git"
    else:
        tip = "文件"
    fnLog("时间依据："+tip)
    for git_time in _cache_logs_data:
        md_file = _cache_logs_data[git_time]
        if "README.md" == md_file:
            continue
        # fnBug()
        (md_name, md_mtime) = get_md_name(os.path.join(os.getcwd(), md_file))
        fnEmpty(md_mtime)
        print(md_name)
        if (md_name in _posts_logs_data.keys()):
            _posts_logs_data[md_name]["git_time"] = git_time
            print(_posts_logs_data[md_name])
# 获取Git时间
update_git_time()


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
        if any(_cache_logs_data):
            mtime = _posts_logs_data[key]["git_time"]
        log_mtime = _posts_logs_data[key]["mtime"]
        fnLog("md: %s, log: %s" % (mtime, log_mtime))
        if (mtime <= log_mtime):
            msg = "skip"
        else:
            id = _posts_logs_data[key]["id"]
            msg = "update"

    return (msg, id)
# 日志查询


def main():
    # 登录
    login()

    # 获取md文件列表并处理
    print("------")
    md_list = get_md_list(_posts_dir_path)
    for md in md_list:
        # 文件标识名
        (md_name, md_mtime) = get_md_name(md)
        # fnBug(md_name, sys._getframe().f_lineno)

        # 判断更新时间
        (msg, id) = check_logs(md_name, md_mtime)
        if "skip" == msg:
            fnLog("无需同步 "+md_name)
            print("---")
            continue
        elif "update" == msg:
            fnLog("md更新 "+md_name)

        # 读取md文件信息
        (content, metadata) = read_md(md)

        # 判断内容格式
        if not any(metadata):
            fnErr("md数据错误", md)
            print("---")
            continue

        # metadata解析
        title = metadata.get("title", "")
        tags = metadata.get("tags", "")
        cate = metadata.get("categories", "")

        # Markdown 解析
        content = markdown.markdown(
            content, extensions=['tables', 'fenced_code'])

        # post data构造
        data_arg = {"Type": "0", "ID": id, "Title": title,
                    "Content": content, "Tag": ",".join(tags), "CateName": cate}
        # 提交请求
        (done, post_id, post_mtime) = update_post(0, data_arg)
        # fnBug("%s %s %s" % (done, post_id, post_mtime), sys._getframe().f_lineno)

        # 写入日志
        if done:
            post_info = {"id": post_id, "mtime": post_mtime}
            update_logs(md_name, post_info)

        # 输出结果
        fnLog("文件：" + md_name)
        fnLog("标题：" + title)
        fnLog("状态：" + str(done))
        print("---")
    print("------")

    # 更新最新文章到readme
    update_readme()
# 入口


main()
