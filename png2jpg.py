# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:40:08 2020

@author: Allen
"""

import os
import sys
from PIL import Image

input_folder=r'C:/Users/Allen/Desktop/choose/3/1'   #輸入資料夾，包含.png格式圖片
output_folder=r'C:/Users/Allen/Desktop/choose/3/1'  #输出資料夾
#training_data=[]    
a=[]
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files if x.endswith('.png')):
        filepath = os.path.join(root, filename) 
        
        object_class = filename.split('.')[0]
        a.append(object_class)
    print(a)
    
for i in a:
    old_path=input_folder+"\\"+str(i)+'.png'
    new_path=output_folder+"\\"+str(i)+'.jpg'
    img=Image.open(old_path)
    img = img.convert("RGB")
    img.save(new_path)