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
        words = ""
        if result.get('log_id', '') != "":
            for i in result.get('words_result'):
                words += i['words'] + '''<br>'''
        else:
            words = str(result)
        return words

    def hello(self):
        return "hello java"

    def fapiao(self):
        options = {}
        options['type'] = 'roll'
        result = self.client.vatInvoice(open(r'C:\Users\Administrator\Desktop\1.png', 'rb').read(), options=options)
        print(result)


if __name__ == '__main__':
    oc = OcrClient()
    oc.fapiao()
