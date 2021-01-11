#encoding=utf-8
import requests
import os,sys
import numpy as np
import json
import time
from sanic import Sanic

app = Sanic(__name__)

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

def post_processing(post_server=True,server_name=None,port=None,data=None):
    if post_server:
       pass
    else:
        #需要自己加端口
        url = 'http://localhost:{}/hello'.format(port)
    res = requests.post(url,json=data)
    if res.ok:
        return res.json()
    else:
        print('NO RESPONSE')

# Import the Sanic app, usually created with Sanic(__name__)
# from external_server import app

def test_index_returns_200():
    request, response = app.test_client.get('/')
    assert response.status == 200

def test_index_put_not_allowed():
    request, response = app.test_client.put('/')
    assert response.status == 405


# 下面这种给 Get 请求传递数据：

def test_get_request_includes_data(url):
    params = {'key1': 'value1', 'key2': 'value2'}
    request, response = app.test_client.get(url, params=params)
    # assert request.args.get('key1') == 'value1'
    print('返回k-v request={},response={}'.format(response, response.json))  # 返回text是没有json值
    print('返回text request={},response={}'.format(response, response.text))  ##返回text,dict形式，都能用text取值
    return response
# 给 POST 请求传递 JSON 数据：

def tt_post_json_request_includes_data(url):
    # data = {'key1': 'value1', 'key2': 'value2'}
    data={'word':'hello python NIhao hello test hell0'}
    request,response =app.test_client.post(url, data=json.dumps(data))
    # assert request.json.get('key1') == 'value1'

    print('request',request)
    print('返回k-v request={},response={}'.format(response,response.json))#返回text是没有json值
    print('返回text request={},response={}'.format(response, response.text))##返回text,dict形式，都能用text取值
    return response

if __name__=='__main__':
    data_json = {'client_content':'hello'}
    t1 = time.time()
    # docker 内部测试端口用8889，anjie服务器上端口是8888
    # res = post_processing(post_server=True,port=8888,data=data_json)

    # res = post_processing(post_server=False, port=8900, data=data_json)
    #http://localhost:18401/word/cloud/generate #sanic 服务地址
    #http://localhost:18402/word/cloud/generate #flask 服务地址
    res=tt_post_json_request_includes_data('http://localhost:18402/word/cloud/generate')
    # res=test_get_request_includes_data('http://localhost:18401/word/cloud/generate')

    # res = tt_post_json_request_includes_data('http://localhost:8888/hello')
    # res=test_get_request_includes_data('http://localhost:8900/hello')

    t2 = time.time()
    print('spend time:{}s'.format(t2 - t1))
    print(res)
