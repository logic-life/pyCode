# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:47:48 2022
Dest:多线程下载书籍
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
contentPattern = '原站阅读。</p>(.*?)<div class'
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
    os.makedirs('斗破苍穹12',exist_ok=True)
    with open(os.path.join('斗破苍穹12',chapter+'.txt'),'w',encoding='utf-8') as f:
        f.write(article)
# %% 获取章节名称，章节url
doupoChapterName,doupobookUrl = getTitleLink(html, blockPattern, linkPattern)
book = [doupoChapterName[1:100],doupobookUrl[1:100]]
book = [[row[i] for row in book] for i in range(len(book[0]))]
# %% 循环的方式效率太低
# for i in range(len(doupobookUrl)):
#     article=getArticle(doupobookUrl[i])
#     article = article.replace('</p><p>', '\n')
#     article = article.replace('<p>', '')
#     article = article.replace('</p>', '')
#     article = article.replace('</div>', '')
#     save(doupoChapterName[i],article)
    
# %% 下载书籍
def saveTxt(book):
    article=getArticle(book[1])
    article = article.replace('</p><p>', '\n')
    article = article.replace('<p>', '')
    article = article.replace('</p>', '')
    article = article.replace('</div>', '')
    save(book[0],article)
# %% 多线程下载章节，速度快
pool = Pool(5)
pool.map(saveTxt,book)
