# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:49:40 2020

@author: Allen
"""

import os, random, shutil


def copyFile(fileDir):
    # 1
	pathDir = os.listdir(fileDir)

    # 2
	sample = random.sample(pathDir, 2000)
	print (sample)
	
	# 3
	for name in sample:
		shutil.copyfile(fileDir+name, tarDir+name)
if __name__ == '__main__':
	fileDir = "D:/Dataset/dogs_and_cats/train/cat/"
	tarDir = 'D:/Dataset/dogs_and_cats/z_test/train/cats/'
	copyFile(fileDir)