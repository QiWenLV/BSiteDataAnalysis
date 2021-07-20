
UP_VIDEO_LIST = "up_video_list"
UP_STAT = "up_stat"
UP_INFO = "up_info"
UP_FOLLOW = "up_follow"
VIDEO_C_INFO = "video_c_info"
VIDEO_DETAIL = "video_detail"
MYSELF_NEW_DYNAMIC = "myself_new_dynamic"
MYSELF_HIS_DYNAMIC = "myself_his_dynamic"

b_url = {
    # 动态列表(登入账号)
    MYSELF_NEW_DYNAMIC: "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid={}&type_list=8&jsonp=jsonp",
    MYSELF_HIS_DYNAMIC: "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_history?uid={}&offset_dynamic_id={}&type=8&from=&jsonp=jsonp",
    # up视频列表
    UP_VIDEO_LIST: "https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp",
    # up关注信息
    UP_STAT: "https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp",
    # up信息
    UP_INFO: "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp",
    # up关注列表
    UP_FOLLOW: "https://api.bilibili.com/x/relation/followings?vmid={}&pn={}&ps={}&order=desc&jsonp=jsonp",
    # 联合投稿up列表
    VIDEO_C_INFO: "https://api.bilibili.com/x/relation/relations?fids=285499073%2C19642758%2C13354765%2C7552204",
    # 视频详细信息
    VIDEO_DETAIL: "https://api.bilibili.com/x/web-interface/view/detail?bvid={}"
}