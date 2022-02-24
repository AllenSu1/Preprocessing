# 改xml類別
import xml.etree.ElementTree as ET
import shutil
import os

original_path = r"D:\Dataset\Allen_thesis\net\VOC2007"
target_path = r"D:\Dataset\Allen_thesis\test\VOC2007"
old_classes = ["whole"]  # 需要的類別
new_classes = "vannamei"  # 改新的類別


# 尋找包含"coffee"類別的文件,並將xml、jpg複製到指定文件夾
def search_file():
    print("step1: search file.")
    for file_name in os.listdir(os.path.join(original_path, "Annotations")):
        old_ann_path = os.path.join(original_path, "Annotations", file_name)
        old_img_path = os.path.join(original_path, "JPEGImages",
                                    file_name.split('.')[0] + '.jpg')
        new_ann_path = os.path.join(target_path, "Annotations", file_name)
        new_img_path = os.path.join(target_path, "JPEGImages",
                                    file_name.split('.')[0] + '.jpg')

        print(old_ann_path)

        # 打開xml文件進行解析
        in_file = open(old_ann_path, encoding="utf-8")
        tree = ET.parse(in_file)  # ET是一个xml文件解析庫，ET.parse（）打开xml文件。parse--"解析"
        root = tree.getroot()  # 獲取根節點

        for obj in root.findall('object'):  # 找到根節點下所有“object”節點
            name = str(
                obj.find('name').text)  # 找到object節點下name子節點的值，不考慮part下的name。
            if name in old_classes:
                # 將符合的文件（xml、jpg）複製到指定文件夾
                shutil.copyfile(old_ann_path, new_ann_path)
                shutil.copyfile(old_img_path, new_img_path)
                break


# 找到文件中的"coffee"，修改或删除其他類別和part標籤。
def search_person_vehicle():
    print("step2: filter classes.")
    for file_name in os.listdir(os.path.join(target_path, "Annotations")):
        file_path = os.path.join(target_path, "Annotations", file_name)
        print(file_path)
        in_file = open(file_path, encoding="utf-8")
        tree = ET.parse(in_file)  # ET是一个xml文件解析庫，ET.parse（）打开xml文件。parse--"解析"
        root = tree.getroot()  # 獲取根節點

        for obj in root.findall('object'):  # 找到根節點下所有“object”節點
            name = str(
                obj.find('name').text)  # 找到object節點下name子節點的值，不考慮part下的name。
            # 判断:如果不是列出的，（這裡可以用in對保留列表成员進行審查），則移除該object節點及其所有子節點。
            # if not (name in old_classes):
            #     root.remove(obj)

            # # 移除person目標上的其他標籤
            # for pa in obj.findall('part'):
            #     obj.remove(pa)

            # 將name為coffee的節點，改為good
            if name in old_classes:
                name = obj.find('name')
                name.text = "vannamei"

        tree.write(file_path)


if __name__ == '__main__':
    search_file()
    search_person_vehicle()
