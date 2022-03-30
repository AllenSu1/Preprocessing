# 更改資料夾下檔案名稱
import os

path = r'D:\dataset'  # 更名
filename = ''  # 檔案名稱
file_extension = '.jpg'  # 儲存


# 從1開始編號
def batch_rename(path):
    count = 1
    for fname in os.listdir(path):
        # print(os.path.join(path, fname))
        new_fname = filename + str(count) + file_extension
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        print(os.path.join(path, new_fname))
        count = count + 1


batch_rename(path)