# 改檔名從一開始編號
import os

path = r'C:\Users\Allen\Desktop\1'

def batch_rename(path):
    count = 1
    for fname in os.listdir(path):
        print(os.path.join(path, fname))
        new_fname = str(count)+'.jpg'
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        print(os.path.join(path, new_fname))
        count = count + 1

batch_rename(path)
