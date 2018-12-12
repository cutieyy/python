# -*- coding:utf-8 -*-

__author__ = 'cutieyy'

import os
DIR1 = '/Users/momo/Desktop/normalvideo' #要统计的文件夹
DIR2 = '/Users/momo/Desktop/normalvideo清晰'
DIR3 = '/Users/momo/Desktop/normalvideo一般'
DIR4 = '/Users/momo/Desktop/normalvideo模糊'

len1=len([name for name in os.listdir(DIR1) if os.path.isfile(os.path.join(DIR1, name))])
len2=len([name for name in os.listdir(DIR2) if os.path.isfile(os.path.join(DIR2, name))])
len3=len([name for name in os.listdir(DIR3) if os.path.isfile(os.path.join(DIR3, name))])
len4=len([name for name in os.listdir(DIR4) if os.path.isfile(os.path.join(DIR4, name))])


print("normalvideo视频总数为：",len1)

print("normalvideo清晰视频总数为：",len2,"占比为：",len2/len1)

print("normalvideo一般视频总数为：",len3,"占比为：",len3/len1)

print("normalvideo模糊视频总数为：",len4,"占比为：",len4/len1)



