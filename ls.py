# coding:utf-8
import os
import random

from aip import AipOcr
import cv2

if __name__ == '__main__':
    """ 你的 APPID AK SK """
    APP_ID = '16667601'
    API_KEY = 'T3xjr0oIM7Pv6cOBU4N6cn90'
    SECRET_KEY = 'IK4bMvckG5yMYEAswKRYeGGFlfQddUlV'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = cv2.imread(r'C:\Users\Administrator\Desktop\1.png')
    if len(image)==0:
        print("Error: could not load image")
        os._exit(0)
    print(image.shape)
    scale = 1.0
    width,height = image.shape[:2]
    new_img = cv2.resize(image, (int(width*scale), int(height*scale)), interpolation=cv2.INTER_CUBIC)#缩小图像
    options = {}
    options['type'] = 'normal'
    new_file = 'result%d' % random.randint(1,1000) + '.jpg'
    cv2.imwrite(new_file, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
    result =  client.vatInvoice(open(new_file, 'rb').read(), options=options)
    words_result = result['words_result']
    print(words_result)
    print('发票号码:', words_result['InvoiceNum'])
    print('开票日期:', words_result['InvoiceDate'])
    print('合计金额:', words_result['TotalAmount'])
    print('合计税额:', words_result['TotalTax'])
    print('销售方名称:', words_result['SellerName'])
    print('销售方纳税人识别号:', words_result['SellerRegisterNum'])
    print('购方名称:', words_result['PurchaserName'])
    print('购方纳税人识别号:', words_result['PurchaserRegisterNum'])
    os.remove(new_file)
