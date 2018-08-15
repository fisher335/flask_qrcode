import  os
from flask import Flask

from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = Flask(__name__)

from router import *



if __name__ == '__main__':
    app.run(debug=True)

