# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import pymysql
import logging
from demz import settings
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
class DemzPipeline(object):
    def __init__(self):
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
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute(
                """select * from user where userId = %s""",
                item['userId'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                self.cursor.execute("""
                update user set name = %s, level = %s, dt = %s, province = %s,city=%s,sex=%s,event=%s,
                follows=%s,fans=%s,described=%s , weibo=%s , douban=%s where userId = %s""",( item['name'],
                     item['level'],
                     item['dt'],
                     item['province'],
                     item['city'],
                     item['sex'],
                     item['event'],
                     item['follows'],
                     item['fans'],
                     item['describe'],
                     item['weibo'],
                     item['douban'],
                     item['userId']
                     ))
            else:
                self.cursor.execute(
                    """insert into user( userId ,  name , level ,  dt  , province ,  city , sex , event , follows , fans , described , weibo , douban )VALUES(%s,%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (item['userId'],
                     item['name'],
                     item['level'],
                     item['dt'],
                     item['province'],
                     item['city'],
                     item['sex'],
                     item['event'],
                     item['follows'],
                     item['fans'],
                     item['describe'],
                     item['weibo'],
                     item['douban']
                     ))

            self.connect.commit()
        except Exception as error:
            # 出现错误时打印错误日志
            log.info("+++sql++++",error)
        return item
