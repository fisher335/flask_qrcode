import  os
from flask import Flask

app = Flask(__name__)

from router import *



if __name__ == '__main__':
    app.run(debug=True)

