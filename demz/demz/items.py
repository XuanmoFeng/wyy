# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemzItem(scrapy.Item):
    # 电影名字
    userId= scrapy.Field()
    name= scrapy.Field()
    level= scrapy.Field()
    dt= scrapy.Field()
    province= scrapy.Field()
    city= scrapy.Field()
    sex= scrapy.Field()
    event= scrapy.Field()
    follows= scrapy.Field()
    fans= scrapy.Field()
    describe= scrapy.Field()
    weibo= scrapy.Field()
    douban= scrapy.Field()
