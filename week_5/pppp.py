
from splinter.driver.webdriver.chrome import Options, Chrome
from splinter.browser import Browser
from contextlib import closing
import requests, json, time, re, os, sys, time
from bs4 import BeautifulSoup
def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    相当于客户端请求
    """
    return dict(line.split(": ", 1) for line in header_raw.split("\n"))

class DouYin(object):
    def __init__(self, width=500, height=300):
        """
        抖音App视频下载
        """
        # 无头浏览器
        chrome_options = Options()
        chrome_options.add_argument(
            'user-agent="com.ss.android.ugc.aweme/400 (Linux; U; Android 8.1.0; zh_CN; vivo Z1; Build/OPM1.171019.011; Cronet/58.0.2991.0)"')

        # self.driver = Browser(driver_name='chrome', executable_path='E:/Program Files (x86)/Google/Chrome/Application/chromedriver', options=chrome_options)
        self.driver = Browser(driver_name='chrome',
                              executable_path='/usr/local/bin/chromedriver',
                              options=chrome_options)
    def get_video_urls(self, user_id):
        """
        获得视频播放地址
        Parameters:
            user_id：查询的用户ID
        Returns:
            video_names: 视频名字列表
            video_urls: 视频链接列表
            nickname: 用户昵称
        """
        video_names = []
        video_urls = []
        un_watermark_url = []
        unique_id = ''
        while unique_id != user_id:
            search_url = 'https://api.amemv.com/aweme/v1/discover/search/?cursor=0&keyword=%s&count=10&type=1&is_pull_refresh=1&hot_search=0&search_source=find_friends&ts=1546862651&js_sdk_version=1.6.4&app_type=normal&manifest_version_code=390&_rticket=1546862652557&ac=wifi&device_id=61169876551&iid=55828869798&mcc_mnc=46001&os_version=8.1.0&channel=update&version_code=390&device_type=AWM-A0&language=zh&uuid=867693040182341&resolution=1080*2160&openudid=34124b9fe8b35bb7&update_version_code=3902&app_name=aweme&version_name=3.9.0&os_api=27&device_brand=blackshark&ssmix=a&device_platform=android&dpi=420&aid=1128&as=a1854453fbd3bc70c34699&cp=483fc65fb2323101e1Sy[g&mas=01a5b8073feec0967d1a375f621da2c36f9c9c6c2cccc60cecc646' % user_id
            raw_headers = """Host: api-hl.amemv.com
Connection: keep-alive
Cookie: install_id=55828869798; ttreq=1$5e9bba290ae1cd73b87266b881a070510969e4b3; sid_tt=7a2e178963209222b89b867481848c35; sessionid=7a2e178963209222b89b867481848c35; odin_tt=b486d50c6d81ba953d9ab9a821b640f01e37bc2d98dc5218e6debd5a9b84e708392b13edba9d4576b4c2d4e75927de7c; sid_guard=7a2e178963209222b89b867481848c35%7C1546853627%7C5184000%7CFri%2C+08-Mar-2019+09%3A33%3A47+GMT; uid_tt=4aa1b339b1d4b15ad1b370401e87c370
Accept-Encoding: gzip
X-SS-REQ-TICKET: 1546862652551
X-Tt-Token: 007a2e178963209222b89b867481848c350ba5b0f5789f5ac1053061a054ffe14be153a440305585a48a1af846c6b6ed4a5a
sdk-version: 1
X-SS-TC: 0
User-Agent: com.ss.android.ugc.aweme/390 (Linux; U; Android 8.1.0; zh_CN; AWM-A0; Build/G66T1810252CN00MP1; Cronet/58.0.2991.0)"""
            headers =get_headers(raw_headers)
            req = requests.get(url=search_url,headers=headers, verify=False)
            html = json.loads(req.text)
            aweme_count = html['user_list'][0]['user_info']['aweme_count']
            uid = html['user_list'][0]['user_info']['uid']
            nickname = html['user_list'][0]['user_info']['nickname']
            unique_id = html['user_list'][0]['user_info']['unique_id']

        i = 1
        aweme_count = 20  #每次请求下载20个视频
        max_cursor = 0   #下载初始值
        while True:


            # user_url = 'https://www.douyin.com/aweme/v1/aweme/post/?user_id=%s&max_cursor=0&count=%s' % (uid, aweme_count)
            user_url ='https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=%d&user_id=%s&count=%d&retry_type=no_retry&mcc_mnc=46001&iid=55828869798&device_id=61169876551&ac=wifi&channel=update&aid=1128&app_name=aweme&version_code=390&version_name=3.9.0&device_platform=android&ssmix=a&device_type=AWM-A0&device_brand=blackshark&language=zh&os_api=27&os_version=8.1.0&uuid=867693040182341&openudid=34124b9fe8b35bb7&manifest_version_code=390&resolution=1080*2160&dpi=420&update_version_code=3902&_rticket=1546860526995&ts=1546860527&js_sdk_version=1.6.4&as=a155a3a3cf9ecc97838799&cp=3aecc359f6323372e1OgWk&mas=019aa95abcb034855eda789a557d0e1e4e9c9cec1ccc1cec9cc6c6'% (max_cursor,uid, aweme_count)
            # headers ={'Host': 'api.amemv.com', 'Connection': 'keep-alive', 'Cookie': 'install_id=55828869798; ttreq=1$5e9bba290ae1cd73b87266b881a070510969e4b3; sid_tt=7a2e178963209222b89b867481848c35; sessionid=7a2e178963209222b89b867481848c35; odin_tt=b486d50c6d81ba953d9ab9a821b640f01e37bc2d98dc5218e6debd5a9b84e708392b13edba9d4576b4c2d4e75927de7c; sid_guard=7a2e178963209222b89b867481848c35%7C1546853627%7C5184000%7CFri%2C+08-Mar-2019+09%3A33%3A47+GMT; uid_tt=4aa1b339b1d4b15ad1b370401e87c370', 'Accept-Encoding': 'gzip', 'X-Tt-Token': '007a2e178963209222b89b867481848c350ba5b0f5789f5ac1053061a054ffe14be153a440305585a48a1af846c6b6ed4a5a', 'sdk-version': '1', 'X-SS-TC': '0', 'User-Agent': 'com.ss.android.ugc.aweme/390 (Linux; U; Android 8.1.0; zh_CN; AWM-A0; Build/G66T1810252CN00MP1; Cronet/58.0.2991.0)'}

            req = requests.get(url=user_url, headers=headers,verify=False)
            html = json.loads(req.text)


            for each in html['aweme_list']:
                share_desc = each['share_info']['share_desc']
                if '抖音-原创音乐短视频社区' == share_desc:
                    video_names.append(str(i) + '.mp4')
                    i += 1
                else:
                    video_names.append(share_desc +'_'+str(i)+ '.mp4')
                    i += 1
                video_urls.append(each['share_info']['share_url'])
                un_watermark_url.append(each['video']['play_addr']['url_list'][0])  #无水印链接，加个list保存这个链接，之后就可以直接用
            if html['has_more']!=1:
                break;
            max_cursor = html['max_cursor']


        return video_names, video_urls, nickname,un_watermark_url

    def get_download_url(self, video_url):
        """
        获得带水印的视频播放地址
        Parameters:
            video_url：带水印的视频播放地址
        Returns:
            download_url: 带水印的视频下载地址
        """
        headers = {
            'user-agent': 'com.ss.android.ugc.aweme/400 (Linux; U; Android 8.1.0; zh_CN; vivo Z1; Build/OPM1.171019.011; Cronet/58.0.2991.0)'
        }
        req = requests.get(url=video_url,headers=headers, verify=False)

        bf = BeautifulSoup(req.text, 'lxml')
        script = bf.find_all('script')[-1]
        video_url_js = re.findall(' playAddr: ".+?"',str(script),re.DOTALL)[0]
        # video_html = json.loads(video_url_js[8:])
        # download_url = video_html['video']['play_addr']['url_list'][0]

        return video_url_js[12:-1]
    def video_downloader(self, video_url, video_name,un_watermark_url=None, watermark_flag=True):
        """
        视频下载
        Parameters:
            video_url: 带水印的视频地址
            video_name: 视频名
            watermark_flag: 是否下载不带水印的视频
        Returns:
            无
        """
        size = 0
        if watermark_flag == True:
            # video_url = self.remove_watermark(video_url)
            video_url = un_watermark_url
        else:
            video_url = self.get_download_url(video_url)
        headers = {
            'user-agent': 'com.ss.android.ugc.aweme/400 (Linux; U; Android 8.1.0; zh_CN; vivo Z1; Build/OPM1.171019.011; Cronet/58.0.2991.0)'
        }
        with closing(requests.get(video_url, stream=True,headers=headers, verify=False)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                sys.stdout.write('  [文件大小]:%0.2f MB\n' % (content_size / chunk_size / 1024))

                with open(video_name, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        file.flush()

                        sys.stdout.write('  [下载进度]:%.2f%%' % float(size / content_size * 100) + '\r')
                        sys.stdout.flush()

    def remove_watermark(self, video_url):
        """
        获得无水印的视频播放地址
        Parameters:
            video_url: 带水印的视频地址
        Returns:
            无水印的视频下载地址
        """
        self.driver.visit('http://douyin.iiilab.com/')
        self.driver.find_by_tag('input').fill(video_url)
        self.driver.find_by_xpath('//button[@class="btn btn-default"]').click()
        html = self.driver.find_by_xpath('//div[@class="thumbnail"]/div/p')[0].html
        bf = BeautifulSoup(html, 'lxml')
        return bf.find('a').get('href')

    def run(self):
        """
        运行函数
        Parameters:
            None
        Returns:
            None
        """
        # self.hello()
        # user_id = input('请输入ID(例如40103580):')
        user_id = '1749761959'
        video_names, video_urls, nickname,un_watermark_url = self.get_video_urls(user_id)
        if nickname not in os.listdir():
            os.mkdir(nickname)
        print('视频下载中:共有%d个作品!\n' % len(video_urls))
        for num in range(len(video_urls)):
            print('  解析第%d个视频链接 [%s] 中，请稍后!\n' % (num + 1, video_urls[num]))
            if '\\' in video_names[num]:
                video_name = video_names[num].replace('\\', '')
            elif '/' in video_names[num]:
                video_name = video_names[num].replace('/', '')
            else:
                video_name = video_names[num]
            self.video_downloader(video_urls[num], os.path.join(nickname, video_name),un_watermark_url[num],True)
            print('\n')

        print('下载完成!')


if __name__ == '__main__':
    douyin = DouYin()
    douyin.run()