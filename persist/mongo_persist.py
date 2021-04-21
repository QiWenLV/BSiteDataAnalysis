import pymongo
from persist import persist


class MongoPersist(persist.IPersist):

    def __init__(self):
        # 获取连接
        myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="root")
        # 获取数据库
        bili_db = myclient['bili_data']
        # 获取集合
        text_coll = bili_db["text_coll"]
        # 插入一条数据
        data = {"id": "1", "text": "aa"}
        x = text_coll.insert_one(data)
        print(x)

    def write(self):
        # v_list_coll = bili_db["v_list"]
        pass

    def read(self):
        pass
