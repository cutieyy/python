# -*- coding: UTF-8 -*-

def chengfabiao(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("{}x{}={}\t".format(j,i,j*i),end='')
        print()


number=int(input("输入乘法表的行数："))
chengfabiao(number)
