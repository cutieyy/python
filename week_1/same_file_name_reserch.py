# !/usr/bin/python
# encoding: utf-8

import os
import glob
from PIL import Image
#指定找到文件后，另存为的文件夹路径
outDir = os.path.abspath('/Users/momo/Desktop/output_0-45')

#指定第一个文件夹的位置
imageDir1 = os.path.abspath('/Users/momo/Desktop/0-45')

#定义要处理的第一个文件夹变量
image1 = [] #image1指文件夹里的文件，包括文件后缀格式；
imgname1 = [] #imgname1指里面的文件名称，不包括文件后缀格式

#通过glob.glob来获取第一个文件夹下，所有'.mp4'文件
imageList1 = glob.glob(os.path.join(imageDir1, '*.mp4'))

#遍历所有文件，获取文件名称（包括后缀）
for item in imageList1:
    image1.append(os.path.basename(item))

#遍历文件名称，去除后缀，只保留名称
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)

#对于第二个文件夹路径，做同样的操作
imageDir2 = os.path.abspath('/Users/momo/Desktop/0-45(1)')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.mp4'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)

#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。
for item1 in imgname1:
    for item2 in imgname2:
        if item1 == item2:
            dir = imageList1[imgname1.index(item1)]
            name = os.path.basename(dir)
            os.system(f'cp {dir} {outDir}')  # 执行终端命令

