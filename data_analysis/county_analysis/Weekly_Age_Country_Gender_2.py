# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:49:44 2020

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt
#讀取資料集
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
dt=pd.read_csv('Weekly_Age_County_Gender_061.csv',encoding = 'ANSI')
#篩選資料107年度
#df1=df[df.年==2019]
#資料整理
df1=dt[dt['確定病名']=='登革熱']
df2=df1[['縣市','確定病例數','性別']]
#樞紐分析
df3=df2.pivot_table(index="縣市", columns="性別",values="確定病例數",
aggfunc="sum")
print(df3)