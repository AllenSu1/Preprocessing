import pandas as pd
import numpy as np
import os
import shutil  #用於移動文件
from tqdm import tqdm

#打開表格文件並讀取
df = pd.read_csv(r"D:\Dataset\defect_detection\8.csv")  #csv文件
img_path = r'D:\Dataset\defect_detection\111train'  #當前資料夾
tar_path = r'D:\Dataset\defect_detection\train'     #目標資料夾

for i in range(0,6):
    newpath = os.path.join(tar_path , str(i))
    os.makedirs(newpath)

for row in tqdm(df.iterrows()):
    now = os.path.join(img_path , str(row[1][0]))
    after = os.path.join(tar_path , str(row[1][1]) , str(row[1][0]))
    shutil.copy(now,after)