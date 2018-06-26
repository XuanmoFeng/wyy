#coding =utf-8 
from scrapy_redis.spiders import RedisSpider
import json
import time
import re
from demz.items import *

class MySpider(RedisSpider):
    name = 'commentor'
    redis_key='commentor:start_urls'
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)
    def parse(self, response):
        pattern = re.compile(r'id=(\d+)')   # 查找数字
        wyyItem=DemzItem()
        wyyItem['userId'] = int(pattern.findall(response.url)[0])
        wyyItem['name']=response.xpath('//span[@class="tit f-ff2 s-fc0 f-thide"]/text()').extract_first()
        level=response.xpath('//span[@class="lev u-lev u-icn2 u-icn2-lev"]/text()').extract_first()
        if level!=None:
            wyyItem['level']=int(level)
        else:
            wyyItem['level']=None
        age=response.xpath('//span[@class="inf s-fc3"]/span[@class="sep"]/@data-age').extract_first()
        if age!=None:
            time_local = time.localtime(age)
            age = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        wyyItem['dt']=age
        city=response.xpath('//div[@class="inf s-fc3"]/span/text()').re(r'所在地区：\s*(.*)')
        if city:
            wyyItem['city']=city[0]
            wyyItem['province']=city[0]
        else:
            wyyItem['city']=None
            wyyItem['province']=None
        sex=response.xpath('//h2["j-name-wrap"]/i/@class').extract_first()
        if sex !=None:
            wyyItem['sex']=int(sex[-1:])
        event=response.xpath('//strong[@id="event_count"]/text()').extract_first()
        if event !=None:
           wyyItem['event']=int(event)
        else:
           wyyItem['event']=None
        follows=response.xpath('//strong[@id="follow_count"]/text()').extract_first()
        if follows!=None:
            wyyItem['follows']=follows
        else:
            wyyItem['follows']=None
        fans=response.xpath('//strong[@id="fan_count"]/text()').extract_first()
        if fans !=None:
            wyyItem['fans']=fans
        describe=response.xpath('//div[@class="inf s-fc3 f-brk"]/text()').re('个人介绍：\s*(.*)')
        if describe:
            wyyItem['describe']=describe[0]
        else:
            wyyItem['describe']=None
        wyyItem['weibo']=response.xpath('//a[@class="u-slg u-slg-sn"]/@href').extract_first()
        wyyItem['douban']=response.xpath('//a[@class="u-slg u-slg-db"]/@href').extract_first()
        yield wyyItem
