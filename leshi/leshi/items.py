# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LeshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    aid_url = scrapy.Field()
    # div_urls = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    play_num = scrapy.Field()
    score = scrapy.Field()
