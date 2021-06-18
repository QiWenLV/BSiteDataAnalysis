import math
import pandas as pd
from tools.common_tools import flat_json
from tools import url_tools
from common.constant import *
from persist.persist import IPersist


def get_v_detail(bivd, v_list_item):
    json_data = url_tools.http2json(b_url[VIDEO_DETAIL].format(bivd), url_tools.headers())["data"]
    view_data = parsing_view(json_data["View"])
    return dict(v_list_item, **view_data)


def parsing_view(json_data):
    """
    解析视频详细数据中View部分的数据
    :param json_data: View部分的数据
    :return:
    """
    # 视频数量，标签id，标签名称，上传时间，创建时间，未知，未知，up名称，
    # 播放数，弹幕库，当前弹幕池，收藏，硬币，转发，现在排名，
    # 历史排名，赞，踩，评分, bvid
    title_tag = ["videos", "tid", "tname", "pubdate", "ctime", "desc", "state", "duration", "owner#name",
                 "stat#view", "stat#danmaku", "stat#reply", "stat#favorite", "stat#coin", "stat#share", "stat#now_rank",
                 "stat#his_rank", "stat#like", "stat#dislike", "stat#evaluation", "cid"]
    # 压平json
    flat_data = flat_json(json_data)
    # 字段筛选
    return {title: flat_data[title] for title in title_tag}


def parsing_tag(json_data):
    pass
