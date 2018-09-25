# -*- coding: utf-8 -*-
# @Date    : '2018/9/25 0025'
# @Author  : Terry feng  (fengshaomin@qq.com)

class BasicConfig:
    '''必须用英文，中文路径会有错，file.save会报错'''
    pass


class DevConfig(BasicConfig):
    HOST='127.0.0.1'
    PORT = 8080
    DOWNLOAD_PATH = r'D:\MyDrivers'

class RunConfig(BasicConfig):
    HOST='O.0.0.O'
    PORT = 7000
    DOWNLOAD_PATH = r'D:\MyDrivers'