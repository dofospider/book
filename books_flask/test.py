#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-28 00:18:41
lastTime: 2020-12-28 00:48:29
LastAuthor: Do not edit
'''
from book import Book


if  __name__ == "__main__":
    book=Book()
    sql_data=book.get_book_infos_by_book_id(281832)
    all_cap_data=book.get_book_all_caps_by_book_id(281832)
    print(sql_data)
    print(all_cap_data)
    try:
        
        if sql_data ==[]:
            raise IndexError('error number')
    except Exception     as e:
        print(e)
    else:
        print('ok')