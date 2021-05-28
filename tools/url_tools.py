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
        ':path': '/x/space/arc/search?mid=927587&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp',
        ':scheme': 'https',
        'accept': 'pplication/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_uuid=5684A24D-7773-48CD-41ED-B20D86EF4A8721303infoc; buvid3=35035664-8C33-4314-A974-354FB09CEEC318548infoc; SESSDATA=68c64e01%2C1633442030%2Ca9ab2%2A41; bili_jct=48e7df40b7da901da605ac7cd18a4476; DedeUserID=22966665; DedeUserID__ckMd5=41ccbfc3c6acad03; sid=k4skmsrh; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(J|)J|uklmR0J\'uYu~)m||m~; LIVE_BUVID=AUTO9516178973626798; bp_article_offset_22966665=511327861028129310; CURRENT_QUALITY=120; fingerprint3=665c88ac1b283bfb4394c7e4d950fa9f; fingerprint_s=94f61fc6498e429f0b5396cd4aa68985; buvid_fp=78EC50F2-C67C-4A25-B185-3176F2DFCC6718544infoc; buvid_fp_plain=78EC50F2-C67C-4A25-B185-3176F2DFCC6718544infoc; bsource=search_baidu; fingerprint=ea9f3ce08744fb9cf7c64cbea6c501b3; bp_video_offset_22966665=515010168420848256; PVID=13; bp_t_offset_22966665=515028997550297903; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f',
        'origin': 'https://space.bilibili.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }