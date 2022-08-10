import os

# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用

from moviepy.editor import *

video = VideoFileClip(
    r"C:\Users\Allen\Desktop\shrimp_video\org\test (2).mov")  # 讀取影片

output = video.resize((540, 960))  # 改變影片的尺寸
# output = video.resize(
#     width=480)  # 單獨指定寬度 width 或高度 height，就會根據比例，自動計算出另外的寬度或高度

output.write_videofile(
    r"C:\Users\Allen\Desktop\shrimp_video\resize\test (2)11.mp4",
    # fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac")
print('ok')