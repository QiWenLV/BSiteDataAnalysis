import math
import pandas as pd

from tools import url_tools
from common.constant import *
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


def get_v_list_data(upid, iPersist: IPersist, increment=True):
    """
    获取视频列表
    :param upid: up主的mid
    :param iPersist: 存储器
    :param increment: 是否增量爬取
    :return:
    """
    headers = url_tools.headers()
    current_page_num = 1
    # 获取请求内容
    list_url = b_url[UP_VIDEO_LIST]
    json_data = url_tools.http2json(list_url.format(upid, current_page_num), headers)
    # 获取视频总数，每页容量，总页码
    video_count, page_capacity, page_total_num = parsing_page_number(json_data)
    # 判断增量更新(因为可能存在合作视频，视频数量可能不准确)。
    in_db_classify_data = iPersist.read('classify_data', {"mid": upid})
    in_db_count = 0 if in_db_classify_data.empty else in_db_classify_data["count"].sum()
    if increment:
        if video_count > in_db_count:
            diff_count = video_count - in_db_count
            page_total_num = diff_count // page_capacity + 1
            video_count = diff_count
        else:
            print(f"up:{upid}, 视频总数:{video_count}, 无需更新")
            return [], []
    print(f"up:{upid}, 需更新{video_count}个视频信息")
    # 获取视频分类信息
    pd_classify_data = parsing_data_classify(json_data)
    pd_classify_data['mid'] = upid
    # 获取第一页的视频列表信息
    pd_v_list_data = parsing_data_list(json_data)
    # 循环获取数据
    for i in range(1, page_total_num):
        current_page_num = i + 1
        json_data = url_tools.http2json(list_url.format(upid, current_page_num), headers)
        pd_v_list_data = pd_v_list_data.append(parsing_data_list(json_data))
    return pd_v_list_data, pd_classify_data


