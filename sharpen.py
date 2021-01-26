# 圖像銳利化
import os
from cv2 import cv2
import torchvision
# input_path
img_path = r'C:\Users\Allen\Desktop\1'
# output_path
out_path = r'C:\Users\Allen\Desktop\1'

def sharpen(img, sigma):    
    # sigma = 5、15、25
    blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
    usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
    return usm

for item in os.listdir(img_path):
    # 提取路徑名稱
    fname = os.path.splitext(item)
    os.path.split(fname[0])
    file_name = fname[0]
    path_com = os.path.join(img_path, item)

    img=cv2.imread(path_com)
    
    for j in range(1,2):
        sigma=50
        sharp_1 = sharpen(img, sigma)
        newName = os.path.join(out_path, file_name)
        newNameTotal = newName + '_sharpen_type' + '_1.jpg'
        print(newNameTotal)
        cv2.imwrite(newNameTotal, sharp_1)

        for i in range(1 , 2):
            # horizontal_img=cv2.flip(img,i)
            sigma=(50*i)
            sharp_2 = sharpen(sharp_1, sigma)
            newName = os.path.join(out_path, file_name)
            newNameTotal = newName + '_sharpen_type' + '_2.jpg'
            print(newNameTotal)
            cv2.imwrite(newNameTotal, sharp_2)
    