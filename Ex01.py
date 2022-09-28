# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 20:01:23 2022

@author: Administrator
"""
# 宣告使用 flask
from flask import Flask

# 初始化 Flask 物件
app = Flask(__name__)

# 建立主網域的路徑
# @app.route("/callback") => linebot 寫的
# app.route 要對應一個函數
# 資料回傳根目錄
@app.route('/')

def home():
    return '這個是首頁'


app.run() # 執行
