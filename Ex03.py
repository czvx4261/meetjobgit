# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 20:26:34 2022

@author: Administrator
"""

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/news')

def news():
    return render_template('news.html')

app.run()

