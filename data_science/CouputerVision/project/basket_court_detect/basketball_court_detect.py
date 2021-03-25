# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:47:01 2020

@author: kevin
"""
import cv2
import numpy as np
def process(img,threshold,lines_weight):
    # print('true')
    #銳化
    # kernel=np.array([[0,-1,0],[-1,5,1],[0,-1,0]],np.float32)
    # img_brighten=cv2.filter2D(img,-1,kernel=kernel)
    # blurred = cv2.GaussianBlur(img, (5,7), 0)
    try:
        a,test = cv2.threshold(img[:,:,2],253,0,4)
        # a,test = cv2.threshold(test,250,255,cv2.THRESH_BINARY)
        ret,img_bi_gray = cv2.threshold(img[:,:,2],threshold,255,cv2.THRESH_BINARY)
    except TypeError:
        print('error')
    # cv2.imwrite('img_bi.jpg', img_bi)
    # 二值化

    # img_test=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) 
    # ret,img_test = cv2.threshold(img_test,200,255,cv2.THRESH_BINARY)
    # img_bi_gray=cv2.cvtColor(img_bi,cv2.COLOR_RGB2GRAY)  
    # img_bi_gray=img_bi[:,:,2]
    
    # 其中我们最常用到的参数为：img = cv2.GaussianBlur(src, (blur1, blur2), 0)，其中src是要进行滤波的原图像，（blur1，blur2）是高斯核的大小，blur1和blur2的选取一般是奇数，blur1和blur2的值可以不同。参数0表示标准差取0。
    # 当blur1=blur2=1时，相当于不对原始图像做操作。blur1和blur2越大，图像的模糊程度越大。但不是blur1和blur2越大越好，blur1和blur2太大，不仅会滤除噪音，还会平滑掉图像中有用的信息。所以blur的选取要进行测试。
    # 如果要进行滤波的图像的长宽比大致为1:1，那么选取blur时，一般设置blur1=blur2。
    # 如果要进行滤波的图像的长宽比大致为m:n，那么选取blur时，blur1:blur2=m:n。
    # # n*n kernal size
    img_bi_gray = cv2.GaussianBlur(img_bi_gray, (5,7), 0)
    # kernel=np.array([[0,-1,0],[-1,5,1],[0,-1,0]],np.float32)
    # img_bi_gray=cv2.filter2D(img_bi_gray,-1,kernel=kernel)
    
    img_bi_gray=cv2.fastNlMeansDenoising(img_bi_gray)
    
    canny = cv2.Canny(img_bi_gray,150 ,150,apertureSize = 7)
    
    lines = cv2.HoughLines(canny,1,np.pi/180,lines_weight)
    # lines = cv2.HoughLinesP(canny,1,np.pi/180,1,0.1,350,65)
    
    # HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None) 
    
    # image： 必须是二值图像，推荐使用canny边缘检测的结果图像； 
    # rho: 线段以像素为单位的距离精度，double类型的，推荐用1.0 
    # theta： 线段以弧度为单位的角度精度，推荐用numpy.pi/180 
    # threshold: The minimum number of intersecting points to detect a line.
    # threshod: 累加平面的阈值参数，int类型，超过设定阈值才被检测出线段，值越大，基本上意味着检出的线段越长，检出的线段个数越少。根据情况推荐先用100试试
    # lines：这个参数的意义未知，发现不同的lines对结果没影响，但是不要忽略了它的存在 
    # minLineLength：线段以像素为单位的最小长度，根据应用场景设置 
    # maxLineGap：同一方向上两条线段判定为一条线段的最大允许间隔（断裂），超过了设定值，则把两条线段当成一条线段，值越大，允许线段上的断裂越大，越有可能检出潜在的直线段
    try:
        for x in range(len(lines)):
               for rho,theta in lines[x]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 10000*(-b))
                    y1 = int(y0 + 10000*(a))
                    if(x<=2):
                        x2 = int(x0 - 10000*(-b))
                        y2 = int(y0 - 10000*(a))
                    else:
                        x2 = int(x0 - 1000*(-b))
                        y2 = int(y0 - 1000*(a))
                        
                    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    except TypeError:
        print('no line')
    # ret,img_bi_gray= cv2.threshold(img[:,:,2],251,255,cv2.THRESH_BINARY)
    
    return img,img_bi_gray,canny
#%%
def test(img,threshold,lines_weight):
    try:
        a,img_bi_gray = cv2.threshold(img[:,:,2],230,0,4)
        # a,test = cv2.threshold(test,250,255,cv2.THRESH_BINARY)
        ret,img_bi_gray = cv2.threshold(img_bi_gray,210,255,cv2.THRESH_BINARY)
    except TypeError:
        print('error')
    
    img_bi_gray=cv2.fastNlMeansDenoising(img_bi_gray)
    img_bi_gray = cv2.GaussianBlur(img_bi_gray, (5,7), 0)
    canny = cv2.Canny(img_bi_gray,10 ,10,apertureSize = 7)
    lines=cv2.HoughLinesP(canny, 1.0, np.pi/180 , 150,10, 5,100) 
    # lines = cv2.HoughLinesP(canny,1,np.pi/180,lines_weight)
    try:
       for x1, y1, x2, y2 in lines[0]:
           cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    except TypeError:
        print('no line')
    # ret,img_bi_gray= cv2.threshold(img[:,:,2],251,255,cv2.THRESH_BINARY)
    
    return img,img_bi_gray,canny
    #%%
def show(img):
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
    # cv2.imshow('img_bi', img_bi)
    # cv2.imshow('img_test',img_test)
    # cv2.imshow('img_bi_gray',img_bi_gray)
    cv2.imshow('img_canny', canny)
    cv2.imshow('img', img)
    # cv2.imshow('canny', canny)
    
    #秀出圖片
    # cv2.imwrite( "result.jpg", img )           #保存圖片
    cv2.waitKey(0)                             #等待按下任一按鍵
    cv2.destroyAllWindows()   
    cv2.imwrite('img_bi_gray.jpg', img_bi_gray)
    cv2.imwrite('basketcourt_detect-hough.jpg',img)   
    cv2.imwrite('canny.jpg',canny)  
    #%%
if __name__ == '__main__':
    import cv2
    import numpy as np
    # https://www.youtube.com/watch?v=zqD_NTysZ6o&t=17s&ab_channel=LakeShowHighlights
    import cv2
    import numpy as np
    url='./basketballcourt1.png'
    img=cv2.imread(url)
    
    (img,img_bi_gray,canny)=test(img,220,200)
    # (img,img_bi_gray,canny)=process(img,245,200)
    # (img,img_bi_gray,canny)=process(img,251,200)
    show(img)
