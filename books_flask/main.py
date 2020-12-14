#!/usr/bin/env python
# coding=UTF-8
'''
Author: dofospider
since: 2020-12-13 00:07:24
lastTime: 2020-12-15 00:45:43
LastAuthor: Do not edit
'''
from flask import Flask
from flask.json import jsonify
from book import Book


app=Flask(__name__)

app.config['JSON_AS_ASCII']=False


@app.route('/',methods=['GET','POST'] )
def hello_world():
    book=Book()
    arrData=book.get_books_info_limit()

    return jsonify(arrData)

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)