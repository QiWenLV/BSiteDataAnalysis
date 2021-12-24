from aiohttp import web
from browser.open_dynamic import open_myself_dynamic, to_obtain_dynamic_list
import datetime
from common.web_result import *
from config.setting import *
from crawler.crawlet_up_follows import get_my_follows, get_follow_tags
from persist.pickle_persist import PicklePersist
import time

pickle_persist = PicklePersist()
setting = Setting()
file_name = "my_star_list_setting.data"


async def get_case_list(req):
    """
    获取关注列表
    /api/case/list
    """
    up_follows_data = get_my_follows(setting.get(Group.config, Key.myid))
    follow_tags_data = get_follow_tags()
    data = pickle_persist.read(file_name)

    if len(data) == 0:
        # 创建文件
        pickle_persist.write(up_follows_data_2_data(up_follows_data))
    # 准备一个新dict，接收更新后的数据
    rst_data = {}
    for item in up_follows_data:
        mid = item["mid"]
        if data.get(mid) is None:
            data[mid] = "0"
        item["type"] = data[mid]
        rst_data[mid] = data[mid]
    # 保存更新后的数据
    pickle_persist.write(file_name, rst_data)

    # 组织返回数据结构
    tag_dict = {}
    for index, tag in enumerate(follow_tags_data):
        tag['list'] = []
        tag_dict[tag['tagid']] = index

    for item in up_follows_data:
        if item['tag'] is None:
            follow_tags_data[tag_dict[0]]['list'].append(item)
        else:
            for t in item['tag']:
                follow_tags_item = follow_tags_data[tag_dict.get(t) if tag_dict.get(t) is not None else tag_dict[0]]
                follow_tags_item['list'].append(item)
    return web.json_response(result(up_follows_data))


async def set_change_one(req):
    """
    更改一个关注up的关注类型 [0=正常，1=特别关注，2=黑名单]
    /api/case/change?upid=[]
    """
    req_data = await req.json()
    data = pickle_persist.read(file_name)
    data[req_data["mid"]] = req_data["type"]
    pickle_persist.write(file_name, data)
    return web.json_response(result())


async def get_case_tags_list(req):
    """
    获取分组
    /api/case/tags
    """
    req_data = await req.json()
    return web.json_response(result())

def up_follows_data_2_data(up_follows_data):
    return {i["mid"]: "0" for i in up_follows_data}
