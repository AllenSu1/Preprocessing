# by Blacky (realy)

import os
from cv2 import cv2

img_path = r'D:\Dataset\defect_detection\train\0'
out_path = r'D:\Dataset\defect_detection\thisone\0'

for item in os.listdir(img_path):
    # 提取路徑名稱
    fname = os.path.splitext(item)
    os.path.split(fname[0])
    file_name = fname[0]
    path_com = os.path.join(img_path, item)

    img=cv2.imread(path_com)
    
    for i in range(-1, 2):
        horizontal_img=cv2.flip(img,i)
        newName = os.path.join(out_path, file_name)
        newNameTotal = newName + '_flip_type' + str(i) + '.jpg'
        print(newNameTotal)
        cv2.imwrite(newNameTotal, horizontal_img)
    