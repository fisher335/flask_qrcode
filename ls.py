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
    if len(image) == 0:
        print("Error: could not load image")
        os._exit(0)
    print(image.shape)
    scale = 1.0
    width, height = image.shape[:2]
    new_img = cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_CUBIC)  # 缩小图像
    options = {}
    options['type'] = 'normal'
    new_file = 'result%d' % random.randint(1, 1000) + '.jpg'
    cv2.imwrite(new_file, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
    result = client.vatInvoice(open(new_file, 'rb').read(), options=options)
    ticket = result['words_result']
    print(ticket)
    print('合计金额', ticket['TotalAmount'])
    print('合计税额', ticket['TotalTax'])
    print('平均税率', format(float(ticket['TotalTax']) / float(ticket['TotalAmount']) * 100, '0.2f') + '%')
    print('价税合计', ticket['AmountInWords'])
    print('价税合计', ticket['AmountInFiguers'])
    print()
    print('销售方名称', ticket['SellerName'])
    print('销售方纳税人识别号', ticket['SellerRegisterNum'])
    print('销售方地址及电话', ticket['SellerAddress'])
    print('销售方开户行及账号', ticket['SellerBank'])
    print()
    print('购方名称', ticket['PurchaserName'])
    print('购方纳税人识别号', ticket['PurchaserRegisterNum'])
    print('购方地址及电话', ticket['PurchaserAddress'])
    print('购方开户行及账号', ticket['PurchaserBank'])
    print()
    print('收款人', ticket['Payee'])
    print('复核', ticket['Checker'])
    print('开票人', ticket['NoteDrawer'])
    print('开票日期', ticket['InvoiceDate'])
    os.remove(new_file)
