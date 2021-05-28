from crawler.crawler_video_list import *
from crawler.crawler_up_stat import *
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist
from persist.csv_persist import CsvPersist


if __name__ == '__main__':
    upid = 176037767
    mongo_persist = MongoPersist()
    # up粉丝信息
    pd_up_stat_data = get_up_stat(upid)
    # 列表信息
    pd_v_list_data, pd_classify_data = get_v_list_data(upid, mongo_persist, increment=False)
    # 写入数据
    mongo_persist.write('up_info', pd_up_stat_data, index="mid")
    mongo_persist.write('up_video_list', pd_v_list_data, index="bvid")
    mongo_persist.write('classify_data', pd_classify_data, index=["mid", "tid"])

