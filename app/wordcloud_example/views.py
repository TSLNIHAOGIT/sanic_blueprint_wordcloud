#encoding=utf8
import sys,os
import numpy as np
import pandas as pd
from scipy import sparse
#将项目根目录加入到运行环境
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'../..')))
from app.wordcloud_example import wordcloud #导入该文件夹下inti模块中的wordcloud
from code.wordcloud_example.get_wordcloud import  get_word_cloud
from app_logging import logger_path as logger
import time
# from flask import  request, jsonify
from sanic.response import json as jsonify

import pandas as pd
import math
import traceback
from datetime import  datetime
import json




#服务端获取客户端发来的json数据
@wordcloud.route('/word/cloud/generate', methods=['GET', 'POST'])
# async def get_wordcloud(request):
async def get_wordcloud(request):
    try:
        logger.info('开始进入模型，服务端获取数据')
        now_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        t1 = time.time()
        print('request',request)
        # content = request.get_json(silent=True, force=True)
        content=request.json
        print('content',content)
        text=content['word']
        # text='"life is short,you need python"'
        res = await get_word_cloud(text)##await后面需要接协程对象，即定义成异步函数即可

        # content=content['data']
        logger.info('from client type content:{}'.format(type(content)))  # Do your processing

        logger.info('筛选出需要的字段')


        logger.info('开始调用模型')

        logger.info('模型已经计算完毕，返回结果，耗时{}s'.format(time.time()-t1))
        return jsonify(res)

    except Exception as e:
        logger.error('出错：{}\n{}'.format(e, traceback.format_exc()))

        return jsonify({'data': None, 'code': "1", 'message': "{}".format(e)})
    # finally:
    #   res_json_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../../log'))
    #
    #   with open(os.path.join(res_json_path,'{}_res_path.json'.format(now_time)),'w',encoding='utf8') as f:
    #     data={
    #
    #         "calculateParam": content,
    #         "calculateResult": {'data':res}
    #     }
    #     json.dump(data,f,indent=4,ensure_ascii=False)
