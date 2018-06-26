# -*- coding: utf-8 -*-
import random
import base64
from queue import Queue
import redis
import time
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
# class ProxyMiddleware(object):
#     def __init__(self, settings):
#         self.queue = 'songsipder:strat_url'
#         # 初始化代理列表
#         self.r = redis.Redis(host=settings.get('REDIS_HOST'),port=settings.get('REDIS_PORT'),db=1)

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings)

#     def process_request(self, request, spider):
#         proxy={}
#         source, data = self.r.blpop(self.queue)
#         proxy['ip_port']=data
#         proxy['user_pass']=None

#         if proxy['user_pass'] is not None:
#             #request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']
#             #proxy_user_pass = "USERNAME:PASSWORD"
#             encoded_user_pass = base64.encodestring(proxy['user_pass'])
#             request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#             print ("********ProxyMiddleware have pass*****" + proxy['ip_port'])
#         else:
#             #ProxyMiddleware no pass
#             print (request.url, proxy['ip_port'])
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']

#     def process_response(self, request, response, spider):
#         """
#         检查response.status, 根据status是否在允许的状态码中决定是否切换到下一个proxy, 或者禁用proxy
#         """
#         print("-------%s %s %s------" % (request.meta["proxy"], response.status, request.url))
#         # status不是正常的200而且不在spider声明的正常爬取过程中可能出现的
#         # status列表中, 则认为代理无效, 切换代理
#         if response.status == 200:
#             print ('rpush',request.meta["proxy"])
#             self.r.rpush(self.queue, request.meta["proxy"].replace('http://','')) 
#         return response

#     def process_exception(self, request, exception, spider):
#         """
#         处理由于使用代理导致的连接异常
#         """
#         proxy={}
#         source, data = self.r.blpop(self.queue)
#         proxy['ip_port']=data
#         proxy['user_pass']=None

#         request.meta['proxy'] = "http://%s" % proxy['ip_port']
#         new_request = request.copy()
#         new_request.dont_filter = True
#         return new_request
class SeleniumMiddleware(object):
    def process_request(self,request,spider):
        try:
            spider.browser.get(request.url)
            spider.browser.switch_to_frame("contentFrame")
        except Exception as e:
            print("selenium error")
        return HtmlResponse(url=spider.browser.current_url,body=spider.browser.page_source,encoding="utf-8", request=request)