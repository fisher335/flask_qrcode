# coding:utf-8
import os
from flask import Flask
from config import RunConfig, DevConfig

app = Flask(__name__)
app.config.from_object(RunConfig)
from router import *

if __name__ == '__main__':
    app.run(debug=True)
