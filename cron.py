# coding=gbk
#/usr/bin/python3
import os
from datetime import datetime
import time

#ÿ��n��ִ��һ��
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        os.system("python C:/Users/Administrator/Desktop/pu.py")
        time.sleep(n)
#һ��
timer(86400)
