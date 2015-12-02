# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class XiciPipeline(object):
 
    def __init__(self):
        self.file = codecs.open('qq.cvs', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
        
        
# from twisted.enterprise import adbapi
# import MySQLdb.cursors
# from bokeh.properties import String
#  
# class XiciPipeline(object):
#  
#     def __init__(self):
#         import sys
#         reload(sys)
#         sys.setdefaultencoding('utf-8')
#         self.dbpool = adbapi.ConnectionPool('MySQLdb', db='yii',
#                 user='root', passwd='root', cursorclass=MySQLdb.cursors.DictCursor,
#                 charset='utf8', use_unicode=True)
#  
#     def process_item(self, item, spider):
#         # run db query in thread pool
#         query = self.dbpool.runInteraction(self._conditional_insert, item)
#         query.addErrback(self.handle_error)
#  
#         return item
#  
#     def _conditional_insert(self, tx, item):
#         sql = "insert into `douban` (`title`, `messages`,`star`,`assess`) values ('"+str(item['title'])+"', '"+str(item['messages'])+"', '"+str(item['star'])+"','"+str(item['assess'][0])+"')";
#         
#         print sql
#         tx.execute(sql)
#         #(item['title'],item['messages'],item['star'],item['assess'])
#     def handle_error(self, e):
#         print e
