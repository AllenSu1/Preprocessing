import cv2

# 調參
height = 100  #圍籬高度
outline = 20  #警戒線外圍

out_flag = False
resize_flag = False  # 是否resize
video_path = r'D:\ntut\Any\code\canny\dataset\IMG_0337.MOV'
frame_freq = 1  # frame_freq 幀取一幀執行程式

# 主程式

tracker_list = []
# colors = [(0,0,255)]  # 設定三個外框顏色
colors = [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]  # 設定三個外框顏色
for i in range(len(colors)):
    tracker = cv2.TrackerCSRT_create()  # 創建三組追蹤器
    tracker_list.append(tracker)

tracking = False  # 設定 False 表示尚未開始追蹤
cap = cv2.VideoCapture(video_path)  # 讀取某個影片

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output2.mov', fourcc, 10.0, size)
a = 0
# 刪減影片影格使用
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    if resize_flag:
        frame = cv2.resize(frame, size)  # 縮小尺寸，加快速度

    keyName = cv2.waitKey(1)

    # 為了避免影片影格太多，所以採用 10 幀取一幀，加快處理速度
    if a % frame_freq == 0:
        if keyName == ord('q'):
            break
        if tracking == False:
            # 如果尚未開始追蹤，就開始標記追蹤物件的外框
            for i in tracker_list:
                area = cv2.selectROI('oxxostudio',
                                     frame,
                                     showCrosshair=False,
                                     fromCenter=False)
                i.init(frame, area)  # 初始化追蹤器
            tracking = True  # 設定可以開始追蹤
        if tracking:
            for i in range(len(tracker_list)):
                success, point = tracker_list[i].update(frame)
                if i != 0:
                    p_rec_x = rec_x
                    p_rec_y = rec_y

                    if out_flag:
                        p_out_rec_x = rec_x
                        p_out_rec_y = rec_y + outline

                # 追蹤成功後，不斷回傳左上和右下的座標
                if success:
                    p1 = [int(point[0]), int(point[1])]
                    p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
                    # cv2.rectangle(frame, p1, p2, colors[i], 1)   # 根據座標，繪製四邊形，框住要追蹤的物件
                    rec_x = (p1[0] + p2[0]) // 2
                    rec_y = (p1[1] + p2[1]) // 2
                    cv2.circle(frame, (rec_x, rec_y), 3, colors[i], -1)
                    cv2.circle(frame, (rec_x, rec_y - height), 3, colors[i],
                               -1)  # 圍籬頂點
                    cv2.line(frame, (rec_x, rec_y), (rec_x, rec_y - height),
                             colors[i], 1)  # 頂底連線

                    if i != 0:
                        cv2.line(frame, (p_rec_x, p_rec_y), (rec_x, rec_y),
                                 colors[i], 1)  # 頂底連線
                        cv2.line(frame, (p_rec_x, p_rec_y - height),
                                 (rec_x, rec_y - height), colors[i], 1)  # 頂底連線

                    if out_flag:  # 是否要警戒線
                        cv2.circle(frame, (rec_x, rec_y + outline), 3,
                                   (255, 255, 0), -1)
                        if i != 0:
                            cv2.line(frame, (p_out_rec_x, p_out_rec_y),
                                     (rec_x, rec_y + outline), (255, 255, 0),
                                     1)  # 頂底連線

                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.putText(frame, 'Virtual Fence', (20, 40), font, 1,
                                (0, 0, 255), 2, cv2.LINE_AA)
                    if out_flag:
                        cv2.putText(frame, 'Cordon', (20, 80), font, 1,
                                    (255, 255, 0), 2, cv2.LINE_AA)

        out.write(frame)
        cv2.imshow('oxxostudio', frame)
    a = a + 1

cap.release()
cv2.destroyAllWindows()