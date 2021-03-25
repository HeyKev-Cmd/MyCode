# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:23:45 2020

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt
#讀取資料集
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
dt=pd.read_csv('output.csv',encoding = 'ANSI')
#篩選資料107年度
city=dt[dt['site_id']=='新北市板橋區'][['female_age','marry_pair']]
#年齡
age=city.groupby('female_age').sum()
print(age)
x=[i+1 for i in range(len(age))]
#設定圖表大小
fig=plt.figure(figsize=[len(age),7]) #寬為10吋，高為6吋
#繪製直條圖
plt.xlabel('女方歲數')
plt.ylabel('人數')
plt.bar(x,age['marry_pair'] )
plt.title("板橋區各年齡結歡數")

#更改x軸的刻度名稱
plt.xticks(x,age.index, rotation=90)
plt.legend(['數量'])
plt.show()