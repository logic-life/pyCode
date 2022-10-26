'''
Description: Python进度条
Version: 0.0-0
Author: logic-life
Date: 2022-10-25 13:48:06
LastEditors: logic-life
LastEditTime: 2022-10-25 14:12:11
'''

# %%

from time import sleep
from tqdm import tqdm

# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
for i in tqdm(range(1, 100)):
   # 模拟你的任务
   sleep(0.01)
sleep(0.5)
# %%
import time
from tqdm import tqdm

# 发呆0.5s
def action():
    time.sleep(0.5)
with tqdm(total=100000, desc='Example', leave=True, ncols=100, unit='img', unit_scale=False) as pbar:
    for i in range(10):
        # 发呆0.5秒
        action()
        # 更新发呆进度
        pbar.update(10000)

# %%
