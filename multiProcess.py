# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:26:06 2022
Dest: 多线程爬虫
@author: Logic-life
"""
from multiprocessing.dummy import Pool
import requests
import time
# %% 多进程计算
def calcPower2(num):
    return num * num

pool = Pool(3)

originNums = [x for x in range(10)]
result = pool.map(calcPower2,originNums)
print(f'计算0-9的平方是:{result}')

# %% 访问网页
def query(url):
    requests.get(url)
# %% 单线程访问网页
start = time.time();
for i in range(100):
    query('https://www.baidu.com')
end  = time.time()
print(f'单线程循环100次百度首页耗时:{end-start}')
# %% 多线程访问网页
urlList = []
start = time.time();
for i in range(100):
    urlList.append('https://www.baidu.com')
pool = Pool(5)
pool.map(query,urlList)
end  = time.time()
print(f'单线程循环100次百度首页耗时:{end-start}')
