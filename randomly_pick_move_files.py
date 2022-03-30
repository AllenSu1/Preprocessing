## 深度學習過程中，需要製作訓練集和驗證集，測試集
## 將filePath檔案下的圖片儲存在newFilePath資料夾下的相應子資料夾中
## pic是字典，存放每個圖片要移到的子資料夾名

import os, random, shutil


def moveFile(fileDir):

    rate_true = True  # 是否按比例或個數挑選檔案 (True 按比例挑選 False 按個數挑選)
    rate = 0.1  # 抽取圖片比例
    picknumber = 16000  # 挑選圖片張數

    pathDir = os.listdir(fileDir)  # 取圖片的原始路徑
    filenumber = len(pathDir)

    if rate_true:
        picknumber = int(filenumber * rate)  # 按照rate比例從文件夾中取一定數量圖片
    else:
        picknumber = picknumber

    sample = random.sample(pathDir, picknumber)  # 隨機選取picknumber數量的樣本圖片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + name)
    return


if __name__ == '__main__':
    fileDir = "D:/Dataset/Train/VOC2007/JPEGImages/"  # 原圖片文件夾路徑
    tarDir = 'D:/Dataset/Test/VOC2007/JPEGImages/'  # 移動到新的文件夾路徑
    moveFile(fileDir)
