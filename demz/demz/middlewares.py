# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from .user_agents import agents
import base64
class ProxyMiddleWare(object):  
    """docstring for ProxyMiddleWare"""  
    def process_request(self,request, spider):  
        '''对request对象加上proxy'''  
        proxy = self.get_random_proxy()  
        print("this is request ip:"+proxy)  
        request.meta['proxy'] = proxy   


    def process_response(self, request, response, spider):  
        '''对返回的response处理'''  
        # 如果返回的response状态不是200，重新生成当前request对象  
        if response.status != 200:  
            proxy = self.get_random_proxy()  
            print("this is response ip:"+proxy)  
            # 对当前reque加上代理  
            request.meta['proxy'] = proxy   
            return request  
        return response  

    def get_random_proxy(self):  
        '''随机从文件中读取proxy'''  
        while 1:  
            with open('/home/ubuntu/fengkai/demz/demz/proxies.txt', 'r') as f:  
                proxies = f.readlines()  
            if proxies:  
                break  
            else:  
                time.sleep(1)  
        proxy = random.choice(proxies).strip()  
        return proxy 
#PROXIES = [
#    {'ip_port': '61.160.233.8', 'user_pass': ''},
#    {'ip_port': '125.93.149.186', 'user_pass': ''},
#    {'ip_port': '58.38.86.181', 'user_pass': ''},
#    {'ip_port': '119.142.86.110', 'user_pass': ''},
#    {'ip_port': '124.161.16.89', 'user_pass': ''},
#    {'ip_port': '61.160.233.8', 'user_pass': ''},
#    {'ip_port': '101.94.131.237', 'user_pass': ''},
#    {'ip_port': '219.157.162.97', 'user_pass': ''},
#    {'ip_port': '61.152.89.18', 'user_pass': ''},
##    {'ip_port': '139.224.132.192', 'user_pass': ''}
#    {'ip_port': '111.155.116.208', 'user_pass': ''}
#]
#class ProxyMiddleware(object):
#    def process_request(self, request, spider):
#        proxy = random.choice(PROXIES)
#        if proxy['user_pass'] is not None:
#            request.meta['proxy'] = "http://%s" % proxy['ip_port']
#            encoded_user_pass = base64.encodestring(proxy['user_pass'].encode('utf-8'))
#            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass.decode('utf-8')
#        else:
#            request.meta['proxy'] = "http://%s" % proxy['ip_port']
class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent

#class ProxyMiddleware(object):
#    def process_request(self, request, spider):
#        proxy = 'https://178.33.6.236:3128'     # 代理服务器
#        request.meta['proxy'] = proxy

class DemzDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
