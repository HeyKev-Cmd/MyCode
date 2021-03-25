# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:37:42 2020

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv('108_ab107_S.csv',encoding='big5')
dt1=df[df['學校類型']!=''  ]
dt2=dt1  [[ '學位生_正式修讀學位外國生','學校名稱','學校類型']]
bins=[-1]
labels=[]
for x in range(200,max(dt2['學位生_正式修讀學位外國生'])+1 ,100  ):
      bins.append(x)
      labels.append(str(x-200)+"-"+  str(x)  )


dt2.index=pd.cut(
dt2['學位生_正式修讀學位外國生'],
    bins, 
    
)
count=pd.DataFrame( pd.Series.value_counts(dt2.index)   )

x=[i+1 for i in range(len(count))]

# #設定圖表大小
fig=plt.figure(figsize=[len(count),len(count)]) #繪製直條圖
plt.xlabel('學生數量區間')
plt.ylabel('學校數量')
plt.bar(x,count['學位生_正式修讀學位外國生']    )
plt.title("108年度台灣大學外籍生")
plt.xticks(x,labels, rotation=90, fontsize = 20,)
plt.legend(['人數'])
plt.show()


