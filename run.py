#-*- coding: utf-8 -*-
# @Date    : '2018/8/15 0015'
# @Author  : Terry feng  (fengshaomin@qq.com)
# -*- coding: utf-8 -*-
# @Date    : 2017/7/17 0017 , @Author  : fengshaomin@bjsasc.com
from gevent import monkey

monkey.patch_all()
from app import app
import  logging
import getopt
import sys
from gevent.pool import Pool
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':

    addr, port = '127.0.0.1', 8080
    opts, _ = getopt.getopt(sys.argv[1:], "b:")
    for opt, value in opts:
        if opt == '-b':
            addr, port = value.split(":")

    pool = Pool(256)
    server = WSGIServer((addr, int(port)), app, spawn=pool)
    server.backlog = 256
    server.max_accept = 30000
    logging.basicConfig(level='DEBUG')
    logging.info('http://{addr}:{port}'.format(addr=addr,port=port))
    server.serve_forever()
