# -*- conding:utf-8 -*-

import time
import requests
import json



#请求
def grab_favorite(self, user_id, max_cursor=0):
    favorite_params = self.FAVORITE_PARAMS
    favorite_params['user_id'] = user_id
    favorite_params['max_cursor'] = max_cursor
    query_params = {favorite_params, self.common_params}
    sign = getSign(self.gettoken(), query_params)
    params = {query_params, sign}
    resp = requests.get(self.FAVORITE_URL,
                        params=params,
                        verify=False,
                        headers=self.HEADERS)

    favorite_info = resp.json()

    hasmore = favorite_info.get('hasmore')
    max_cursor = favorite_info.get('max_cursor')

    video_infos = favorite_info.get('aweme_list')

    for per_video in video_infos:
        author_nickname = per_video['author'].get("nickname")
        author_uid = per_video['author'].get('uid')
        video_desc = per_video.get('desc')
        download_item = {
            "author_nickname": author_nickname,
            "video_desc": video_desc,
            "author_uid": author_uid,
        }
        awemeid = per_video.get("awemeid")
        self.download_favorite_video(awemeid, download_item)
        time.sleep(5)

    return hasmore, max_cursor




#翻页
def grab_favorite_main(self, user_id):
    count = 1
    self.logger.info("当前正在爬取第 👉 {} 👈 页内容...".format(count))
    hasmore, max_cursor = self.grab_favorite(user_id)
    while hasmore:
        count += 1
        self.logger.info("当前正在爬取第 👉 {} 👈 页内容...".format(count))
        hasmore, max_cursor = self.grab_favorite(user_id, max_cursor)




#视频下载
def download_favorite_video(self, awemeid, video_infos):
    video_content = self.download_video(awemeid)
    author_nickname = video_infos.get("author_nickname")
    author_uid = video_infos.get("author_uid")
    video_desc = video_infos.get("video_desc")
    video_name = "".join(author_nickname, author_uid, video_desc)

    self.logger.info("download_favorite_video 正在下载视频 {} ".format(video_name))

    if not video_content:
        self.logger.warn("你正在下载的视频，由于某种神秘力量的作用，已经凉凉了，请跳过...")
        return

    with open("../videos/{}.mp4".format(video_name), 'wb') as f:
        f.write(video_content)

def download_video(self, awemeid, retrytimes=0):
    query_params = self.common_params
    query_params['awemeid'] = awemeid

    sign = getSign(self.gettoken(), query_params)
    params = {query_params, sign}

    postdata = {
        "awemeid": awemeid
    }

    resp = requests.get(self.VIDEO_DETAILURL,
                        params=params,
                        data=post_data,
                        verify=False,
                        headers=self.HEADERS)
    resp_result = resp.json()
    play_addr_raw = resp_result['aweme_detail']['video']['play_addr']['url_list']

    content = requests.get(play_addr).content

    return content