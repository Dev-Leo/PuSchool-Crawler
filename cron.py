# coding=gbk
#/usr/bin/python3
import os
from datetime import datetime
import time

#每隔n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        os.system("python C:/Users/Administrator/Desktop/pu.py")
        time.sleep(n)
#一天
timer(86400)
