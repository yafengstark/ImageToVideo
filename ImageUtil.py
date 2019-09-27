# -*- coding:utf-8 -*-

import cv2
import os

import VideoUtil


# 按指定图像大小调整尺寸
def resize_image(image, height=640, width=480):
    top, bottom, left, right = (0, 0, 0, 0)

    # 获取图片尺寸
    h, w, _ = image.shape

    # 对于长宽不等的图片，找到最长的一边
    longest_edge = max(h, w)

    # 计算短边需要增加多少像素宽度才能与长边等长(相当于padding，长边的padding为0，短边才会有padding)
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass  # pass是空语句，是为了保持程序结构的完整性。pass不做任何事情，一般用做占位语句。

    # RGB颜色
    BLACK = [0, 0, 0]
    # 给图片增加padding，使图片长、宽相等
    # top, bottom, left, right分别是各个边界的宽度，cv2.BORDER_CONSTANT是一种border type，表示用相同的颜色填充
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    # 调整图像大小并返回图像，目的是减少计算量和内存占用，提升训练速度
    return cv2.resize(constant, (height, width))


def resizeImage(path_name):
    num = 0
    for dir_image in os.listdir(path_name):  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        full_path = os.path.abspath(os.path.join(path_name, dir_image))

        if dir_image.endswith('.jpg'):
            print dir_image
            image = cv2.imread(full_path)
            if image == None:
                continue
            image = resize_image(image)
            # 将尺寸调整好的图片保存起来
            image_name = '%s%d.jpg' % ('resize_image', num)  # 注意这里图片名一定要加上扩展名，否则后面imwrite的时候会报错
            cv2.imwrite(image_name, image)
            num = num + 1

def removeImages():
    '''
    移除当前目录的文件
    :return:
    '''
    for dir_image in os.listdir('./'):  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        if dir_image.endswith('.jpg'):
            os.remove(dir_image)



if __name__ == '__main__':
    removeImages()