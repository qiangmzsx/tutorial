# -*- coding: utf-8 -*-  
""" 
数据库管理类 
"""  
import MySQLdb
from DBUtils.PooledDB import PooledDB  
 
  
# 数据库实例化类  
class DbManager(object):  
  
    def __init__(self):  
        connKwargs = {'host':'127.0.0.1', 'user':'root', 'port':3306, 'passwd':'root', 'db':'yii', 'charset':"utf8"}
        args = (10, 10, 30, 100, True, 0, None)  
        self._pool = PooledDB(MySQLdb, *args, **connKwargs)  
  
    def getConn(self):  
        return self._pool.connection()  
    
    def executeAndGetId(self, sql, param=None):  
        """ 执行插入语句并获取自增id """  
        conn = self.getConn()  
        cursor = conn.cursor()  
        if param == None:  
            cursor.execute(sql)  
        else:  
            cursor.execute(sql, param)  
        id = cursor.lastrowid  
        cursor.close()  
        conn.close()  
        return id
    
    def queryAll(self, sql):  
        """ 获取所有信息 """  
        conn = self.getConn()  
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  
        rowcount = cursor.execute(sql)  
        if rowcount > 0:  
            res = cursor.fetchall()  
        else:  
            res = None  
        cursor.close()  
        conn.close()  
        return res 
    
    def execute(self,sql, param=None):  
        """ 执行sql语句 """  
        conn = self.getConn()  
        cursor = conn.cursor()  
        if param == None:  
            rowcount = cursor.execute(sql)  
        else:  
            rowcount = cursor.execute(sql, param)  
        cursor.close()  
        conn.close()  
        return rowcount 
    
    def queryOne(self,sql):  
        """ 获取一条信息 """  
        conn = self.getConn()  
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)  
        rowcount = cursor.execute(sql)  
        if rowcount > 0:  
            res = cursor.fetchone()  
        else:  
            res = None  
        cursor.close()  
        conn.close()  
        return res  
 
  
  
if __name__ == "__main__":
    dbManager = DbManager()  
    res = dbManager.execute('select count(*) from douban')  
    print str(res)  
  
    res = dbManager.queryOne('select * from douban limit 20000, 1')  
    print str(res)  
  
    res = dbManager.queryAll('select * from douban limit 10')  
    print str(res)  
