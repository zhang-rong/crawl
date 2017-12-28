# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
# from images.items import ImagesItem

from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class ImagesPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        db = client['meizitu']
        self.collection = db['images']

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert(data)
        return item



