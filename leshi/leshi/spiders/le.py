import scrapy
from leshi.items import LeshiItem
from scrapy.http import Request
import json


class LeSpider(scrapy.Spider):
    name = 'le'
    allowed_domains = ['http://www.le.com']
    # start_urls = ['http://www.le.com/']
    tv = 'http://list.le.com/apin/chandata.json?c=2&d=1&md=&o=20&p={}&s=1'
    movie = 'http://list.le.com/apin/chandata.json?c=1&d=1&md=&o=9&p={}&s=1'
    comic = 'http://list.le.com/apin/chandata.json?c=5&d=1&md=&o=20&p={}&s=1'

    start_urls = []

    tv_num = range(1,20)
    movie_num = range(1,20)
    # 动漫
    comic_num = range(1,21)

    for i in tv_num:
        start_urls.append(tv.format(str(i)))
    for i in movie_num:
        start_urls.append(movie.format(str(i)))
    for i in comic_num:
        start_urls.append(comic.format(str(i)))


    def parse(self, response):
        js = json.loads(response.text)['data_list']
        for x in js:
            item = LeshiItem()
            category = x['categoryName']
            name = x['name']
            aid_url = 'http://www.le.com/tv/' + str(x['aid']) + '.html'
            image = sorted(x['images'].items())[0]
            title = x['subname']
            type = x['subCategoryName']
            area = x['areaName']
            play_num = x['playCount']
            score =  x['rating']
            # div_urls = x['divs']
            item['category'] = category
            item['name'] = name
            item['aid_url'] = aid_url
            item['image'] = image
            item['title'] = title
            item['type'] = type
            item['area'] = area
            item['play_num'] = play_num
            item['score'] = score
            # item['div_urls'] = div_urls
            yield item




