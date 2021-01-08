#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-13 00:07:24
lastTime: 2021-01-09 01:23:50
LastAuthor: Do not edit
'''
from flask import Flask,request
from flask.json import jsonify
from book import Book
from settings import BOOK_LIST

import json
import re



app=Flask(__name__)

app.config['JSON_AS_ASCII']=False

def is_string_validate(str):
    sub_str=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str)==len(sub_str):
        return False
    else:
        return True

@app.route('/books_cates',methods=['GET'])
def get_books_cates():
    """
    docstring
    """
    resData={
        "resCode":0,
        "data":[
            {"id":0,"text":'首页',"url":'/'},
            {"id":1,"text":'玄幻',"url":'/xuanhuan'},
            {"id":2,"text":'修真',"url":'/xiuzhen'},
            {"id":3,"text":'都市',"url":'/dushi'},
            {"id":4,"text":'历史',"url":'/lishi'},
            {"id":5,"text":'网游',"url":'/wangyou'},
            {"id":6,"text":'科幻',"url":'/kehuan'},
            {"id":7,"text":'言情',"url":'/yanqing'},
            {"id":8,"text":'其他',"url":'/qita'},
            {"id":9,"text":'完本',"url":'/quanben'},
        ],
        "message":'对本次请求的说明'
    }

    return jsonify(resData)


@app.route('/<string:book_cate>',methods=['POST'])
def get_cates_infos(book_cate):

    """
    docstring
    """
    if request.method=='POST':
        pass
        # print("in nomal case")
        get_data=json.loads(request.get_data(as_text=True))
        key=get_data['key']

        if book_cate in BOOK_LIST:

            if key =='newest':
                
                book=Book()
                sqldata=book.get_cates_newest_books_30(book_cate)
                resData={
                    "resCode":0,
                    "data":sqldata,
                    "message":'the newest refresh book information'
                }
                return jsonify(resData)
                pass
            elif key=='most':
                book=Book()
                sqldata=book.get_cates_most_books_30(book_cate)
                resData={
                    "resCode":0,
                    "data":sqldata,
                    "message":'the most views book information' 
                }
                return jsonify(resData) 
            else:
                resData={
                    "resCode":2,
                    "data":[],
                    "message":'error prament',
                }

            return jsonify(resData) 
        else:
            return {"resCode":404}
    else:
        resData={
            "resCode":1,
            "data":[],
            "message":'request function error!',
        }
        # print('in resdata')
        return jsonify(resData)

    


@app.route('/',methods=['GET','POST'] )
def hello_world():
    book=Book()
    arrData=book.get_books_info_limit()

    return jsonify(arrData)

@app.route('/book/<int:book_id>',methods=['POST'])
def get_book_infos_by_id(book_id):
    """
    book profoment infomation
    """
    if request.method=='POST':
        get_data=json.loads(request.get_data(as_text=True))
        key=get_data['key']
        secretKey=get_data['secretKey']
        if key=='index':
            book=Book()
            try:
                
                sql_data=book.get_book_infos_by_book_id(book_id)
                if sql_data==[]:
                    raise IndexError('error index')
            except Exception as r:
                
                resData={
                    "resCode":1,
                    "data":[],
                    "message":'error'
                    }
                return jsonify(resData)
            else:
                resData={
                    "resCode":0,
                    "data":sql_data,
                    "message":'book information'
                }
                return jsonify(resData)
            pass
        elif key =='cap20':
            book=Book()
            try:
                
                sql_data=book.get_book_infos_by_book_id(book_id)
                # print(sql_data)
                if sql_data==[]:
                    raise IndexError('error index')
            except Exception as r:
                
                resData={
                    "resCode":1,
                    "data":[],
                    "message":'r'
                    }
                return jsonify(resData)
            else:

                cap_20_data=book.get_book_newest_20_caps_by_book_id(book_id)   
                resData={
                    "resCode":0,
                    "data":cap_20_data,
                    "message":'all capter information'
                    }
                return jsonify(resData)
        elif key == 'all':
            book=Book()
            try:
                
                sql_data=book.get_book_infos_by_book_id(book_id)
                if sql_data==[]:
                    raise IndexError('error index')
            except Exception as r:
                
                resData={
                    "resCode":1,
                    "data":[],
                    "message":'r'
                    }
                return jsonify(resData)
            else:

                all_cap_data=book.get_book_all_caps_by_book_id(book_id)   
                # print(all_cap_data) 
                resData={
                    "resCode":0,
                    "data":all_cap_data,
                    "message":'all capter information'
                    }
                return jsonify(resData)
        else:
            resData={
                "resCode":1,
                "data":[],
                "message":'error default'
            }
            return jsonify(resData)

    else:
        resData={
            "resCode":1,
            "data":[],
            "message":'request function error!',
        }
        return jsonify(resData)

@app.route('/book/<int:book_id>/<int:sort_id>',methods=['POST'])
def get_book_detail_infos(book_id,sort_id):
    """
    get_book_detail_infos
    """
    if request.method=='POST':
        book=Book()
        sql_book_id_data=book.get_book_infos_by_book_id(book_id)
        if len(sql_book_id_data)==0:
            resData={
                "resCode":1,
                "data":[],
                "message":'error book infos',
            }
            # print('ee')
            return jsonify(resData)
        
        sort_book_details=book.get_book_detail_by_book_id_sort_id(book_id,sort_id)
        try:
            preItems=book.get_pre_cap_id(book_id,sort_id)[0]['sort_id']
        except Exception  as identifier:
            preItems=''
        else:
            preItems

        try:
            nextItems=book.get_next_cap_id(book_id,sort_id)[0]['sort_id']
        except Exception as identifier:
            nextItems=''
        else:
            nextItems

        sort_book_details[0]['book_name']=sql_book_id_data[0]['book_name']
        sort_book_details[0]['pre_id']=preItems
        sort_book_details[0]['next_id']=nextItems
        # print(sort_book_details)
        resData={
            "resCode":0,
            "data":sort_book_details,
            "message":'all book infos',
        }
        # print(sql_book_id_data)
        # print(sort_book_details)
        return jsonify(resData)
    else:
        resData={
            "resCode":1,
            "data":[],
            "message":'request function error!',
        }
        return jsonify(resData)
        
@app.route('/search',methods=['POST'])
def serach_info():
    if request.method =='POST':
        get_data=json.loads(request.get_data(as_text=True))
        key=get_data['key']
        secretKey=get_data['secretKey']
        if is_string_validate(key):
            resData={
                "resCode":1,
                "data":[],
                "message":'error param',
            }
        book=Book()
        search_data=book.search_infos_by_key(key)
        if len(search_data)==0:
            resData={
                "resCode":0,
                "data":[],
                "message":'empty data!'
            }
            return jsonify(resData)
        resData={
            "resCode":0,
            "data":search_data,
            "message":'search resoult'

        }
        return jsonify(resData)


    else:
        resData={
            "resCode":1,
            "data":[],
            "message":'request fun error!'
        }
        
        return jsonify(resData)

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)