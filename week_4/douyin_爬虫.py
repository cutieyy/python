#!/usr/bin/env python3
# coding:utf-8
# @Time :10/11/18 21:03


import logging
import os
import time
import json
import copy
import re
import sys
from logging.handlers import RotatingFileHandler

sys.path.append("..")
import logging
import os

sys.path.append('../')
sys.path.append('../../')

#from www_douyin_com.spiders.douyin_crawl import DouyinCrawl

def getLogger(task_name="root", level=logging.INFO, console_out=False):
    logger = logging.getLogger(task_name)
    if isinstance(level, str):
        level = level.lower()
    if level == "debug":
        level = logging.DEBUG
    elif level == "info":
        level = logging.INFO
    elif level == "warning":
        level = logging.WARNING
    elif level == "error":
        level = logging.ERROR
    else:
        level = logging.INFO

    if not os.path.exists("../logs"):
        os.makedirs("../logs")
    LOG_FILE = "../logs/%s.log" % task_name
    fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=64 * 1024 * 1025, backupCount=5, encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if console_out is True:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    logger.setLevel(level)
    return logger

class DouyinCrawl(object):
    logger = getLogger("DouyinCrawl", console_out=True)

    # headers
    __HEADERS = {"User-Agent": "Aweme/2.7.0 (iPhone; iOS 11.0; Scale/2.00)"}
    # __HEADERS = {"User-Agent": "Aweme/2.8.0 (iPhone; iOS 12.0; Scale/2.00)"}

    # params
    __FOLLOW_LIST_PARAMS = {
        "count": "20",
        "offset": "0",
        "user_id": None,
        "source_type": "2",
        "max_time": int(time.time()),
    }

    __COMMENT_LIST_PARAMS = {
        "count": "20",
        "cursor": "0",
        "comment_style": '2',
        "aweme_id": None,
        "digged_cid": "",
    }

    __USER_VIDEO_PARAMS = {
        "count": "21",
        # "offset": "0",
        "user_id": None,
        # "max_cursor": str(int(time.time())) + "000",
        "max_cursor": "0",
    }


douyin_crawl = DouyinCrawl()

argv_execute = sys.argv[1:-1]

if len(sys.argv) < 3:
    print("请输入正确的参数：如 python video_download_run.py -one 6610886853165845773")

allow_execute = ["-one", "-ulike", "-upost", "-m"]

if not all(map(lambda x: x in allow_execute, argv_execute)):
    print("请输入正确的限制命令：当前仅支持 -one 、-m 、 -ulike 和 -upost")

if "-one" in argv_execute:
    print("正在下载...")
    douyin_crawl.download_one_video(sys.argv[-1])
    print("下载完成...")

if "-upost" in argv_execute:
    if not "-m" in argv_execute:
        douyin_crawl.grab_user_media(sys.argv[-1], "USER_POST")
    else:
        douyin_crawl.grab_user_media(sys.argv[-1], "USER_POST", content='-m')

if sys.argv[1] == "-ulike":
    if not "-m" in argv_execute:
        douyin_crawl.grab_user_media(sys.argv[-1], "USER_LIKE")
    else:
        douyin_crawl.grab_user_media(sys.argv[-1], "USER_LIKE", content='-m')










