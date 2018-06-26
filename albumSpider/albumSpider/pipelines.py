# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import pymysql
import logging
from albumSpider import settings
class AlbumspiderPipeline(object):

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
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        try:
            self.cursor.execute(
                """select * from album where albumid = %s""",
                item['albumid'])
            repetition = self.cursor.fetchone()
            if repetition:
                pass
            else:
                self.cursor.execute(
                    """insert into album( albumid ,  singerid , albumname ,  albumtime ,albumpic )VALUES(%s,%s, %s, %s, %s)""",
                    (item['albumid'],
                     item['singerid'],
                        item['albumname'],
                        item['albumtime'],
                        item['albumpic']
                     ))
                self.connect.commit()
        except Exception as e:
            print(e)
        return item
