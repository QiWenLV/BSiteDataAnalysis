import math
import pandas as pd

from tools import url_tools
from common.constant import b_url
from persist.persist import IPersist


def parsing_page_number(json_data):
    """
    解析页码
    :param json_data: 数据
    :return: 视频总数，每页容量，总页码
    """
    page_data = json_data["data"]["page"]
    video_count = page_data["count"]
    page_capacity = page_data["ps"]
    return video_count, page_capacity, math.ceil(video_count / page_capacity)


def parsing_data_classify(json_data):
    """
    解析视频分类信息
    :param json_data: 数据
    :return: pandas['tid', 'count', 'name']
    """
    classify_data = json_data["data"]["list"]["tlist"]
    return pd.DataFrame(classify_data.values())


def parsing_data_list(json_data):
    """
    解析视频列表信息
    :param json_data: 数据
    :return: pandas['comment', 'typeid', 'play', 'pic', 'subtitle', 'description',
       'copyright', 'title', 'review', 'author', 'mid', 'created', 'length',
       'video_review', 'aid', 'bvid', 'hide_click', 'is_pay', 'is_union_video',
       'is_steins_gate']
    """
    v_data_list = json_data["data"]["list"]["vlist"]
    return pd.DataFrame(v_data_list)


def get_v_list_data(upid, iPersist: IPersist):

    headers = {
        ':authority': 'api.bilibili.com',
        ':path': '/x/space/arc/search?mid=927587&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp',
        ':scheme': 'https',
        'accept': 'pplication/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_uuid=5684A24D-7773-48CD-41ED-B20D86EF4A8721303infoc; buvid3=35035664-8C33-4314-A974-354FB09CEEC318548infoc; SESSDATA=68c64e01%2C1633442030%2Ca9ab2%2A41; bili_jct=48e7df40b7da901da605ac7cd18a4476; DedeUserID=22966665; DedeUserID__ckMd5=41ccbfc3c6acad03; sid=k4skmsrh; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(J|)J|uklmR0J\'uYu~)m||m~; LIVE_BUVID=AUTO9516178973626798; bp_article_offset_22966665=511327861028129310; CURRENT_QUALITY=120; fingerprint3=665c88ac1b283bfb4394c7e4d950fa9f; fingerprint_s=94f61fc6498e429f0b5396cd4aa68985; buvid_fp=78EC50F2-C67C-4A25-B185-3176F2DFCC6718544infoc; buvid_fp_plain=78EC50F2-C67C-4A25-B185-3176F2DFCC6718544infoc; bsource=search_baidu; fingerprint=ea9f3ce08744fb9cf7c64cbea6c501b3; bp_video_offset_22966665=515010168420848256; PVID=13; bp_t_offset_22966665=515028997550297903; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f',
        'origin': 'https://space.bilibili.com',
        'referer': f'https://space.bilibili.com/{upid}/video?tid=0&keyword=&order=pubdate',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
    }
    current_page_num = 1
    list_url = b_url["up_video_list"]
    # 获取请求内容
    json_data = url_tools.http2json(list_url.format(upid, current_page_num), headers)
    # 获取视频总数，每页容量，总页码
    video_count, page_capacity, page_total_num = parsing_page_number(json_data)
    # 获取视频分类信息
    pd_classify_data = parsing_data_classify(json_data)
    # 获取第一页的视频列表信息
    pd_v_list_data = parsing_data_list(json_data)
    # 循环获取数据
    for i in range(page_total_num) - 1:
        current_page_num = i + 2
        json_data = url_tools.http2json(list_url.format(upid, current_page_num), headers)
        pd_v_list_data.append(parsing_data_list(json_data))

    iPersist.write()

