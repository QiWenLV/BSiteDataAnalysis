
UP_VIDEO_LIST = "up_video_list"
UP_STAT = "up_stat"
UP_INFO = "up_info"

b_url = {
    # up视频列表
    UP_VIDEO_LIST:"https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn={}&keyword=&order=pubdate&jsonp=jsonp",
    # up关注信息
    UP_STAT:"https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp",
    # up信息
    UP_INFO:"https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp"
}