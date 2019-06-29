# -*- coding:utf-8 -*-   Date   : '2015/8/12 0012 * 10:47'
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
from app import view
