# 複製資料夾下檔案到另個資料夾
import os, random, shutil
from sqlalchemy import true


def copyFile(fileDir, Copy, num):

    if Copy == True:

        pathDir = os.listdir(fileDir)
        sample = random.sample(pathDir, num)
        print(sample)

        for name in sample:
            shutil.copyfile(fileDir + name, tarDir + name)
        print('複製成功！')

    else:
        print('未複製成功！')


if __name__ == '__main__':
    fileDir = "C:/Users/Allen/Desktop/2/"
    tarDir = 'C:/Users/Allen/Desktop/1/'
    numFile = 3  # 欲隨機複製檔案的個數
    readyCopy = False  # 防手誤 True表示開始複製

    copyFile(fileDir, readyCopy, numFile)
