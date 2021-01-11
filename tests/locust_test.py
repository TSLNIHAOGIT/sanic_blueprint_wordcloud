# from locust import HttpLocust
from locust import HttpUser,TaskSet,task
import subprocess
import json


import time
from locust import HttpUser, task




import locust.stats
#加入文件更新的频率 存储的csv文件
locust.stats.CSV_STATS_INTERVAL_SEC = 5 # 默认是2秒


# class QuickstartUser(HttpUser):
#     @task
#     def hello_world(self):
#         self.client.get("/hello")
#         self.client.get("/world")
#
#     @task(3)
#     def view_item(self):
#         for item_id in range(10):
#             self.client.get(f"/item?id={item_id}", name="/item")
#             time.sleep(1)
#
#     def on_start(self):
#         self.client.post("/login", json={"username":"foo", "password":"bar"})



#This is the TaskSet class.
class UserBehavior(TaskSet):
    #Execute before any task.
    # def on_start(self):
    #     pass

    # #the @task takes an optional weight argument.
    # @task(1)
    # def list_header(self):
    #     r = self.client.get("/homepage/list_header.html")
    #     if json.loads((r.content))["result"] != 100:
    #         r.failure("Got wrong response:"+r.content)
    #
    # @task(2)
    # def list_goods(self):
    #     r = self.client.get("/homepage/list_goods.html")
    #     if json.loads((r.content))["result"] != 100:
    #         r.failure("Got wrong response:"+r.content)

    @task
    def post_example(self):
        url='http://localhost:18401/word/cloud/generate' #sanic
        # url = 'http://localhost:18402/word/cloud/generate' #flask
        data = {'word': 'hello python NIhao hello test hell0'}
        r = self.client.post(url,json=data)
        # print(r.content)
        # if json.loads((r.content))["result"] != 100:
        #     r.failure("Got wrong response:" + r.content)

#This is one HttpLocust class.
class WebUserLocust(HttpUser):
    #Speicify the weight of the locust.
    weight = 1
    #The taskset class name is the value of the task_set.
    # task_set = UserBehavior
    tasks = [UserBehavior]
    #Wait time between the execution of tasks.
    min_wait = 5000
    max_wait = 15000

#This is another HttpLocust class.
class MobileUserLocust(HttpUser):
    weight = 3
    tasks = [UserBehavior]
    min_wait = 3000
    max_wait = 6000

#if __name__ == '__main__':
#    subprocess.Popen('locust -f .\locust_test_1.py --host=http://api.g.caipiao.163.com', shell=True)