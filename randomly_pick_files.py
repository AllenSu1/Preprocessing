# 複製資料夾下檔案到另個資料夾
import os, random, shutil


def copyFile(fileDir):

    pathDir = os.listdir(fileDir)

    sample = random.sample(pathDir, 100)
    print(sample)

    for name in sample:
        shutil.copyfile(fileDir + name, tarDir + name)


if __name__ == '__main__':
    fileDir = "D:/Dataset/Allen_thesis/vannamei/vannamei_v1/image/"
    tarDir = 'E:/test/'
    copyFile(fileDir)
