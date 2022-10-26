'''
Description: 多线程爬虫
Version: 0.0-0
Author: logic-life
Date: 2022-10-19 21:02:16
LastEditors: logic-life
LastEditTime: 2022-10-25 14:54:20
'''
# %% 多进程计算
from multiprocessing.dummy import Pool
import requests
import time
def calcPower2(num):
    return num * num

# 多进程创建
pool = Pool(3)

originNums = [x for x in range(10)]
result = pool.map(calcPower2, originNums)
print(f'计算0-9的平方是:{result}')

# %% 访问网页


def query(url):
    requests.get(url)


# %% 单进程访问网页
start = time.time()
for i in range(100):
    query('https://www.baidu.com')
end = time.time()
print(f'单进程循环100次百度首页耗时:{end-start}')
# %% 多进程访问网页
urlList = []
start = time.time()
for i in range(100):
    urlList.append('https://www.baidu.com')
pool = Pool(5)
pool.map(query, urlList)
end = time.time()
print(f'多进程循环100次百度首页耗时:{end-start}')
