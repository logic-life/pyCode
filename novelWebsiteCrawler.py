# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:47:48 2022

@author: Logic-life
"""
import requests as REQ
import re
import os
from multiprocessing.dummy import Pool
# %% URL及对应的正则
startUrl = 'https://www.doupobook.cc'
blockPattern = '<div id="play_0">(.*)</a></li>'
linkPattern = 'href="(.*?)" title='
chapterNamePattern = 'title="(.*?)">'
contentPattern = '<p>(.*?)</p>'
# %%获取html页面
info = REQ.get('https://www.doupobook.cc/doupo/')
info.encoding = "utf-8"
html = info.text
toUrlList = []
toChapterNameList = []
# %% 获取章节页面URL


def getTitleLink(html, pattern_1, pattern_2):
   
    textBlock = re.findall(blockPattern, html, re.S)[0]
    titleLink = re.findall(linkPattern, textBlock, re.S)
    chapterName = re.findall(chapterNamePattern, textBlock, re.S)
    for url in titleLink:
        toUrlList.append(startUrl+url)
    for Name in chapterName:
        toChapterNameList.append(Name)
    return toChapterNameList,toUrlList


# %% 
def getArticle(htmlUrl):
    textInfo = REQ.get(htmlUrl)
    textInfo.encoding = "utf-8"
    textInfo = textInfo.text
    text = re.search(contentPattern, textInfo, re.S).group(1)
    return text
# %% 
def save(chapter,article):
    os.makedirs('斗破苍穹',exist_ok=True)
    with open(os.path.join('斗破苍穹',chapter+'.txt'),'w',encoding='utf-8') as f:
        f.write(article)
# %%
# def opeator(pool):
    # art = getArticle()
    # save(chapter, article)
# %% 获取章节名称，章节url
# doupoChapterName,doupobookUrl = getTitleLink(html, blockPattern, linkPattern)
# pool = Pool(5)

# pool.map(getArticle,doupobookUrl)

