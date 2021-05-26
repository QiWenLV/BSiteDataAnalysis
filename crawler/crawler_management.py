from crawler.crawler_video_list import *
from persist.persist import IPersist
from persist.mongo_persist import MongoPersist
from persist.csv_persist import CsvPersist


if __name__ == '__main__':
    upid = '927587'
    mongo_persist = MongoPersist()
    csv_persist = CsvPersist('csv')
    get_v_list_data(upid, mongo_persist)

    a = mongo_persist.read("up_video_list", {"mid":int(upid)})
    print(a.count())
