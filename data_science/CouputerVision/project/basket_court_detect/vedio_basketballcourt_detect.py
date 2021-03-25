# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:11:23 2020

@author: kevin
"""


import dlib
import cv2
import imutils
from basketball_court_detect import process
import numpy as np
if __name__ == '__main__':
    # https://www.youtube.com/watch?v=zqD_NTysZ6o&t=17s&ab_channel=LakeShowHighlights
    
    # 開啟影片檔案
    rote='target_trim_short.mp4'
    cap = cv2.VideoCapture(rote)
    
    # 取得畫面尺寸
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 使用 XVID 編碼
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Xvid是一个开放源代码的MPEG-4视频编解码器，它是基于OpenDivX而编写的
    
    # 建立 VideoWriter 物件，輸出影片至 output.avi，FPS ->偵 值為 20.0
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

    #%%
    # 以迴圈從影片檔案讀取影格，並顯示出來
    while(cap.isOpened()):
      ret, frame = cap.read()
      # 偵測人臉
      if(ret'True'):
          (img,img_bi_gray,canny)=process(frame)
          out.write(img)
        
          # 顯示結果
          cv2.imshow("test", img)
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
      else:
         # 顯示結果
         print('no frame')
        
    cap.release()
    out.release()
    # cv2.destroyAllWindows()
    
