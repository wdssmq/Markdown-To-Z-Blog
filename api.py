import os
import requests
import json
import time
import locale
import markdown
import frontmatter
import re

locale.setlocale(locale.LC_CTYPE, 'chinese')

config_info = {}

with open("config.json", 'rb') as f:
    config_info = json.loads(f.read())

# print(config_info)

# {
#     "USERNAME": "语言黑洞",
#     "PASSWORD": "addfwqevee",
#     "API-URL": "http://127.0.0.1:8000/edsa-demo/zb_system/api.php"
# }


def login():
    data = http("post", "member", "login", config_info)
    if not data is None:
        config_info["token"] = data["token"]
        config_info["AuthorID"] = data["user"]["ID"]
        print("登录成功")
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
    cate_id = 12
    author_id = config_info["AuthorID"]
    data_arg["CateID"] = cate_id
    data_arg["AuthorID"] = author_id
    data = http("post", "post", "post", data_arg)
    if not data is None:
        # 调试↓
        # print(data)
        print("提交成功")


def http(method, mod, act, data_arg={}):
    try:
        headers_arg = {"Authorization": "Bearer " + config_info["token"]}
    except:
        headers_arg = {}
        print("未登录")
    if method == "get":
        r = requests.get(config_info["API-URL"] + "?mod=" + mod +
                         "&act=" + act, params=data_arg, headers=headers_arg)
        # 调试↓
        # print(r.url)
    else:
        r = requests.post(config_info["API-URL"] + "?mod=" +
                          mod + "&act=" + act, data=data_arg, headers=headers_arg)

    rlt = r.json()

    # print(rlt)

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

    print(insert_info)

    new_readme_md_content = re.sub(
        r'---start---(.|\n)*---end---', insert_info, readme_md_content)

    with open(os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

    print("更新ReadMe成功")

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


def get_md_list(dir_path):
    md_list = []
    dirs = os.listdir(dir_path)
    for i in dirs:
        if os.path.splitext(i)[1] == ".md":
            md_list.append(os.path.join(dir_path, i))
    # print(md_list)
    return md_list
# 获取特定目录的markdown文件列表


def main():
    # 登录
    login()

    # 获取md文件列表并处理
    print("------")
    md_list = get_md_list(os.path.join(os.getcwd(), "_posts"))
    for md in md_list:
        md_name = os.path.basename(md)
        # 读取md文件信息
        (content, metadata) = read_md(md)
        # 获取title
        title = metadata.get("title", "")
        tags = metadata.get("tags", "")
        cate = metadata.get("categories", "")
        # 调试↓
        # print("%s%s" % (",".join(tags), cate))
        data_arg = {"Type": "0", "ID": 0, "Title": title,
                    "Content": content, "Tag": ",".join(tags)}
        # log
        print("文件名：%s \n 标题：%s" % (md_name, title))
        update_post(0, data_arg)
        print("---")
    print("------")
    # 更新最新文章到readme
    update_readme()
# 入口


main()
