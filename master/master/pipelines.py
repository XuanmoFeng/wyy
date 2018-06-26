# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import pymysql
import logging
import os
from master import settings
from master.items import *
import redis
logging.basicConfig(authStatus=logging.INFO,
                    format='%(asctime)s - %(name)s - %(authStatusname)s - %(message)s')
log = logging.getLogger(__name__)


class DemzPipeline(object):
    def __init__(self):
        self.conn = redis.Redis(host='112.74.173.89',port=6379)
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            if isinstance(item, UserItem):
                self.cursor.execute("""select * from user where userId = %s""",item['userId'])
                repetition = self.cursor.fetchone()
                url='http://music.163.com/user/home?id=%s'%item['userId'] #
                self.conn.lpush('commentor:start_urls',url) #
                if repetition:
                    self.cursor.execute("""update user set name = %s, authStatus = %s, avatarUrl = %s,
                                        expertTags = %s,experts=%s,locationInfo=%s,remarkName=%s,
                                        userType=%s,vipType=%s where userId = %s""",
                                        (item['nickname'],
                                         item['authStatus'],
                                         item['avatarUrl'],
                                         item['expertTags'],
                                         item['experts'],
                                         item['locationInfo'],
                                         item['remarkName'],
                                         item['userType'],
                                         item['vipType'],
                                         item['userId']))
                else:
                    self.cursor.execute("""insert into user(userId,avatarUrl,expertTags,experts,
                                        locationInfo,name,remarkName,authStatus,userType,vipType)
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                        (item['userId'],
                                         item['avatarUrl'],
                                         item['expertTags'],
                                         item['experts'],
                                         item['locationInfo'],
                                         item['nickname'],
                                         item['remarkName'],
                                         item['authStatus'],
                                         item['userType'],
                                         item['vipType']))

            elif isinstance(item, Comment):
                self.cursor.execute("""select * from comment where commentId = %s""",item['commentId'])
                repetition = self.cursor.fetchone()
                if repetition:
                    pass
                else:
                    self.cursor.execute("""insert into comment(commentId,content,liked,likedCount,
                                        pendaneData,time,userId,beReplied)
                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                                        (item['commentId'],
                                         item['content'],
                                         item['liked'],
                                         item['likedCount'],
                                         item['pendaneData'],
                                         item['time'],
                                         item['userId'],
                                         item['beReplied']))
            elif isinstance(item, ReplyItem):
                self.cursor.execute("""select * from reply where commentId = %s""", item['commentId'])
                repetition = self.cursor.fetchone()
                if repetition:
                    pass
                else:
                    self.cursor.execute("""insert into reply(commentId,content,userId)
                                        VALUES(%s,%s,%s)""",
                                        (item['commentId'],
                                         item['content'],
                                         item['userId']))
            elif isinstance(item,SongComment):
                self.cursor.execute("""select * from song_coment where commentId =%s""",item['commentId'])
                repetition=self.cursor.fetchone()
                if repetition:
                    pass
                else:
                    self.cursor.execute("""insert into song_coment(commentId,userId,songId)VALUES(%s,%s,%s)""",
                        (item['commentId'],item['userId'],item['songId']))
            self.connect.commit()
        except Exception as e:
            log.error(e)
        return item
