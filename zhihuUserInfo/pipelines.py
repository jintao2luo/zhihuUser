# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# import codecs
import pymongo
# from zhihuUserInfo import settings

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_username, mongo_pwd):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_username = mongo_username
        self.mongo_pwd = mongo_pwd

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_username=crawler.settings.get('MONGO_USERNAME'),
            mongo_pwd=crawler.settings.get('MONGO_PWD'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.client[self.mongo_db].authenticate(self.mongo_username, self.mongo_pwd, self.mongo_db,
                                                mechanism='SCRAM-SHA-1')
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #这里通过mongodb进行了一个去重的操作，每次更新插入数据之前都会进行查询，判断要插入的url_token是否已经存在，如果不存在再进行数据插入，否则放弃数据
        self.db['user'].update({'url_token': item["url_token"]},{'$set':item}, True)
        return item