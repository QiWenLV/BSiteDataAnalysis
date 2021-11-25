import pymongo
from persist import persist
import json
import pandas as pd


class MongoPersist(persist.IPersist):

    def __init__(self):
        # 获取连接
        myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="root")
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # 获取数据库
        self.bili_db = myclient['bili_data']

    def write(self, to_sink, data, index=None):
        coll_curr = self.bili_db[to_sink]
        # 将数据转换为  [{'a': 1}, {'a': 2}] 格式
        if type(data) == pd.DataFrame:
            data = data.to_dict(orient='records')
        elif type(data) == dict:
            data = [data]
        elif data is None:
            print("数据为空, 无法写入")
            return
        # json_data = json.loads(data.to_json(orient='records', lines=False))
        if index is None or index == "":
            coll_curr.insert_many(data)
            return
        def_filter = None
        if type(index) == str:
            def_filter = lambda item: {index: item[index]}
        elif type(index) == list:
            def_filter = lambda item: {i: item[i] for i in index}
        if len(data) == 0:
            print("sink:{}, 输入数据集为空".format(to_sink))
            return
        bulkWriteResult = coll_curr.bulk_write([pymongo.UpdateOne(def_filter(item), {"$set": item}, upsert=True) for item in data])
        print("sink:{}, 匹配{}条数据".format(to_sink, bulkWriteResult.matched_count))
        print("sink:{}, 写入{}条数据".format(to_sink, bulkWriteResult.upserted_count))
        print("sink:{}, 修改{}条数据".format(to_sink, bulkWriteResult.modified_count))

    def read(self, source, filter):
        coll_curr = self.bili_db[source]
        result = pd.DataFrame([item for item in coll_curr.find(filter)])
        if not result.empty:
            result.drop(columns="_id", inplace=True)
        return result

    def count(self, source, filter) -> int:
        coll_curr = self.bili_db[source]
        return coll_curr.count(filter)
