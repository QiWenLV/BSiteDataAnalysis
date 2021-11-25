import webbrowser as web
import datetime
import demjson
from tools import url_tools
from common.constant import *

DYNAMIC_URL = "https://www.bilibili.com/video/"


def to_obtain_dynamic_list(last_time: datetime.datetime, limit=100):
    myid = "22966665"
    # 获取最新动态
    data = url_tools.http2json(b_url[MYSELF_NEW_DYNAMIC].format(myid), url_tools.user_agent(), url_tools.cookies())['data']
    # 继续获取动态的offset
    next_offset = data['history_offset']
    cards = data['cards']
    # 需要打开的页面数
    open_count = 0
    wait_open_url_list = []
    is_down = True
    while is_down:
        rst_list, is_down, open_count = collect_url(cards, last_time, open_count, limit)
        next_data = url_tools.http2json(b_url[MYSELF_HIS_DYNAMIC].format(myid, next_offset), url_tools.user_agent(),
                                        url_tools.cookies())['data']
        wait_open_url_list += rst_list
        cards = next_data['cards']
        next_offset = next_data['next_offset']
    print("总计获取{}个视频链接".format(open_count))
    return wait_open_url_list



def collect_url(cards, last_time: datetime.datetime, open_count, limit):
    wait_open_url_list = []
    is_down = True
    for card in cards:
        if int(card['desc']['timestamp']) > last_time.timestamp() and open_count < limit:
            video_desc = demjson.decode(card['card'].replace('\n', '').replace('\r\n', ''))
            wait_open_url_list.append({
                'bvid': card['desc']['bvid'],
                'up': card['desc']['user_profile']['info']['uname'],
                'time': datetime.datetime.fromtimestamp(card['desc']['timestamp']),
                'title': video_desc['title'],
                'url': video_desc['short_link'],
                'like': video_desc['stat']['like'],
                'coin': video_desc['stat']['coin'],
                'favorite': video_desc['stat']['favorite'],
                'view': video_desc['stat']['view'],
                'videos': video_desc['videos'],
                'mid': video_desc['owner']['mid']
            })
            open_count += 1
        else:
            is_down = False
            break
    return wait_open_url_list, is_down, open_count


def open_myself_dynamic(wait_open_url_list):
    web.register("edge", None, web.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
    bro_inst = web.get("edge")
    for item in wait_open_url_list:
        bro_inst.open(item)
    print("打开完成，共打开了{}个页面".format(len(wait_open_url_list)))

if __name__ == '__main__':
    to_obtain_dynamic_list(datetime.datetime(2021, 7, 19, 22, 0, 0))