# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from albumSpider.items import *
from scrapy_redis.spiders import RedisSpider
class AlbumSpider(RedisSpider):
    name = 'album'
    redis_key = "albumsipder:strat_urls"
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(AlbumSpider, self).__init__(*args, **kwargs)
    def parse(self, response):
        selector = Selector(response=response)
        pattern =re.compile(r'id=(.*?)&')
        result1 = pattern.findall(response.url)
        albumname = selector.xpath(
            '//ul/li/div[@class="u-cover u-cover-alb3"]/@title').extract()
        albumid = selector.xpath(
            '//ul/li/div[@class="u-cover u-cover-alb3"]/a[@class="msk"]/@href').re(r'id=(.*)')
        albumpic = selector.xpath(
            '//ul/li/div[@class="u-cover u-cover-alb3"]/img/@src').extract()
        albumtime=selector.xpath(
        	'//ul/li/p/span[@class="s-fc3"]/text()').extract()
        for name, id, pic,time in zip(albumname, albumid, albumpic,albumtime):
            album = AlbumIdItem()
            album['albumname'] = name
            album['albumid'] = id
            album['albumpic'] = pic
            album['singerid']= result1[0]
            album['albumtime']=time
            yield album