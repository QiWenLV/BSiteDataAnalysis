import requests
from bs4 import BeautifulSoup
import json


def http2json(url, header):
    response = requests.get(url, header)
    if requests is None:
        print(f"{__name__}: 请求错误")
    return json.loads(response.text)

def headers():
    return {
        ':authority': 'api.bilibili.com',
        ':path': '/dynamic_svr/v1/dynamic_svr/dynamic_history?uid=22966665&offset_dynamic_id=544170960545081763&type=8&from=&platform=web',
        ':scheme': 'https',
        'accept': 'pplication/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': "l=v; _uuid=F8667130-2265-A571-2531-C3F135313E2D49379infoc; buvid3=8E2D7209-C2EC-4A9E-BAC7-CEB3FABE4E1313441infoc; fingerprint=5a866b4a943c7accd52cbee2cf405149; buvid_fp=8E2D7209-C2EC-4A9E-BAC7-CEB3FABE4E1313441infoc; buvid_fp_plain=747FE9AD-8C06-47E5-9445-9A4B34F0674C34778infoc; SESSDATA=6dbd0a1a%2C1639279559%2Cc99db%2A61; bili_jct=c64cc9435f45afca9b36c477e4665746; DedeUserID=22966665; DedeUserID__ckMd5=41ccbfc3c6acad03; sid=anln2xdj; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um~u)RmJlJ0J'uYkJ~RlR~k; bp_video_offset_22966665=544265299500177611; PVID=1; bp_t_offset_22966665=544265299500177611",
        'origin': 'https://space.bilibili.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }