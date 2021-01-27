## 深度學習過程中，需要製作訓練集和驗證集，測試集
## 將filePath檔案下的圖片儲存在newFilePath資料夾下的相應子資料夾中
## pic是字典，存放每個圖片要移到的子資料夾名

import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)    # 取圖片的原始路徑
        filenumber=len(pathDir)
        rate=0.1    # 抽取圖片比例
        picknumber=int(filenumber*rate) # 按照rate比例從文件夾中取一定數量圖片
        sample = random.sample(pathDir, picknumber)  # 隨機選取picknumber數量的樣本圖片
        print (sample)
        for name in sample:
                shutil.move(fileDir+name, tarDir+name)
        return

if __name__ == '__main__':
	fileDir = "D:/Dataset/defect_detection/choose_2/train/5/"    # 原圖片文件夾路徑
	tarDir = r'D:\\Dataset\\defect_detection\\choose_2\\val\\5\\'    # 移動到新的文件夾路徑
	moveFile(fileDir)