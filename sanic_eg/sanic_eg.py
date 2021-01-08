import asyncio
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from sanic import Sanic
from sanic.response import text
from sanic.log import logger
app = Sanic(__name__)


from sanic.response import json

@app.route("/hello",methods=["POST","GET"])
async def post_json(request):
  ##request和response解析数据的形式基本上是一样的
  logger.info('post request from client={}'.format(request.json))
  # logger.info('get request from client={}'.format(request.text))
  res=json({ "received": True, "message": 'Hello' ,'request':request.json})
  # logger.info('res={}'.format(res))
  logger.info('返回结果')
  return res
  # return  text('Hello world!')

@app.route("/")
async def test(request_content):
    logger.info('request={},{}'.format(request_content,request_content.json))
    # return text('Hello world!')
    return  json({"hello": "world"})
if __name__=='__main__':
    logger.info('开始运行')
    app.update_config('my_config.py')
    print('config',app.config['A'])
    app.run(host="0.0.0.0", port=8900, debug=True)