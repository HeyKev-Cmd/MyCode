# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:17:02 2020

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt
#讀取資料集
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
#設定中文
df=pd.read_csv('height.csv')
#篩選資料107年度
df1=df[df['學年度']==107][['年齡','總計','男','女']]
#年齡
df2=df1.groupby('年齡').sum()
print(df2)
x=[i+1 for i in range(len(df2))]
#設定圖表大小
fig=plt.figure(figsize=[7,7]) #寬為10吋，高為6吋
#繪製直條圖
plt.set_xlabel='age'
plt.xlabel('年齡')
plt.ylabel('身高')
plt.bar(x,df2['總計'] )
plt.title("107年度學生身高平均值(6歲-15歲)")

#更改x軸的刻度名稱
plt.xticks(x,df2.index, rotation=40)
plt.legend(['height'])
plt.show()
