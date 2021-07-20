from common.constant import *

from tools import url_tools
from common.constant import b_url



def get_up_follows(upid):
    """
    获取up的关注列表
    :param upid:
    :return:
    """
    title_tag = ["mid", "attribute", "mtime", "tag", "special", "uname"]
    # 计算关注量(因为B站限制只能查看5页)
    follow_data = url_tools.http2json(b_url[UP_FOLLOW].format(upid, 1, 1), url_tools.headers())
    if follow_data["data"] is None:
        print(follow_data['message'])
        return
    follow_total = follow_data["total"]
    ps = follow_total // 4
    # 获取请求内容
    follows_list = []
    for i in range(1, 6):
        json_up_follows = url_tools.http2json(b_url[UP_FOLLOW].format(upid, i, ps), url_tools.headers())
        for item in json_up_follows["data"]["list"]:
            data_dict = {title: item[title] for title in title_tag}
            data_dict["upid"] = upid
            follows_list.append(data_dict)
    return follows_list
