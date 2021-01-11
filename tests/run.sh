locust -f locust_test.py --headless -u 1000  -r 1000  -t 30s  --stop-timeout 99 --host localhost  --csv=locusts_report

#-u 用户数
#-r 每秒产生的用户数量
#-t 运行时间
#--host 测试的主机