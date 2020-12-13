#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-13 00:07:14
lastTime: 2020-12-14 00:46:15
LastAuthor: Do not edit
'''
from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE,MYSQL_CHARSET


class Book(object):
    """
    book base class
    """
    def __init__(self,):
        """
        init class
        """
        self.conn=connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset=MYSQL_CHARSET,


            )

        self.cursor=self.conn.cursor(DictCursor)
        pass

    def __del__(self, ):
        """
        distrol class
        """
        self.cursor.close()
        self.conn.close()

        pass

    def get_books_info_limit(self, ):
        """
        docstring
        """
        sql='select * from book_infos limit 3'
        self.cursor.execute(sql)
        data=[]

        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)

        return data

