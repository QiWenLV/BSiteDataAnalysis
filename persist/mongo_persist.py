import pymongo
from persist import persist
import json
import pandas as pd


class MongoPersist(persist.IPersist):

    def __init__(self):
        # 获取连接
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="root")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # 获取数据库
        self.bili_db = myclient['bili_data']

    def write(self, to_sink, data, index=None):
        coll_curr = self.bili_db[to_sink]
        json_data = json.loads(data.to_json(orient='records', lines=False))
        if index is None or index == "":
            coll_curr.insert_many(json_data)
            return
        def_filter = None
        if type(index) == str:
            def_filter = lambda item: {index: item[index]}
        elif type(index) == list:
            def_filter = lambda item: {i: item[i] for i in index}
        bulkWriteResult = coll_curr.bulk_write([pymongo.UpdateOne(def_filter(item), {"$set": item}, upsert=True) for item in json_data])
        print(f"写入{bulkWriteResult.upserted_count()}条数据")

    def read(self, source, filter):
        coll_curr = self.bili_db[source]
        result = pd.DataFrame([item for item in coll_curr.find(filter)])
        result.drop(columns="_id", inplace=True)
        return result

    def count(self, source, filter) -> int:
        coll_curr = self.bili_db[source]
        return coll_curr.count(filter)
