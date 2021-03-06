import os
from cv2 import cv2
import torchvision

img_path = r'C:\Users\Allen\Desktop\1'
out_path = r'C:\Users\Allen\Desktop\2'

Alpha = 0.5    #乘數因子
Beta =100   #偏移量

for item in os.listdir(img_path):
    # 提取路徑名稱
    fname = os.path.splitext(item)
    os.path.split(fname[0])
    file_name = fname[0]
    path_com = os.path.join(img_path, item)

    img=cv2.imread(path_com)
    
    for i in range(0, 3):
        bright=i*5
        horizontal_img = cv2.convertScaleAbs(img, alpha = Alpha, beta = Beta)
        newName = os.path.join(out_path, file_name)
        newNameTotal = newName + '_bright_type' + str(i) + '.jpg'
        print(newNameTotal)
        cv2.imwrite(newNameTotal, horizontal_img)
    