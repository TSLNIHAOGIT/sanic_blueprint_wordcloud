from sanic.response import json
from sanic import Blueprint
from sanic.log import logger
bp = Blueprint('my_blueprint')

@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})

@bp.route("/hello",methods=["POST","GET"])
async def post_json(request):
  ##request和response解析数据的形式基本上是一样的
  logger.info('post request from client={}'.format(request.json))
  # logger.info('get request from client={}'.format(request.text))
  res=json({ "received": True, "message": 'Hello' ,'request':request.json})
  # logger.info('res={}'.format(res))
  logger.info('返回结果')
  return res