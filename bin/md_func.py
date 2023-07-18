""" Markdown 文件相关操作 """
import os
import frontmatter
import inspect
import markdown

from bin.base import fnEmpty, fnLog, fnBug, fnErr, fnGetTimeStr, fnGetFileTime
from bin.func import check_logs, update_logs, save_logs, up_img_host
from bin.http_func import get_post_code, update_post

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


def md_file_check(md_meta, md_file):
    """ 检查 markdown 文件是否符合要求 """
    if md_meta["title"] == "未命名" or "new-post" in md_meta["md_name"]:
        fnErr("标题或文件名不符合要求：%s" % md_file,  inspect.currentframe().f_lineno)
        return False
    return True
# 检查 markdown 文件是否符合要求


def md_post_fn(md_content, md_meta, md_file):
    """ 解析 markdown 文件并发送 """
    # 跳过「未命名」文章
    if not md_file_check(md_meta, md_file):
        return False
    # metadata 解析
    post_data = {
        "title": md_meta.get("title", ""),
        "date": md_meta.get("date", ""),
        "tags": md_meta.get("tags", ""),
        "cate": md_meta.get("categories", ""),
        "alias": md_meta.get("alias", ""),
        "status": md_meta.get("status", "0"),
        "cover_id": md_meta.get("id", ""),
        "log_id": md_meta.get("log_id", ""),
        "md_name": md_meta.get("md_name", ""),
    }

    debug = debug_info["debug"]
    # DEBUG 开启时以 cover_id 为准
    if debug and isinstance(post_data["cover_id"], int) and post_data["log_id"] == 0:
        fnLog()
        fnBug(post_data["cover_id"],  inspect.currentframe().f_lineno)
        fnLog()
        post_data["log_id"] = post_data["cover_id"]

    # cover_id 不为空，且 _posts_logs_data 中不存在时远程拉取文章信息
    if isinstance(post_data["cover_id"], int) and post_data["log_id"] == 0:
        (web_code, web_title) = get_post_code(post_data["cover_id"])
        if web_code == 200:
            fnLog("文章将被覆盖：「%s」「%s」" %
                  (post_data["cover_id"], web_title))
            post_data["log_id"] = post_data["cover_id"]
        else:
            fnErr("文章不存在：%s" % post_data["cover_id"],
                  inspect.currentframe().f_lineno)
            debug_info["log"] += "文章不存在：%s | %s \n" % (
                post_data["cover_id"], post_data["md_name"])
            return False

    # cover_id 不为空，但是与 _posts_logs_data 记录不一致时
    if isinstance(post_data["cover_id"], int) and post_data["cover_id"] != post_data["log_id"]:
        debug_info["log"] += "ID 不匹配：%s - %s - %s \n" % (post_data["md_name"],
                                                         post_data["cover_id"], post_data["log_id"])

    if not isinstance(post_data["cover_id"], int):
        debug_info["log"] += "未指定 id ：%s - %s \n" % (post_data["md_name"],
                                                     post_data["cover_id"])

    if post_data["alias"] == "":
        debug_info["log"] += "未指定 alias ：%s \n" % (post_data["md_name"])

    md_content = up_img_host(
        post_data["md_name"], md_content, config_info["IMG_HOST"])

    html_content = markdown.markdown(
        md_content, extensions=['tables', 'fenced_code', 'sane_lists', 'md_in_html', 'nl2br'])

    html_content = "%s<!--%i-->\n" % (html_content, post_data["log_id"])
    md_content = "%s<!--%i-->\n" % (md_content, post_data["log_id"])

    # post data 构造
    data_arg = {
        "Type": "0",
        "ID": post_data["log_id"],
        "Title": post_data["title"],
        "Alias": post_data["alias"],
        "Content": html_content,
        "MD_Content": md_content,
        "Tag": ",".join('%s' % tag for tag in post_data["tags"]),
        "CateName": post_data["cate"],
        "Status": post_data["status"],
    }
    # 合并 date
    if post_data["date"] != "":
        data_arg["PostTime"] = post_data["date"]

    # 提交请求
    (done, post_id, post_mtime) = update_post(data_arg)

    # 写入日志
    if done:
        post_info = {
            "id": int(post_id),
            "len": len(md_content),
            "mtime": post_mtime,
        }
        update_logs(post_data["md_name"], post_info, logs_info)
        logs_info["need_save"] = True

    # 输出结果
    fnLog("标题：" + post_data["title"])
    fnLog("状态：" + str(done))
    print("---")
    return True


def md_list_fn(posts_dir):
    """ 获取 md 文件列表并处理 """
    fnLog()
    fnLog("## 遍历文章处理：")
    md_list = get_md_list(posts_dir)
    for md_file in md_list:
        # 获取文件信息
        (md_name, md_mtime) = get_md_info(md_file)

        # 判断更新时间
        (log_msg, log_id) = check_logs(
            md_name, md_mtime, logs_info, debug_info["debug"])
        fnLog("### %s | %s | %s" % (md_name, log_id, fnGetTimeStr(md_mtime)),
              inspect.currentframe().f_lineno)
        if "skip" == log_msg:
            fnLog("无需同步")
            fnLog()
            continue
        if "update" == log_msg:
            fnLog("md 更新")
        else:
            fnLog("md 新增")

        # 读取 md 文件信息
        (md_content, md_meta) = get_md_content(md_file)

        # 判断内容格式
        if not any(md_meta):
            fnErr(["md 数据错误", md_file], inspect.currentframe().f_lineno)
            fnLog()
            continue

        # 文章发布/更新
        md_meta["log_id"] = log_id
        md_meta["md_name"] = md_name
        md_post_fn(md_content, md_meta, md_file)
        fnLog()
    # end for
    fnLog()
    save_logs(logs_info)
    fnLog("### 文章计数")
    fnBug(len(md_list), inspect.currentframe().f_lineno, debug_info["debug"])
    fnLog("共计：%s" % len(logs_info["list"]))
# 获取 md 文件列表并处理
