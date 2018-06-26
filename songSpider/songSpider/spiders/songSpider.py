# coding:utf-8
import scrapy

from scrapy.selector import Selector
from selenium import webdriver
from songSpider.items import *
import re

from scrapy_redis.spiders import RedisSpider
class Song_Spider(RedisSpider):
	name = "song"
	def __init__(self):
		self.browser=webdriver.Firefox()
	redis_key = "songSpider:start_urls"
	def parse(self,response):
		pattern = re.compile(r'id=(\d+)')   # 查找数字
		albumid = int(pattern.findall(response.url)[0])
		self.browser.get(response.url)
		self.browser.switch_to_frame("contentFrame")
		selector = Selector(text=self.browser.page_source)
		songids = selector.xpath('//span[@class="txt"]/a/@href').re(r'id=(.*)')
		songnames = selector.xpath('//span[@class="txt"]/a/b/@title').extract()
		times=selector.xpath('//span[@class="u-dur "]/text()').extract()
		# singername=selector.xpath('//')
		singerid=selector.xpath('//div[@class="text"]/span/a/@href').re(r'id=(.*)')
		for (songid, songname,t) in zip(songids, songnames,times):
			song=SongspiderItem()
			song['songid']=songid
			song['songname']=songname
			song['length']=t
			song['albumid']=albumid
			song['singerid']=singerid[0]
			yield song
