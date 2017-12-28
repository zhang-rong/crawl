# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.utils.project import get_project_settings


settings = get_project_settings()

class LeshiPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        db = client['leshi']
        self.collection = db['data']

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert(data)
        return item