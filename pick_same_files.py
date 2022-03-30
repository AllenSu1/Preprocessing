# 複製(移動)資料夾下檔案對應的xml到另個資料夾
import os, random, shutil
from pathlib import Path


def copyFile(fileDir, xmlDir, tarDir):
    '''
    fileDir是獲取檔名的路徑
    xmlDir是fileDir所對應檔案的路徑
    tarDir複製(移動)檔案的路徑
    '''

    pathDir = os.listdir(fileDir)
    print(pathDir)

    for name in pathDir:
        name = os.path.splitext(name)[0] + '.xml'
        # shutil.copyfile(xmlDir + name, tarDir + name) # 複製
        shutil.move(xmlDir + name, tarDir + name)  # 移動


if __name__ == '__main__':
    fileDir = "D:/Dataset/Test/VOC2007/JPEGImages/"
    xmlDir = "D:/Dataset/Train/VOC2007/Annotations/"
    tarDir = 'D:/Dataset/Test/VOC2007/Annotations/'

    # 執行 複製(移動)資料夾下檔案對應的xml到另個資料夾
    copyFile(fileDir, xmlDir, tarDir)

    jpgFile = os.listdir(fileDir)
    xmlFile = os.listdir(tarDir)

    # 以下為檢驗部分 確認複製(移動)的檔案是否對應
    error = 0
    for i in range(len(jpgFile)):
        jpgFile[i] = os.path.splitext(jpgFile[i])[0]
        xmlFile[i] = os.path.splitext(xmlFile[i])[0]

        # print(jpgFile[i])
        # print(xmlFile[i])

        if jpgFile[i] == xmlFile[i]:
            pass
        else:
            error += 1

    if error == 0:
        print('執行成功！')