from cv2 import cv2

org = cv2.imread(r'C:\Users\Allen\Desktop\blacky.jpg')
res = cv2.resize(org, (640,480))
cv2.imwrite('640_480.jpg', res)

