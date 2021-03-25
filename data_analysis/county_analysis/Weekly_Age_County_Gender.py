# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:58:04 2020

@author: kevin
"""
import pandas as pd
import matplotlib.pyplot as plt
#讀取資料集
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
dt=pd.read_csv('Weekly_Age_County_Gender_061.csv',encoding = 'ANSI')
#篩選資料107年度
city=dt[dt['縣市']=='高雄市'][['鄉鎮','確定病例數']]
#年齡
district=city.groupby('鄉鎮').sum()
print(district)
x=[i+1 for i in range(len(district))]
#設定圖表大小
fig=plt.figure(figsize=[len(district),7]) #寬為10吋，高為6吋
#繪製直條圖
plt.xlabel('鄉鎮')
plt.ylabel('人數')
plt.bar(x,district['確定病例數'] )
plt.title("2013-2020高雄各區登革熱數")

#更改x軸的刻度名稱
plt.xticks(x,district.index, rotation=90)
plt.legend(['數量'])
plt.show()