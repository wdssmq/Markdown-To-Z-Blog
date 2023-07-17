""" 通用函数封装 """
import os

# pylint: disable=invalid-name

def fnEmpty():
    """ 占位空函数 """
    return 1
# 什么也不做


def fnLog(msg="", tip=None, log_type=""):
    """ 输出信息 """
    if not tip is None:
        tip = f" ← {tip}"
    else:
        tip = ""
    if isinstance(msg, list):
        rlt = ""
        for x in msg:
            if not any(rlt):
                rlt += str(x)
            else:
                rlt = rlt + "，" + str(x)
        msg = rlt
    if isinstance(msg, int):
        msg = str(msg)
    if not any(msg):
        print("")
    else:
        print(f"_{log_type}{msg}{tip}")
# 输出信息


def fnBug(msg, tip=None, debug=True):
    """ 调试信息输出 """
    if debug:
        fnLog(msg, tip, "[debug]")
# 调试信息输出


def fnErr(msg, tip=None):
    """ 错误信息 """
    fnLog(msg, tip, "_[err]")
# 错误信息


def fnGetDirsInDir(path):
    """ 获取子文件夹 """
    return [x for x in os.listdir(path) if os.path.isdir(x)]
# 获取子文件夹


def fnGetFilesInDir(path):
    """ 获取文件夹中的文件 """
    return [x for x in os.listdir(path) if not os.path.isdir(x)]
# 获取文件夹中的文件


def fnGetFilesInDir2(path, ext):
    """ 获取指定后缀的文件 """
    return [x for x in os.listdir(path) if not os.path.isdir(x) and os.path.splitext(x)[1] == ext]
# 获取指定后缀的文件


def fnGetFileTime(file):
    """ 获取文件时间 """
    mtime = os.stat(file).st_mtime  # 文件的修改时间
    ctime = os.stat(file).st_ctime  # 文件的创建时间
    return (int(mtime), int(ctime))
# 获取文件时间
