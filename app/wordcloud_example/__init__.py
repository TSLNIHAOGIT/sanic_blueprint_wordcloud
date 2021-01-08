# from flask import Blueprint
from sanic import Blueprint

import os,sys
wordcloud = Blueprint('wordcloud_example')##不能加__name__参数，不然访问不了post方法

#将项目根目录加入到运行环境
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app.wordcloud_example import views





