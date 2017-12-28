# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from images.items import ImagesItem
import scrapy.cmdline


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['meizitu.com']
    meizitu = 'http://www.meizitu.com/a/more_{}.html'
    start_urls = []

    for i in range(1,73):
        start_urls.append(meizitu.format(i))

    def parse(self, response):
        data = response.xpath('//div[@class="pic"]')
        for x in data:
            item = ImagesItem()
            name = x.xpath('./a/img/@alt').extract()[0]
            images = x.xpath('./a/@href').extract()[0]
            images_urls = x.xpath('./a/img/@src').extract()[0]
            item['name'] = name
            item['images'] = images
            item['images_urls'] = images_urls
            yield item


#调试
def main():
    scrapy.cmdline.execute(['scrapy','crawl','meizitu'])

if __name__ == '__main__':
    main()