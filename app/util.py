# coding:utf-8
from aip import AipOcr


class OcrClient:
    """ 你的 APPID AK SK """
    APP_ID = '16667601'
    API_KEY = 'T3xjr0oIM7Pv6cOBU4N6cn90'
    SECRET_KEY = 'IK4bMvckG5yMYEAswKRYeGGFlfQddUlV'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def simple_ocr(self, path):
        result = self.client.basicGeneral(self.get_file_content(path))
        return result

    def hello(self):
        return "hello java"
