from crawler.crawler_video_list import *
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist


if __name__ == '__main__':
    upid = '927587'
    mongo_persist = MongoPersist()
    get_v_list_data(upid, mongo_persist)