# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    authStatus = scrapy.Field()
    avatarUrl = scrapy.Field()
    expertTags = scrapy.Field()
    experts = scrapy.Field()
    locationInfo = scrapy.Field()
    nickname = scrapy.Field()
    remarkName = scrapy.Field()
    userId = scrapy.Field()
    userType = scrapy.Field()
    vipType = scrapy.Field()


class SongComment(scrapy.Item):
    commentId = scrapy.Field()
    userId = scrapy.Field()
    songId = scrapy.Field()


class Comment(scrapy.Item):
    commentId = scrapy.Field()
    content = scrapy.Field()
    liked = scrapy.Field()
    likedCount = scrapy.Field()
    pendaneData = scrapy.Field()
    time = scrapy.Field()
    userId = scrapy.Field()
    beReplied = scrapy.Field()


class ReplyItem(scrapy.Item):
    commentId = scrapy.Field()
    content = scrapy.Field()
    userId = scrapy.Field()
