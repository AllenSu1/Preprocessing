#固定size的圖片每x度旋轉一次
import os
from cv2 import cv2
from PIL import Image
import numpy as np
import argparse

#每幾度轉一次
angle = 45

# 定義旋轉rotate函數
def rotate(image, angle, center=None, scale=1.0):
    # 獲取圖像尺寸
    (h, w) = image.shape[:2]
 
    # 若未指定旋轉中心，則將圖像中心設為旋轉中心
    if center is None:
        center = (w / 2, h / 2)
 
    # 執行旋轉
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # 返迴旋轉後的圖像
    return rotated

img_path = r'D:\Dataset\defect_detection\thisone\5'  # 輸入路徑 
out_path = r'D:\Dataset\defect_detection\thisone\5'

for item in os.listdir(img_path):
    # 提取路徑名稱
    fname = os.path.splitext(item)
    os.path.split(fname[0])
    file_name = fname[0]
    path_com = os.path.join(img_path, item)

    img=cv2.imread(path_com)
        
    for i in range(0,8):
        img_rotate = rotate(img , i * angle)  # N°旋轉一次
        newname = os.path.join(out_path, file_name + '_rotate' + str("_") + str((i)*15) + '.jpg')
        print(newname)
        cv2.imwrite(newname , img_rotate)