import math
import pandas as pd
from common.constant import *

from tools import url_tools
from common.constant import b_url
def get_up_stat(upid):
    headers = url_tools.headers()
    # 获取请求内容
    json_up_stat = url_tools.http2json(b_url[UP_STAT].format(upid), headers)
    json_up_info = url_tools.http2json(b_url[UP_INFO].format(upid), headers)
    # {"code":0,"message":"0","ttl":1,"data":{"mid":13354765,"following":66,"whisper":0,"black":0,"follower":6277735}}
    dp_up_stat = pd.DataFrame(json_up_stat["data"])
    dp_up_info = pd.DataFrame(json_up_stat["data"])
    print('')
    return

def parsing_up_info(json_up_info):
    json_up_info["data"]
    """
    {
    "code":0,
    "message":"0",
    "ttl":1,
    "data":{
        "mid":13354765,
        "name":"徐大虾咯",
        "sex":"男",
        "face":"http://i1.hdslb.com/bfs/face/c44a60be5d81ed32a50578b394e50e104e8ea2f7.jpg",
        "sign":"微博@徐大虾咯咯丨商务合作请联系WX:xudaxiawork丨QQ2673049513",
        "rank":10000,
        "level":6,
        "jointime":0,
        "moral":0,
        "silence":0,
        "birthday":"10-07",
        "coins":0,
        "fans_badge":true,
        "official":{
            "role":1,
            "title":"bilibili 2020百大UP主、2019年度原创栏目奖UP主",
            "desc":"",
            "type":0
        },
        "vip":{
            "type":2,
            "status":1,
            "due_date":1642262400000,
            "vip_pay_type":1,
            "theme_type":0,
            "label":{
                "path":"",
                "text":"年度大会员",
                "label_theme":"annual_vip",
                "text_color":"#FFFFFF",
                "bg_style":1,
                "bg_color":"#FB7299",
                "border_color":""
            },
            "avatar_subscript":1,
            "nickname_color":"#FB7299",
            "role":3,
            "avatar_subscript_url":"http://i0.hdslb.com/bfs/vip/icon_Certification_big_member_22_3x.png"
        },
        "pendant":{
            "pid":2100,
            "name":"BML2020暗黑版",
            "image":"http://i1.hdslb.com/bfs/garb/item/6de2948bdf4b19112b06f899c88063dea4643ad7.png",
            "expire":0,
            "image_enhance":"http://i1.hdslb.com/bfs/garb/item/6de2948bdf4b19112b06f899c88063dea4643ad7.png",
            "image_enhance_frame":""
        },
        "nameplate":{
            "nid":8,
            "name":"知名偶像",
            "image":"http://i0.hdslb.com/bfs/face/27a952195555e64508310e366b3e38bd4cd143fc.png",
            "image_small":"http://i0.hdslb.com/bfs/face/0497be49e08357bf05bca56e33a0637a273a7610.png",
            "level":"稀有勋章",
            "condition":"所有自制视频总播放数\u003e=100万"
        },
        "user_honour_info":{
            "mid":0,
            "colour":null,
            "tags":null
        },
        "is_followed":true,
        "top_photo":"http://i2.hdslb.com/bfs/space/1501b105b903e6b2fa5c210aa67e1b5c2c58fc26.png",
        "theme":{

        },
        "sys_notice":{

        },
        "live_room":{
            "roomStatus":1,
            "liveStatus":0,
            "url":"https://live.bilibili.com/1319010",
            "title":"小玩",
            "cover":"http://i0.hdslb.com/bfs/live/new_room_cover/4fc1f0796b8c995c29fb9df7b8ac95f1fe3332bd.jpg",
            "online":314616,
            "roomid":1319010,
            "roundStatus":0,
            "broadcast_type":0
        }
    }
}
    """