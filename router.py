# -*- coding: utf-8 -*-
# @Date    : '2018/4/16 0016'
# @Author  : Terry feng  (fengshaomin@qq.com)
from app import app
from flask import request, render_template, redirect, url_for, send_from_directory, make_response
import qrcode
import os, time
from random import randint
import json
import requests

c_pa = os.path.dirname(__file__)
static_path = c_pa + os.sep + "static"

DOWNLOAD_PATH = r'D:\用户目录\下载'


@app.route('/list/', methods=['GET'])
def list_header():
    return render_template('list.html', session=request.headers)


@app.route('/wiki/')
def upload():
    return redirect("https://github.com/fisher335/wiki/issues")


@app.route('/')
@app.route('/index/')
@app.route('/qrcode/', methods=['GET'])
def index():
    return render_template("index.html")


#
#
@app.route('/qrcode/', methods=['POST'])
def qrcodelike():
    url = request.form.get('url', "")
    print(url.encode("utf-8"))
    img_name = randint(1, 1000000)
    imge = qrcode.make(url)
    pa = static_path + os.sep + 'qrcode' + os.sep + str(img_name) + ".png"

    print(pa)
    imge.save(pa)
    return render_template('qrcode.html', img=img_name)


@app.route('/upload/', methods=['get'])
def upload_get():
    return render_template('upload.html')


@app.route('/upload/', methods=['post'])
def upload_post():
    f = request.files['file']
    file_name = f.filename
    print(file_name)
    # f.save(static_path + os.sep + 'videos' + os.sep + file_name)
    f.save(os.path.join(DOWNLOAD_PATH,file_name))
    return redirect('/file/')


@app.route('/file/', methods=['get'])
def file_list():
    li_file = []
    # video_path = static_path + os.sep + 'videos'
    for path, dir, file in os.walk(DOWNLOAD_PATH):
        for i in file:
            li_file.append(i)
    return render_template('file.html', files=li_file)


@app.route('/download/<filename>/', methods=['get'])
def download_file(filename):
    video_path = static_path + os.sep + 'qrcode'
    print(filename)
    return send_from_directory(video_path, filename=filename, as_attachment=True)


@app.route('/zhuang/', methods=['get'])
def dazhuang():
    return render_template('zhuang.html')


@app.route('/ip/', methods=['get'])
def get_ip():
    my_ip = requests.get('http://jsonip.com').json()['ip']
    return make_response(my_ip)


@app.route('/downloadfile/<filename>/', methods=['get'])
def download_uploaded_file(filename):

    print(filename)
    return send_from_directory(DOWNLOAD_PATH, filename=filename, as_attachment=True)
