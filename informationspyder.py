# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 23:16:06 2022

@author: logic-life
"""

import requests
import re
import csv
inurl = "https://y.qianzhan.com/yuanqu/diqu/3401/?pg="
cityNames = []
gardenNames = []
for i in range(1, 44):
    outurl = inurl + str(i)
    info = requests.get(url=outurl)
    info.encoding = "utf-8"
    html = info.text
    trPattern = ' <td class="rope">.*?class="blue (.*?)<td class="rope">'
    gardenPattern = 'text-el">(.*?) </a>'
    cityPattern = '<td>.*?市 </td>.*?<td>(.*?) </td>'
    trData = re.findall(trPattern,html,re.S)
    for data in trData:
        gardenData = re.findall(gardenPattern, data)[0].strip()
        cityData = re.findall(cityPattern, data,re.S)[0].strip()
        gardenNames.append(gardenData)
        cityNames.append(cityData)

# %% 矩阵转置
output = [gardenNames,cityNames]
output = [[row[i] for row in output] for i in range(len(output[0]))]
# %% 写入csv文件
infile = 'D:\python\data.csv'
with open(infile,'w+',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output)
    

