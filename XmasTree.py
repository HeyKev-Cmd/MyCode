# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:48:31 2020

@author: OSA
"""
height=15
batch=4

for x in range(1,height+1):
      print(" " * int(height-x),end="" )
      if(x%2==1 and x!=1):
          print("O" *    int(2*x-1 )   )
      elif(x==1):
          print("*")
      else:
          print("X" *    int(2*x-1 )   )
for y in range(1,batch+1):
      print(" "*(height-2),"X")
   

