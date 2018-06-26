# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy




class SongspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    songname = scrapy.Field()
    length = scrapy.Field()
    songid = scrapy.Field()
    singerid = scrapy.Field()
    albumid=scrapy.Field()
    pass