#coding =utf-8
from scrapy_redis.spiders import RedisSpider
import json
import time
import re
from master.items import UserItem,Comment,SongComment 
from Wyy import WangYiYun
import scrapy
class CommentSpider(RedisSpider):
    name = 'comment'
    page = 1
    url=""
    redis_key="comment:start_url"
    def make_requests_from_url(self,url):
        self.url=url
        music = WangYiYun()
        print(url)
        text = music.create_random_16()
        rid = re.findall(r"comments/(.*?)\?", url)[0]
        params = music.get_params(rid, text, self.page)
        encSecKey = music.get_encSEcKey(text)
        fromdata = {'params': params, 'encSecKey': encSecKey}
        
        return scrapy.FormRequest(
            url=url,
            formdata=fromdata,
            callback=self.parse_page
            )

    def __get_jsons(self):
        music = WangYiYun()
        print(self.url)
        text = music.create_random_16()
        rid = re.findall(r"comments/(.*?)\?", self.url)[0]
        params = music.get_params(rid, text, self.page)
        encSecKey = music.get_encSEcKey(text)
        fromdata = {'params': params, 'encSecKey': encSecKey}
        print(fromdata )
        return scrapy.FormRequest(
            url=self.url,
            formdata=fromdata,
            callback=self.parse_page
            )

    def parse_page(self, response):
        jsons = json.loads(response.body.decode('utf-8'))
        jsons = json.dumps(jsons)
        comments = self.json2list(jsons)
        for i in comments:
            yield i
            if len(i) <10:
                print('评论已经获取完')
        else:
            self.page += 1
            yield self.__get_jsons()

    def json2list(self, jsons):
        users = json.loads(jsons)
        comment=Comment()
        user =UserItem()
        song=SongComment()
        for a in users['comments']:
            userT=a['user'];
            user['userId'] = userT['userId']
            song['userId']=int(user['userId'])
            rid = re.findall(r"comments/R_SO_4_(.*?)\?", self.url)[0]
            song['songId']=rid
            user['avatarUrl']=userT['avatarUrl']
            user['expertTags']=userT['expertTags']
            user['experts']=userT['experts']
            user['avatarUrl']=userT['avatarUrl']
            user['locationInfo']=userT['locationInfo']
            user['nickname']=userT['nickname']
            user['remarkName']=userT['remarkName']
            user['userType']=userT['userType']
            user['vipType']=userT['vipType']
            user['authStatus']=userT['authStatus']
            comment['commentId']=a['commentId']
            song['commentId']=int(comment['commentId'])
            comment['content']=a['content']
            comment['liked']=a['liked']
            comment['pendaneData']=a['pendantData']
            comment['likedCount']=a['likedCount']
            time_local = time.localtime(a['time']/1000)
            comment['time'] = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            reply=a['beReplied']
            if reply:
                comment['beReplied']=1
            else:
                comment['beReplied']=0
            comment['userId']=userT['userId']
            yield user
            yield comment
            yield song
