import math
import pandas as pd
from common.constant import *
from tools.common_tools import flat_json

from tools import url_tools
from common.constant import b_url


def get_up_info(upid):
    headers = url_tools.headers()
    # 获取请求内容
    json_up_stat = url_tools.http2json(b_url[UP_STAT].format(upid), headers)
    json_up_info = url_tools.http2json(b_url[UP_INFO].format(upid), headers)
    # {"mid":13354765,"following":66,"whisper":0,"black":0,"follower":6277735}
    if json_up_info is None:
        print("获取up信息失败")
    return dict(flat_json(json_up_info["data"]), **json_up_stat["data"])



