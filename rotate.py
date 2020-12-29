#固定size的圖片每x度旋轉一次
import os
from cv2 import cv2
from PIL import Image
import numpy as np
import argparse

# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
 
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
 
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # 返回旋转后的图像
    return rotated

# input_path
img_path = r'D:\GitHub\t109318121\ML_Classification\resize\test'  # 輸入路徑 
# output_path
out_path = r'D:\GitHub\t109318121\ML_Classification\rotate\test'

for item in os.listdir(img_path):
    # 提取路徑名稱
    fname = os.path.splitext(item)
    os.path.split(fname[0])
    file_name = fname[0]
    path_com = os.path.join(img_path, item)

    img=cv2.imread(path_com)
        
    for i in range(-3,4):
        img_rotate = rotate(img , i * 15)  # 15°旋轉一次
        # cv2.imshow('0',img_rotate)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        newname = os.path.join(out_path, file_name + '_rotate' + str("_") + str((i)*15) + '.jpg')
        print(newname)
        cv2.imwrite(newname , img_rotate)