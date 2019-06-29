# -*- coding:utf-8 -*-   Date   : '2015/7/31 * 15:50'
from app import app

# app.run(host='0.0.0.0')


if __name__ == '__main__':
    print(app.config.get('HOST'))
    app.run(debug=True)
