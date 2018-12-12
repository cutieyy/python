# -*- coding: UTF-8 -*-

def feibonaqi(num):
    n1=0
    n2=1
    count=2
    if num<=0:
        print("请输入一个正数:")
    elif num==1:
        print("斐波那契数列为：")
        print(n1)
    else:
        print("斐波那契数列为：")
        print(n1,',',n2,end=",")
        while(count<num):
            three=n1+n2
            print(three,end=",")
            n1=n2
            n2=three
            count+=1

number=int(input("请输入需要的个数："))
feibonaqi(number)
