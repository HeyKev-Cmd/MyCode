import urllib.request
import cv2
import os
 
# 創建圖片保存目錄
if not os.path.exists('basketball_img'):
    os.makedirs('basketball_img')
 
neg_img_url = ['http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02802721']
 
urls = ''
for img_url in neg_img_url:
    urls += urllib.request.urlopen(img_url).read().decode()
 
img_index = 1
for url in urls.split('\n'):
    try:
        print(url)   
        urllib.request.urlretrieve(url, 'basketball_img/'+str(img_index)+'.jpg')
        # 把圖片轉為灰度圖片
        gray_img = cv2.imread('basketball_img/'+str(img_index)+'.jpg', cv2.IMREAD_GRAYSCALE)
        # 更改圖像大小
        image = cv2.resize(gray_img, (150, 150))
        # 保存圖片
        cv2.imwrite('basketball_img/'+str(img_index)+'.jpg', image)
        img_index += 1
    except Exception as e:
        print(e)
 
# 判斷兩張圖片是否完全一樣
def is_same_image(img_file1, img_file2):
    img1 = cv2.imread(img_file1)
    img2 = cv2.imread(img_file2)
    if img1.shape == img2.shape and not (np.bitwise_xor(img1, img2).any()):
        return True
    else:
        return False
 
# 去除重複圖片
"""
file_list = os.listdir('neg')
try:
    for img1 in file_list:
        for img2 in file_list:
            if img1 != img2:
                if is_same_image('neg/'+img1, 'neg/'+img2) is True:
                    print(img1, img2)
                    os.remove('neg/'+img1)
        file_list.remove(img1)
except Exception as e:
    print(e)
"""

import os
import numpy as np
 
with open('basketball_img.txt', 'w') as f:
    url='basketball_img'
    for img in os.listdir(url):
        line = url+'/'+img+'\n'
        f.write(line)