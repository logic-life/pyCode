# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:35:25 2022

@author: Logic-life
"""
import csv
# %%
name = ["name1","name2","name3"];
sex = ["male","female","female"];
content = [name,sex]
# 矩阵转置
content = [[row[i] for row in content] for i in range(len(content[0]))]
print(content)
# %%
infile = "text.csv"
with open(infile,'w+') as f:
    writer = csv.writer(f )
    writer.writerows(content)
    