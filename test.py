# import cv2

# def sharpen(img, sigma=100):
#     # sigma = 5、15、25
#     blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
#     usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)

#     return usm

# img0 = cv2.imread(
#     r'D:\Dataset\Allen_thesis\vannamei\vannamei_v1\image\vannamei16677.jpg')
# # img0 = cv2.resize(img0, (432, 768), interpolation=cv2.INTER_LINEAR)   #resize
# img = sharpen(img0)

# cv2.imshow("img0", img0)
# cv2.imshow("img", img)

# cv2.waitKey()

# 算像素質方圖
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

fileDir = r"D:\Dataset\Allen_thesis\vanamei_demo"
pathDir = os.listdir(fileDir)

# 畫出 RGB 三種顏色的分佈圖
b_list, g_list, r_list = [], [], []
for img_path in pathDir:

    filePath = os.path.join(fileDir, img_path)
    img = cv2.imread(filePath)

    b_histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    g_histr = cv2.calcHist([img], [1], None, [256], [0, 256])
    r_histr = cv2.calcHist([img], [2], None, [256], [0, 256])

    b_list.append(b_histr)
    g_list.append(g_histr)
    r_list.append(r_histr)

channel_b = np.array(b_list).mean(axis=0)
channel_g = np.array(g_list).mean(axis=0)
channel_r = np.array(r_list).mean(axis=0)

plt.plot(channel_b, color='b')
plt.plot(channel_g, color='g')
plt.plot(channel_r, color='r')
plt.xlim([0, 256])
plt.show()