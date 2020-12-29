# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:48:59 2020

@author: Blacky
"""
import os
import numpy as np
import cv2

def main():
    # input_path
    img_path = r'C:\Users\Allen\Desktop\choose'
    # output_path
    out_path = r'C:\Users\Allen\Desktop\choose\resize'
    # mode == 1 補值
    # mode == 2 線性插植
    mode = 1
    
    dim = (224, 224)
    for item in os.listdir(img_path):
        # 提取路徑名稱
        fname = os.path.splitext(item)
        os.path.split(fname[0])
        file_name = fname[0]
        path_com = os.path.join(img_path, item)
        img = cv_imread(path_com)
        # img = cv2.imread(path_com)
        if mode == 1:
            # 補值
            img = resize_keep_aspectratio(img)
        if mode == 2:
            # 線性插值
           img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(os.path.join(out_path, file_name + '.jpg'), img)


def resize_keep_aspectratio(image_src):
    dst_size = (224, 224)
    src_h, src_w = image_src.shape[:2]
    print(src_h, src_w)
    dst_h, dst_w = dst_size
    # 判断应该按哪个边做等比缩放
    h = dst_w * (float(src_h)/src_w)  # 按照ｗ做等比缩放
    w = dst_h * (float(src_w)/src_h)  # 按照h做等比缩放
    h = int(h)
    w = int(w)
    if h <= dst_h:
        image_dst = cv2.resize(image_src, (dst_w, int(h)))
    else:
        image_dst = cv2.resize(image_src, (int(w), dst_h))
    h_, w_ = image_dst.shape[:2]
    print(h_, w_)
    top = int((dst_h - h_) / 2)
    down = int((dst_h - h_+1) / 2)
    left = int((dst_w - w_) / 2)
    right = int((dst_w - w_+1) / 2)
    value = [0, 0, 0]
    borderType = cv2.BORDER_CONSTANT
    print(top, down, left, right)
    image_dst = cv2.copyMakeBorder(
        image_dst, top, down, left, right, borderType, None, value)
    return image_dst

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv處理的话，需要轉换成bgr，轉换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

if __name__ == '__main__':
    main()