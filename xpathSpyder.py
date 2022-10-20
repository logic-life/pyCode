# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:14:44 2022

@author: Logic-life

XPath匹配字段信息位置
"""
import lxml.html
import re
import csv
import requests as REQ
# %% 获取网页内容
url = 'https://m.xbiquge.so/'
content = REQ.get(url)
content.encoding = 'GB2312'
content = content.text;
novel = []
author = []
name = []
# %% xpath截取信息
selector = lxml.html.fromstring(content)
url = selector.xpath('//div[@class="s_list"]/a/@href')
text = selector.xpath('//div[@class="s_list"]/a/text()')
for i in text :
   i= str(i)
   author.append(re.findall('(.*?)：', i)) 
   name.append(re.findall('《(.*?)》', i)) 
# %%
for i in range(len(author)):
    novel.append([author[i][0],name[i][0],url[i]])
# %% 
infile = 'D:\code\小说信息.csv'
with open(infile,'w+',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(novel)