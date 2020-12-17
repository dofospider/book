#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-13 00:07:24
lastTime: 2020-12-17 23:32:10
LastAuthor: Do not edit
'''
from flask import Flask,request
from flask.json import jsonify
from book import Book
from settings import BOOK_LIST

import json




app=Flask(__name__)

app.config['JSON_AS_ASCII']=False

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
            {"id":9,"text":'完本',"url":'/wanben'},
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
        print("in nomal case")
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
                pass
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
        print('in resdata')
        return jsonify(resData)

    


@app.route('/',methods=['GET','POST'] )
def hello_world():
    book=Book()
    arrData=book.get_books_info_limit()

    return jsonify(arrData)

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)