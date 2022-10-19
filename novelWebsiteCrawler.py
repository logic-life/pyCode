# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:47:48 2022

@author: Logic-life
"""
import requests as REQ
import re

# %% URL及对应的正则
startUrl = 'https://www.doupobook.cc'
blockPattern = '<div id="play_0>(.*)</div>"'
linkPattern = '<li class="line3"><a href="(.*)" title=.*?'
# %%获取html页面
html = REQ.get('https://www.doupobook.cc/doupo/').content.decode()
# %% 获取章节页面URL
def getTitleLink(html,pattern_1,pattern_2):
    toUrlList = []
    textBlock = re.findall(blockPattern,html,re.S)
    titleLink = re.findall(linkPattern,textBlock,re.S)
    for url in titleLink:
        toUrlList.append(startUrl+url)
    return toUrlList
# %% 
doupobookUrl = getTitleLink(html, blockPattern, linkPattern)      
    
    