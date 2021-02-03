#資料擴增=>擴增各類別資料集
import os
from cv2 import cv2

# 輸入分類資料夾路徑
img_path = r'C:\Users\Allen\Desktop\project1'
# 輸出分類資料夾路徑
out_path = r'C:\Users\Allen\Desktop\ttt'
classes = os.listdir(img_path)

method='_flip_type'

num=0
for i in classes:
    # print('{}={}'.format((num),(i)))
    new_img_path = os.path.join(img_path, i) #輸入的類別資料夾路徑
    new_out_path = os.path.join(out_path, i) #輸出的類別資料夾路徑
    print(new_img_path)

    # 如果儲存資料集的資料夾不存在, 才建立資料夾
    if not os.path.isdir(new_out_path):
        os.mkdir(new_out_path)

    for item in os.listdir(new_img_path):   #取類別資料夾下所有檔案
        # 提取路徑名稱
        fname = os.path.splitext(item)  #splitext=>切檔名、副檔名
        os.path.split(fname[0])
        file_name = fname[0]
        path_com = os.path.join(new_img_path, item)

        img=cv2.imread(path_com)    # 讀取圖檔
        
        ##############資料擴增方法#################
        for i in range(-1, 2):
            aug_img=cv2.flip(img,i)
        ##########################################    

            #處理輸出檔名
            newName = os.path.join(new_out_path, file_name)
            newNameTotal = newName + method + str(i) + '.jpg'
            print(newNameTotal)
            cv2.imwrite(newNameTotal, aug_img)

    num+=1


    