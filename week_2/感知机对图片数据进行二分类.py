# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
#import tf as tf
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import os
import tensorflow as tf


def creat_x_database(rootdir,resize_row,resize_col):
    #列出文件夹下所有的，目录和文件
    list = os.listdir(rootdir)
    # print(list)
    #创建一个随机矩阵，作为多个图片转换为矩阵后传入其中
    database=np.arange(len(list)*resize_row*resize_col*3).reshape(len(list)
    ,resize_row,resize_col,3)
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])    #把目录和文件名合成一个路径
        if os.path.isfile(path):                ##判断路径是否为文件
            image_raw_data = tf.gfile.FastGFile(path,'rb').read()#读取图片
            with tf.Session() as sess:
                img_data = tf.image.decode_jpeg(image_raw_data)#图片解码
                #压缩图片矩阵为指定大小
                resized=tf.image.resize_images(img_data,[resize_row,resize_col],method=0)
                database[i]=resized.eval()
    return database


def creat_y_database(length,classfication_value,one_hot_value):
    #创建一个适当大小的矩阵来接收
    array=np.arange(length*classfication_value).reshape(length,classfication_value)
    for i in range(0,length):
        array[i]=one_hot_value #这里采用one hot值来区别合格与不合格
    return array


#Perceptron
#数据线性可分，二分类数据
#此处为一元一次线性方程
class Model:
    def __init__(self):
        self.w=np.ones(len(database[0])-1,dtype=np.float32)
        self.b=0
        self.l_rate=0.1
        #self.data=data

    def sign(self,x,w,b):
        y=np.dot(x,w)+b
        return y

    #随机梯度下降法
    def fit(self,X_train,y_train):
        is_wrong=False
        while not is_wrong:
            wrong_count=0
            for d in range(len(X_train)):
                X=X_train[d]
                y=y_train[d]
                if y*self.sign(X,self.w,self.b)<=0:
                    self.w=self.w+self.l_rate*np.dot(y,X)
                    self.b=self.b+self.l_rate*y
                    wrong_count+=1
            if wrong_count==0:
                is_wrong=True
        return 'Perceptron Model!'

    def score(self):
        pass


#创建训练集
fail_x_data=creat_x_database('/Users/momo/Desktop/1',128,128)
true_x_data=creat_x_database('/Users/momo/Desktop/0',128,128)
x_data=np.vstack((fail_x_data,true_x_data))  #两个矩阵在列上进行合并
#创建标签集
fail_y_data=creat_y_database(fail_x_data.shape[0],2,[0,1])
true_y_data=creat_y_database(true_x_data.shape[0],2,[1,0])
y_data=np.vstack((fail_y_data,true_y_data))


perceptron=Model()
perceptron.fit(x_data,y_data)



