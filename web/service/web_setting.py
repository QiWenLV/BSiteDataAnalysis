from aiohttp import web
from browser.open_dynamic import open_myself_dynamic, to_obtain_dynamic_list
import datetime
from common.web_result import *
from config.setting import *
from persist.pickle_persist import PicklePersist
import time

pickle_persist = PicklePersist()
setting = Setting()


async def set_seting_kv(req):
    """
    设置键值对参数
    /api/setting/kv
    """
    req_data = await req.json()
    setting.set(Group.config, req_data["key"], req_data["value"])
    return web.json_response(result("ok"))
