# -*- coding:utf-8 -*-

import VideoUtil
import ImageUtil

import os
if __name__ == '__main__':

    bqbDir = '/Users/tongyanfeng/Pictures/ChineseBQB'

    for dir_image in os.listdir(bqbDir):  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表

        if("." in dir_image):
            continue
        print dir_image
        # ImageUtil.removeImages()
        imagesDir = os.path.abspath(os.path.join(bqbDir,dir_image))

        print imagesDir

        ImageUtil.resizeImage(imagesDir)
        # os.path.abspath(os.path.join(path_name, dir_image))
        VideoUtil.getVideo(dir_image+'.avi')
        ImageUtil.removeImages()



