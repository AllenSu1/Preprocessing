# 複製資料夾下檔案對應的xml到另個資料夾
import os, random, shutil


def copyFile(fileDir, xmlDir, tarDir):
    '''
    fileDir是獲取檔名的路徑
    xmlDir是fileDir所對應檔案的路徑
    tarDir複製檔案的路徑
    '''

    pathDir = os.listdir(fileDir)
    print(pathDir)

    for name in pathDir:
        name = os.path.splitext(name)[0] + '.xml'
        shutil.copyfile(xmlDir + name, tarDir + name)


if __name__ == '__main__':
    fileDir = "D:/Dataset/VOC2007/JPEGImages/"
    xmlDir = "D:/Dataset/Allen_thesis/vannamei/vannamei_monkey/pic_black_all_label/"
    tarDir = 'D:/Dataset/VOC2007/Annotations/'
    copyFile(fileDir, xmlDir, tarDir)