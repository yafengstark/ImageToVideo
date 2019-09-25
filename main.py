import os
import cv2
import numpy as np

# path = '需要调用的图片路径 例如：C:/picture/'
path = 'E:/biaoqingbao'
filelist = os.listdir(path)

fps = 1  # 视频每秒24帧
unit = 100
size = (640, 480)  # 需要转为视频的图片的尺寸
# 可以使用cv2.resize()进行修改
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video = cv2.VideoWriter(path+"/VideoTest1.mp4", fourcc, fps, size)
# 视频保存在当前目录下

for item in filelist:
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path +'\\' +item

        print('image: ' + item)

        img = cv2.imread(item)
        cv2.imshow('image', img)

        video.write(img)

video.release()
cv2.destroyAllWindows()
