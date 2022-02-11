from aiohttp import web
from browser.open_dynamic import open_myself_dynamic, to_obtain_dynamic_list
import datetime
from common.web_result import *
from config.setting import *
import time
from functools import reduce


setting = Setting()

DYNAMIC_URL = "https://www.bilibili.com/video/"


async def get_home_table(req):
    """
    获取动态列表
    /api/{date}/{limit}
    """
    start_timestamp = req.match_info['date']
    limit = req.match_info['limit']
    # 保存当前时间
    scan_time = time.mktime(datetime.datetime.now().timetuple())
    # 获取动态列表
    wait_open_url_list = to_obtain_dynamic_list(datetime.datetime.fromtimestamp(int(start_timestamp)), int(limit))
    new_s = []  # 存储去重后的数据
    for i in wait_open_url_list:
        i['time'] = int(i['time'].timestamp())
        if any(str(d.get('bvid', None)).lower() == str(i['bvid']).lower() for d in new_s):
            pass
        else:
            new_s.append(i)
    return web.json_response(result({"list": new_s, "scan_time": scan_time}))


# async def get_home_table(req):
#     return web.json_response({"a":"a"})


async def post_open_dynamic(req):
    """
    打开动态
    /api/open?scan_time=[]&limit=[]
    """
    start_timestamp = req.query.get("scan_time")
    limit = req.query.get("limit")
    data = await req.json()
    open_myself_dynamic([DYNAMIC_URL + item for item in data])

    setting.set(Group.dynamic, Key.last_time, start_timestamp)
    setting.set(Group.dynamic, Key.limit_num, limit)
    return web.json_response(result())


async def get_home_param(req):
    """
    获取初始化参数(scan_time, limit)
    /api/home_param
    """
    return web.json_response(result(
        {"scan_time": setting.get(Group.dynamic, Key.last_time), "limit": setting.get(Group.dynamic, Key.limit_num)}))
