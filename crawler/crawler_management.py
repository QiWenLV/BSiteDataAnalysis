from crawler.crawler_video_list import *
from crawler.crawler_up_stat import *
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist
from persist.csv_persist import CsvPersist


def crawler(upid, iPersist: IPersist):
    # up账号信息
    iPersist.write('up_info', get_up_info(upid), index="mid")
    # 视频列表信息
    pd_v_list_data, pd_classify_data = get_v_list_data(upid, mongo_persist, increment=False)
    iPersist.write('up_video_list', pd_v_list_data, index="bvid")
    iPersist.write('classify_data', pd_classify_data, index=["mid", "tid"])



if __name__ == '__main__':
    upid = 176037767
    mongo_persist = MongoPersist()

    up_stat_data = get_up_info(upid)
    mongo_persist.write("up_info", up_stat_data, index="mid")
    # crawler(upid, mongo_persist)
