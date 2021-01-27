import os, random, shutil

def copyFile(fileDir):

	pathDir = os.listdir(fileDir)

	sample = random.sample(pathDir, 2000)
	print (sample)
	
	for name in sample:
		shutil.copyfile(fileDir+name, tarDir+name)
if __name__ == '__main__':
	fileDir = "D:/Dataset/dogs_and_cats/train/cat/"
	tarDir = 'D:/Dataset/dogs_and_cats/z_test/train/cats/'
	copyFile(fileDir)